import os
import sys
import csv
import datetime
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message  # Flask-Mail



# NÃO ALTERAR: adiciona caminho para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Flask
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
CORS(app)  # habilitar CORS

from src.models.user import db
from src.routes.user import user_bp
from src.routes.presentes import presentes_bp

# =======================================
# 📧 CONFIGURAÇÃO DE E-MAIL (SMTP)
# =======================================
# Exemplo com Gmail — substitua pelos seus dados
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "chacozinha14@gmail.com"       # <-- altere aqui
app.config["MAIL_PASSWORD"] = "avzm idxi kqtj ykdb" # <-- altere aqui
app.config["MAIL_DEFAULT_SENDER"] = ("Chá de Cozinha", "schacozinha14@gmail.com")

mail = Mail(app)

# =======================================

# Caminho do CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), 'database', 'escolhas.csv')

# Lista de presentes
presentes = [
    {"id": 1, "nome": "Aparelho de jantar"},
    {"id": 2, "nome": "Jogo de panelas"},
    {"id": 3, "nome": "Jogo de copos"},
    {"id": 4, "nome": "Jogo de Talheres"},
    {"id": 5, "nome": "Jogo de xícaras"},
    {"id": 6, "nome": "Pratos de sobremesa"},
    {"id": 7, "nome": "Taças Para vinho"},
    {"id": 8, "nome": "Faqueiro"},
    {"id": 9, "nome": "Cuscuzeira"},
    {"id": 10, "nome": "Peneira"},
    {"id": 11, "nome": "Porta tempero preto giratório"},
    {"id": 12, "nome": "Fruteira de mesa"},
    {"id": 13, "nome": "Formas e assadeiras"},
    {"id": 14, "nome": "Jarra de Suco"},
    {"id": 15, "nome": "Panos de Prato"},
    {"id": 16, "nome": "Tábua de Madeira"},
    {"id": 17, "nome": "Lixeira inox de banheiro"},
    {"id": 18, "nome": "Panela de pressão"},
    {"id": 19, "nome": "Abridor de Lata"},
    {"id": 20, "nome": "Escorredor de louças de inox"},
    {"id": 21, "nome": "Escorredor de macarrão"},
    {"id": 22, "nome": "Ralador"},
    {"id": 23, "nome": "Frigideira"},
    {"id": 24, "nome": "Potes de plástico Herméticos"},
    {"id": 25, "nome": "Potes de vidro"},
    {"id": 26, "nome": "Suporte de papel toalha"},
    {"id": 27, "nome": "Pano de pia"},
    {"id": 28, "nome": "Copo medidor"},
    {"id": 29, "nome": "Petisqueira de bambu"},
    {"id": 30, "nome": "Boleira"},
    {"id": 31, "nome": "Lixeira de cozinha"},
    {"id": 32, "nome": "Toalhas de banho"},
    {"id": 33, "nome": "Toalhas de rosto"},
    {"id": 34, "nome": "Kit lavabo"},
    {"id": 35, "nome": "Tapete banheiro"},
    {"id": 36, "nome": "Chuveiro 220V 6800W"},
    {"id": 37, "nome": "Assento para vaso sanitário"},
    {"id": 38, "nome": "Acessorios para banheiro"},
    {"id": 39, "nome": "Escova sanitária"},
    {"id": 40, "nome": "Organizadores"},
    {"id": 41, "nome": "Cabides"},
    {"id": 42, "nome": "Liquitificador"},
    {"id": 43, "nome": "Mixer"},
    {"id": 44, "nome": "Processador"},
    {"id": 45, "nome": "Espremedor de frutas"},
    {"id": 46, "nome": "Batedeira"},
    {"id": 47, "nome": "Ferro de passar"},
    {"id": 48, "nome": "Chaleira Elétrica"},
    {"id": 49, "nome": "Concha para sorvete"}
]

# Função para criar CSV se não existir
def criar_csv():
    if not os.path.exists(CSV_PATH):
        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Convidado", "Presente", "DataHora"])

# Função para gravar escolha no CSV
def salvar_escolha_csv(convidado, presente):
    criar_csv()
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([convidado, presente, data_hora])

# 📨 Função para enviar o CSV por e-mail
def enviar_csv_por_email():
    try:
        with app.app_context():
            msg = Message(
                subject="🎁 Novo presente escolhido - Lista atualizada",
                recipients=["talitacsilva090@gmail.com"],  # <-- altere aqui
                body="Olá! Um novo presente foi escolhido. Em anexo está a lista atualizada."
            )

            # Adiciona o CSV como anexo
            with open(CSV_PATH, "rb") as f:
                msg.attach("escolhas.csv", "text/csv", f.read())

            mail.send(msg)
            print("📨 E-mail enviado com sucesso!")
    except Exception as e:
        print(f"⚠️ Erro ao enviar e-mail: {e}")

# Função auxiliar: retorna os nomes já escolhidos
def carregar_presentes_escolhidos():
    nomes_escolhidos = set()
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                nome = linha["Presente"].strip().lower()
                nomes_escolhidos.add(nome)
    return nomes_escolhidos

# Endpoint GET para listar presentes disponíveis
@app.route("/presentes", methods=["GET"])
def listar_presentes():
    nomes_escolhidos = carregar_presentes_escolhidos()
    presentes_disponiveis = [
        p for p in presentes if p["nome"].strip().lower() not in nomes_escolhidos
    ]
    return jsonify(presentes_disponiveis)

# Endpoint POST para registrar escolha e enviar e-mail
@app.route("/escolher-presente", methods=["POST"])
def escolher_presente():
    dados = request.get_json()
    if not dados or "convidado" not in dados or "presente" not in dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    salvar_escolha_csv(dados["convidado"], dados["presente"])
    enviar_csv_por_email()  # <-- envia o CSV atualizado
    print(f"Convidado {dados['convidado']} escolheu {dados['presente']}")

    return jsonify({"sucesso": True, "mensagem": "Escolha registrada e e-mail enviado!"}), 200

# Servir frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
