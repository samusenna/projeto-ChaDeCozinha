from flask import Blueprint, request, jsonify
import csv
import os
from datetime import datetime

presentes_bp = Blueprint('presentes', __name__)

# Caminho para o arquivo CSV que funcionará como planilha
CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'escolhas.csv')

# Dados iniciais dos presentes
PRESENTES_INICIAIS = [
    {'id': '1', 'nome': 'Aparelho de jantar', 'disponivel': True},
    {'id': '2', 'nome': 'Jogo de panelas', 'disponivel': True},
    {'id': '3', 'nome': 'Jogo de copos', 'disponivel': True},
    {'id': '4', 'nome': 'Jogo de Talheres', 'disponivel': True},
    {'id': '5', 'nome': 'Jogo de xícaras', 'disponivel': True},
    {'id': '6', 'nome': 'Partos de sobremesa', 'disponivel': True},
    {'id': '7', 'nome': 'Taças Para vinho',  'disponivel': True},
    {'id': '8', 'nome': 'Faqueiro', 'disponivel': True},
    {'id': '9', 'nome': 'Cuscuzeira', 'disponivel': True},
    {'id': '10', 'nome': 'Peneira', 'disponivel': True}, 
    {'id': '11', 'nome': 'Porta tempero preto giratório',  'disponivel': True},
    {'id': '12', 'nome': 'Fruteira de mesa', 'disponivel': True},
    {'id': '13', 'nome': 'Formas e assadeiras', 'disponivel': True},
    {'id': '14', 'nome': 'Jarra de Suco', 'disponivel': True},
    {'id': '15', 'nome': 'Panos de Prato', 'disponivel': True},
    {'id': '16', 'nome': 'Tábua de vidro', 'disponivel': True},
    {'id': '17', 'nome': 'Lixeira inox de banheiro',  'disponivel': True},
    {'id': '18', 'nome': 'Panela de pressão', 'disponivel': True},
    {'id': '19', 'nome': 'Abridor de Lata', 'disponivel': True},
    {'id': '20', 'nome': 'Escorredor de louças de inox', 'disponivel': True}, 
    {'id': '21', 'nome': 'Escorredor de macarrão',  'disponivel': True},
    {'id': '22', 'nome': 'Ralador', 'disponivel': True},
    {'id': '23', 'nome': 'Frigideira', 'disponivel': True},
    {'id': '24', 'nome': 'Potes de plástico Herméticos', 'disponivel': True},
    {'id': '25', 'nome': 'Potes de vidro', 'disponivel': True},
    {'id': '28', 'nome': 'Suporte de papel toalha', 'disponivel': True},
    {'id': '29', 'nome': 'Pano de pia', 'disponivel': True},
    {'id': '30', 'nome': 'Copo medidor', 'disponivel': True},
    {'id': '32', 'nome': 'Petisqueira de bambu', 'disponivel': True},
    {'id': '33', 'nome': 'Boleira', 'disponivel': True},
    {'id': '34', 'nome': 'Lixeira de cozinha', 'disponivel': True},
    {'id': '35', 'nome': 'Toalhas de banho', 'disponivel': True},
    {'id': '36', 'nome': 'Toalhas de rosto', 'disponivel': True},
    {'id': '37', 'nome': 'Kit lavabo',  'disponivel': True},
    {'id': '38', 'nome': 'Tapete banheiro', 'disponivel': True},
    {'id': '39', 'nome': 'Chuveiro 220V 6800W', 'disponivel': True},
    {'id': '40', 'nome': 'Assento para vaso sanitário', 'disponivel': True},
    {'id': '41', 'nome': 'Acessorios para banheiro', 'disponivel': True},
    {'id': '42', 'nome': 'Escova sanitária', 'disponivel': True},
    {'id': '43', 'nome': 'Organizadores', 'disponivel': True},
    {'id': '44', 'nome': 'Cabides', 'disponivel': True},
    {'id': '45', 'nome': 'Liquitificador', 'disponivel': True},
    {'id': '46', 'nome': 'Mixer', 'disponivel': True},
    {'id': '47', 'nome': 'Processador',  'disponivel': True},
    {'id': '48', 'nome': 'Espremedor de frutas', 'disponivel': True},
    {'id': '49', 'nome': 'Batedeira', 'disponivel': True},
    {'id': '50', 'nome': 'Ferro de passar', 'disponivel': True},
    {'id': '51', 'nome': 'Chaleira Elétrica', 'disponivel': True},
    {'id': '52', 'nome': 'Concha para sorvete', 'disponivel': True}    
    ]

def inicializar_csv():
    """Inicializa o arquivo CSV se não existir"""
    if not os.path.exists(CSV_FILE):
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Convidado', 'Presente', 'Data/Hora'])

def obter_presentes_escolhidos():
    """Obtém a lista de presentes já escolhidos do CSV"""
    if not os.path.exists(CSV_FILE):
        return []
    
    escolhidos = []
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            escolhidos.append({
                'nome': row['Presente']
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
                e['nome'] == presente['nome']
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
        
        if not dados or not dados.get('convidado') or not dados.get('presente'):
            return jsonify({'erro': 'Dados incompletos'}), 400
        
        inicializar_csv()
        
        # Verificar se o presente ainda está disponível
        escolhidos = obter_presentes_escolhidos()
        ja_escolhido = any(
            e['nome'] == dados['presente']
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
                    'data_hora': row['Data/Hora']
                })
        
        return jsonify(escolhas)
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

