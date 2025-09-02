import React from 'react';

// Mapeamento de IDs de presentes para caminhos de imagem
// As imagens devem estar na pasta public/images ou em assets/images
const IMAGENS_PRESENTES = {
  '1': 'src/img/AparelhoJantar.png',
  '2': 'src/img/JogoPanelas.png', 
  '3': 'src/img/',
  '4': 'src/img/',
  '5': 'src/img/',
  '6': 'src/img/',
  '7': 'src/img/', 
  '8': 'src/img/',
  '9': 'src/img/',
  '10': 'src/img/',
  '11': 'src/img/',
  '12': 'src/img/', 
  '13': 'src/img/',
  '14': 'src/img/',
  '15': 'src/img/',
  '16': 'src/img/',
  '17': 'src/img/', 
  '18': 'src/img/',
  '19': 'src/img/',
  '20': 'src/img/',
  '21': 'src/img/',
  '22': 'src/img/', 
  '23': 'src/img/',
  '24': 'src/img/',
  '25': 'src/img/',
  '26': 'src/img/',
  '27': 'src/img/', 
  '28': 'src/img/',
  '29': 'src/img/',
  '30': 'src/img/',
  '31': 'src/img/',
  '32': 'src/img/',
  '33': 'src/img/'
};

function PresenteCardComImagem({ presenteId, nomePresente, children }) {
  const imagemSrc = IMAGENS_PRESENTES[presenteId];

  return (
    <div className="presente-card">
      {imagemSrc ? (
        <img src={imagemSrc} alt={nomePresente} className="presente-imagem" />
      ) : (
        <div className="presente-icon">🎁</div> // Ícone padrão se a imagem não for encontrada
      )}
      <h3 className="presente-nome">{nomePresente}</h3>
      {children} {/* Renderiza os botões ou outros elementos passados como children */}
    </div>
  );
}

export default PresenteCardComImagem;
