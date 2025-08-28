from flask import Blueprint, request, jsonify
import csv
import os
from datetime import datetime

presentes_bp = Blueprint('presentes', __name__)

# Caminho para o arquivo CSV que funcionará como planilha
CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'escolhas.csv')

# Dados iniciais dos presentes
PRESENTES_INICIAIS = [
    {'id': '1', 'nome': 'Batedeira', 'cor': 'Vermelha', 'disponivel': True},
    {'id': '2', 'nome': 'Liquidificador', 'cor': 'Prata', 'disponivel': True},
    {'id': '3', 'nome': 'Torradeira', 'cor': 'Branca', 'disponivel': True},
    {'id': '4', 'nome': 'Cafeteira', 'cor': 'Preta', 'disponivel': True},
    {'id': '5', 'nome': 'Processador de Alimentos', 'cor': 'Azul', 'disponivel': True},
    {'id': '6', 'nome': 'Micro-ondas', 'cor': 'Inox', 'disponivel': True},
    {'id': '7', 'nome': 'Sanduicheira', 'cor': 'Vermelha', 'disponivel': True},
    {'id': '8', 'nome': 'Fritadeira Elétrica', 'cor': 'Preta', 'disponivel': True},
    {'id': '9', 'nome': 'Mixer', 'cor': 'Branca', 'disponivel': True},
    {'id': '10', 'nome': 'Panela Elétrica de Arroz', 'cor': 'Rosa', 'disponivel': True}
]

def inicializar_csv():
    """Inicializa o arquivo CSV se não existir"""
    if not os.path.exists(CSV_FILE):
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Convidado', 'Presente', 'Cor', 'Data/Hora'])

def obter_presentes_escolhidos():
    """Obtém a lista de presentes já escolhidos do CSV"""
    if not os.path.exists(CSV_FILE):
        return []
    
    escolhidos = []
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            escolhidos.append({
                'nome': row['Presente'],
                'cor': row['Cor']
            })
    return escolhidos

@presentes_bp.route('/presentes', methods=['GET'])
def listar_presentes():
    """Retorna a lista de presentes disponíveis"""
    try:
        inicializar_csv()
        escolhidos = obter_presentes_escolhidos()
        
        # Filtrar presentes disponíveis
        presentes_disponiveis = []
        for presente in PRESENTES_INICIAIS:
            ja_escolhido = any(
                e['nome'] == presente['nome'] and e['cor'] == presente['cor'] 
                for e in escolhidos
            )
            if not ja_escolhido:
                presentes_disponiveis.append(presente)
        
        return jsonify(presentes_disponiveis)
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@presentes_bp.route('/escolher-presente', methods=['POST'])
def escolher_presente():
    """Registra a escolha de um presente"""
    try:
        dados = request.get_json()
        
        if not dados or not dados.get('convidado') or not dados.get('presente') or not dados.get('cor'):
            return jsonify({'erro': 'Dados incompletos'}), 400
        
        inicializar_csv()
        
        # Verificar se o presente ainda está disponível
        escolhidos = obter_presentes_escolhidos()
        ja_escolhido = any(
            e['nome'] == dados['presente'] and e['cor'] == dados['cor'] 
            for e in escolhidos
        )
        
        if ja_escolhido:
            return jsonify({'erro': 'Este presente já foi escolhido por outro convidado'}), 409
        
        # Registrar a escolha no CSV
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                dados['convidado'],
                dados['presente'],
                dados['cor'],
                datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            ])
        
        return jsonify({'sucesso': True, 'mensagem': 'Presente escolhido com sucesso!'})
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@presentes_bp.route('/escolhas', methods=['GET'])
def listar_escolhas():
    """Retorna todas as escolhas registradas"""
    try:
        if not os.path.exists(CSV_FILE):
            return jsonify([])
        
        escolhas = []
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                escolhas.append({
                    'convidado': row['Convidado'],
                    'presente': row['Presente'],
                    'cor': row['Cor'],
                    'data_hora': row['Data/Hora']
                })
        
        return jsonify(escolhas)
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

