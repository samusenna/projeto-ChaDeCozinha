# 📋 Instruções de Uso - Chá de Cozinha

## 🎯 Para os Organizadores

### Como Iniciar a Aplicação

1. **Abra o terminal** e navegue até a pasta do projeto
2. **Inicie o servidor**:
   ```bash
   cd cha-backend
   source venv/bin/activate
   python src/main.py
   ```
3. **Acesse no navegador**: `http://localhost:5000`
4. **Compartilhe o link** com seus convidados

### Como Personalizar os Presentes

1. Abra o arquivo: `cha-backend/src/routes/presentes.py`
2. Encontre a seção `PRESENTES_INICIAIS`
3. Modifique os presentes conforme sua necessidade:
   ```python
   PRESENTES_INICIAIS = [
       {'id': '1', 'nome': 'Batedeira', 'cor': 'Vermelha', 'disponivel': True},
       {'id': '2', 'nome': 'Liquidificador', 'cor': 'Prata', 'disponivel': True},
       # Adicione ou modifique conforme necessário
   ]
   ```

### Como Acessar a Lista de Escolhas

1. **Via arquivo CSV**: Abra `cha-backend/src/database/escolhas.csv`
2. **Via navegador**: Acesse `http://localhost:5000/api/escolhas`
3. **Planilha do Excel**: Importe o arquivo CSV no Excel ou Google Sheets

## 👥 Para os Convidados

### Como Escolher um Presente

1. **Acesse o link** fornecido pelos organizadores
2. **Visualize os presentes** disponíveis na página
3. **Clique em "Escolher este presente"** no item desejado
4. **Digite seu nome completo** no formulário
5. **Clique em "Confirmar Escolha"**
6. **Pronto!** Seu presente foi reservado e removido da lista

### ⚠️ Importante para Convidados

- ✅ Cada presente só pode ser escolhido **uma vez**
- ✅ Após confirmar, o presente **desaparece** da lista
- ✅ Você receberá uma **mensagem de confirmação**
- ❌ **Não é possível** alterar a escolha depois de confirmar

## 🔧 Solução de Problemas

### Se a página não carregar:
1. Verifique se o servidor está rodando
2. Confirme o endereço: `http://localhost:5000`
3. Tente atualizar a página (F5)

### Se aparecer erro ao escolher presente:
1. Verifique sua conexão com a internet
2. Tente novamente em alguns segundos
3. Se persistir, contate os organizadores

### Se o presente "sumiu" antes de escolher:
- Significa que outro convidado escolheu primeiro
- Escolha outro presente disponível

## 📱 Compatibilidade

A aplicação funciona em:
- ✅ **Computadores** (Windows, Mac, Linux)
- ✅ **Tablets** (iPad, Android)
- ✅ **Celulares** (iPhone, Android)
- ✅ **Navegadores**: Chrome, Firefox, Safari, Edge

## 💡 Dicas para os Organizadores

### Antes do Evento:
- [ ] Teste a aplicação com alguns presentes
- [ ] Personalize a lista conforme seus desejos
- [ ] Compartilhe o link com antecedência
- [ ] Explique como funciona para os convidados

### Durante o Evento:
- [ ] Mantenha o computador/servidor ligado
- [ ] Monitore as escolhas pelo arquivo CSV
- [ ] Ajude convidados com dificuldades técnicas

### Após o Evento:
- [ ] Baixe o arquivo CSV com todas as escolhas
- [ ] Guarde uma cópia de segurança
- [ ] Use a lista para organizar a entrega dos presentes

## 📞 Contato

Em caso de dúvidas técnicas:
1. Verifique este manual primeiro
2. Teste em outro navegador/dispositivo
3. Reinicie o servidor se necessário

**Divirta-se com seu chá de cozinha! 🎉**

