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
    {"id": 16, "nome": "Tábua de vidro"},
    {"id": 17, "nome": "Lixeira inox de banheiro"},
    {"id": 18, "nome": "Panela de pressão"},
    {"id": 19, "nome": "Abridor de Lata"},
    {"id": 20, "nome": "Escorredor de louças de inox"},
    {"id": 21, "nome": "Escorredor de macarrão"},
    {"id": 22, "nome": "Ralador"},
    {"id": 23, "nome": "Frigideira"},
    {"id": 24, "nome": "Potes de plástico Herméticos"},
    {"id": 25, "nome": "Potes de vidro"},
    {"id": 28, "nome": "Suporte de papel toalha"},
    {"id": 29, "nome": "Pano de pia"},
    {"id": 30, "nome": "Copo medidor"},
    {"id": 32, "nome": "Petisqueira de bambu"},
    {"id": 33, "nome": "Boleira"},
    {"id": 34, "nome": "Lixeira de cozinha"},
    {"id": 35, "nome": "Toalhas de banho"},
    {"id": 36, "nome": "Toalhas de rosto"},
    {"id": 37, "nome": "Kit lavabo"},
    {"id": 38, "nome": "Tapete banheiro"},
    {"id": 39, "nome": "Chuveiro 220V 6800W"},
    {"id": 40, "nome": "Assento para vaso sanitário"},
    {"id": 41, "nome": "Acessorios para banheiro"},
    {"id": 42, "nome": "Escova sanitária"},
    {"id": 43, "nome": "Organizadores"},
    {"id": 44, "nome": "Cabides"},
    {"id": 45, "nome": "Liquitificador"},
    {"id": 46, "nome": "Mixer"},
    {"id": 47, "nome": "Processador"},
    {"id": 48, "nome": "Espremedor de frutas"},
    {"id": 49, "nome": "Batedeira"},
    {"id": 50, "nome": "Ferro de passar"},
    {"id": 51, "nome": "Chaleira Elétrica"},
    {"id": 52, "nome": "Concha para sorvete"}
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
