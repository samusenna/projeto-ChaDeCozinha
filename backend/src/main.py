import os
import sys
import csv
import datetime
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS

# NÃO ALTERAR: adiciona caminho para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Flask
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
CORS(app)  # habilitar CORS

from src.models.user import db
from src.routes.user import user_bp
from src.routes.presentes import presentes_bp
from flask_mail import Mail, Message  # Importar Flask-Mail e Message

# Caminho do CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), 'database', 'escolhas.csv')

# Lista de presentes (pode ser removida se só usar CSV)
presentes = [
    {"id": 1, "nome": "Aparelho de jantar"},
    {"id": 2, "nome": "Jogo de panelas"},
    {"id": 3, "nome": "Jogo de copos"},
    {"id": 4, "nome": "Jogo de Talheres"},
    {"id": 5, "nome": "Jogo de xícaras"},
    {"id": 6, "nome": "Partos de sobremesa"},
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
    {"id": 49, "nome": "Concha para sorvete"},
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
    criar_csv()  # garante que o arquivo exista
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([convidado, presente, data_hora])

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

# Endpoint GET para listar presentes
@app.route("/presentes", methods=["GET"])
def listar_presentes():
    return jsonify(presentes)

# Endpoint POST para registrar escolha
@app.route("/escolher-presente", methods=["POST"])
def escolher_presente():
    dados = request.get_json()
    if not dados or "convidado" not in dados or "presente" not in dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    salvar_escolha_csv(dados["convidado"], dados["presente"])
    print(f"Convidado {dados['convidado']} escolheu {dados['presente']}")

    return jsonify({"sucesso": True, "mensagem": "Escolha registrada!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Configuração do Flask-Mail
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME", "samuelsenna21.09@gmail.com")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD", "jesusefiel123")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER", "samuelsenna21.09@gmail.com")

mail = Mail(app)

# 🔹 Teste de envio de e-mail (executa quando o app sobe)
with app.app_context():
    try:
        msg = Message(
            subject="Teste de Email",
            recipients=["samuelsenna13.13@gmail.com"],  # Troque pelo email real que receberá
            body="Este é um e-mail de teste enviado pelo Flask-Mail."
        )
        mail.send(msg)
        print("✅ Email enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")

# Passar a instância do mail para a blueprint de presentes (se ela realmente usar isso)
presentes_bp.mail = mail

# Registrar blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(presentes_bp, url_prefix='/api')

# Configuração do banco SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# Rota para servir arquivos estáticos
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
    app.run(host='0.0.0.0', port=5001, debug=True)
