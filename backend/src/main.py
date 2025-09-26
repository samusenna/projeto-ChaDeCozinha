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
    {"id": 1, "nome": "Conjunto de panelas", "cor": "Prata"},
    {"id": 2, "nome": "Jogo de copos", "cor": "Transparente"},
    {"id": 3, "nome": "Batedeira", "cor": "Vermelha"}
]

# Função para criar CSV se não existir
def criar_csv():
    if not os.path.exists(CSV_PATH):
        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Convidado", "Presente", "Cor", "DataHora"])

# Função para gravar escolha no CSV
def salvar_escolha_csv(convidado, presente, cor):
    criar_csv()  # garante que o arquivo exista
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([convidado, presente, cor, data_hora])

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
    if not dados or "convidado" not in dados or "presente" not in dados or "cor" not in dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    salvar_escolha_csv(dados["convidado"], dados["presente"], dados["cor"])
    print(f"Convidado {dados['convidado']} escolheu {dados['presente']} ({dados['cor']})")

    return jsonify({"sucesso": True, "mensagem": "Escolha registrada!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
