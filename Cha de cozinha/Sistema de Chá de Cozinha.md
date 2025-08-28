# Sistema de Chá de Cozinha

Uma aplicação web completa desenvolvida em React e Flask para gerenciar pedidos de chá de cozinha, permitindo que convidados escolham presentes que são automaticamente removidos da lista e registrados em uma planilha.

## 🎯 Funcionalidades

- **Interface Responsiva**: Design moderno e responsivo com Tailwind CSS
- **Seleção de Presentes**: Lista de eletrodomésticos com cores específicas
- **Sistema de Reserva**: Presentes escolhidos são automaticamente removidos da lista
- **Armazenamento em Planilha**: Dados salvos em arquivo CSV com nome do convidado, presente, cor e data/hora
- **Feedback Visual**: Mensagens de sucesso e erro para o usuário
- **Validação**: Verificação de dados antes do envio

## 🛠️ Tecnologias Utilizadas

### Frontend
- **React 18** com Vite
- **Tailwind CSS** para estilização
- **shadcn/ui** para componentes de interface
- **Lucide React** para ícones

### Backend
- **Flask** (Python)
- **Flask-CORS** para permitir requisições cross-origin
- **CSV** para armazenamento de dados

## 📁 Estrutura do Projeto

```
/
├── cha-de-cozinha/          # Frontend React
│   ├── src/
│   │   ├── components/ui/   # Componentes shadcn/ui
│   │   ├── App.jsx         # Componente principal
│   │   ├── App.css         # Estilos
│   │   └── main.jsx        # Ponto de entrada
│   ├── dist/               # Build de produção
│   └── package.json
│
├── cha-backend/            # Backend Flask
│   ├── src/
│   │   ├── routes/
│   │   │   ├── presentes.py # Rotas da API
│   │   │   └── user.py     # Rotas de usuário (template)
│   │   ├── models/         # Modelos do banco
│   │   ├── static/         # Arquivos estáticos (frontend)
│   │   ├── database/
│   │   │   └── escolhas.csv # Planilha com as escolhas
│   │   └── main.py         # Aplicação principal
│   ├── venv/               # Ambiente virtual Python
│   └── requirements.txt    # Dependências Python
│
└── README.md               # Esta documentação
```

## 🚀 Como Executar

### Desenvolvimento

1. **Backend (Flask)**:
   ```bash
   cd cha-backend
   source venv/bin/activate
   python src/main.py
   ```
   O backend estará disponível em `http://localhost:5000`

2. **Frontend (React)**:
   ```bash
   cd cha-de-cozinha
   pnpm run dev --host
   ```
   O frontend estará disponível em `http://localhost:5173`

### Produção

Para produção, o frontend é construído e servido pelo Flask:

1. **Construir o frontend**:
   ```bash
   cd cha-de-cozinha
   pnpm run build
   ```

2. **Copiar arquivos para o Flask**:
   ```bash
   cp -r cha-de-cozinha/dist/* cha-backend/src/static/
   ```

3. **Executar apenas o Flask**:
   ```bash
   cd cha-backend
   source venv/bin/activate
   python src/main.py
   ```

## 📊 API Endpoints

### `GET /api/presentes`
Retorna a lista de presentes disponíveis (não escolhidos ainda).

**Resposta**:
```json
[
  {
    "id": "1",
    "nome": "Batedeira",
    "cor": "Vermelha",
    "disponivel": true
  }
]
```

### `POST /api/escolher-presente`
Registra a escolha de um presente por um convidado.

**Corpo da requisição**:
```json
{
  "convidado": "Nome do Convidado",
  "presente": "Batedeira",
  "cor": "Vermelha"
}
```

**Resposta de sucesso**:
```json
{
  "sucesso": true,
  "mensagem": "Presente escolhido com sucesso!"
}
```

### `GET /api/escolhas`
Retorna todas as escolhas registradas.

**Resposta**:
```json
[
  {
    "convidado": "Maria Silva",
    "presente": "Batedeira",
    "cor": "Vermelha",
    "data_hora": "23/08/2025 15:26:20"
  }
]
```

## 📋 Lista de Presentes Padrão

1. Batedeira (Vermelha)
2. Liquidificador (Prata)
3. Torradeira (Branca)
4. Cafeteira (Preta)
5. Processador de Alimentos (Azul)
6. Micro-ondas (Inox)
7. Sanduicheira (Vermelha)
8. Fritadeira Elétrica (Preta)
9. Mixer (Branca)
10. Panela Elétrica de Arroz (Rosa)

## 💾 Armazenamento de Dados

Os dados são armazenados em um arquivo CSV localizado em:
`cha-backend/src/database/escolhas.csv`

**Formato do CSV**:
```csv
Convidado,Presente,Cor,Data/Hora
Maria Silva,Batedeira,Vermelha,23/08/2025 15:26:20
João Santos,Liquidificador,Prata,23/08/2025 15:26:59
```

## 🎨 Personalização

### Modificar Lista de Presentes
Edite o array `PRESENTES_INICIAIS` em `cha-backend/src/routes/presentes.py`:

```python
PRESENTES_INICIAIS = [
    {'id': '1', 'nome': 'Seu Presente', 'cor': 'Sua Cor', 'disponivel': True},
    # ... mais presentes
]
```

### Alterar Cores e Estilo
O projeto usa Tailwind CSS. As cores principais podem ser alteradas em `cha-de-cozinha/src/App.jsx`:
- `bg-rose-500` para cor principal
- `from-pink-50 to-rose-100` para gradiente de fundo

## 🔧 Dependências

### Frontend
- React 18.3.1
- Vite 6.3.5
- Tailwind CSS
- shadcn/ui components
- Lucide React icons

### Backend
- Flask 3.1.1
- Flask-CORS 6.0.0
- Python 3.11+

## 📱 Responsividade

A aplicação é totalmente responsiva e funciona bem em:
- Desktop (1024px+)
- Tablet (768px - 1023px)
- Mobile (até 767px)

## 🛡️ Segurança

- Validação de dados no frontend e backend
- Sanitização de entrada do usuário
- CORS configurado adequadamente
- Verificação de disponibilidade de presentes

## 🚀 Deploy

Para fazer deploy da aplicação:

1. Configure um servidor com Python 3.11+
2. Clone o projeto
3. Configure o ambiente virtual e instale dependências
4. Configure um servidor web (Nginx + Gunicorn recomendado)
5. Configure SSL/HTTPS para produção

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme se as portas 5000 (backend) e 5173 (frontend dev) estão disponíveis
3. Verifique os logs do console para erros específicos

## 📝 Licença

Este projeto foi desenvolvido especificamente para uso em chás de cozinha e eventos similares.

