import React from 'react';

// Mapeamento de IDs de presentes para caminhos de imagem
// As imagens devem estar na pasta public/images ou em assets/images
const IMAGENS_PRESENTES = {
  '1': '/assets/AparelhosDeJantar.jpg',
  '2': '/assets/JogoDePanelas.jpg', 
  '3': '/assets/JogoDeCopos.jpg',
  '4': '/assets/JogoDeTalher.jpg',
  '5': '/assets/JogoDeXicaras.jpg',
  '6': '/assets/TaçaDeSobremesa.jpg',
  '7': '/assets/JogoDeTaças.jpg', 
  '8': '/assets/Faqueiro.jpg',
  '9': '/assets/Cuzcuzeira.jpg',
  '10': '/assets/Peneiras.jpg',
  '11': '/assets/PortaTempeiros.jpg',
  '12': '/assets/FruteiraDeMesa.jpg', 
  '13': '/assets/Assadeira.jpg',
  '14': '/assets/JarraDeSuco.jpg',
  '15': '/assets/PanoDePrato.jpg',
  '16': '/assets/TabuaDeMadeira.jpg',
  '17': '/assets/Lixeira.jpg', 
  '18': '/assets/PanelaDePressao.jpg',
  '19': '/assets/AbridorDeLatas.jpg',
  '20': '/assets/EscorredorDeLouças.jpg',
  '21': '/assets/Escorredor.jpg',
  '22': '/assets/Ralador.jpg', 
  '23': '/assets/Frigideira.jpg',
  '24': '/assets/PotesHermeticos.jpg',
  '25': '/assets/PotesDeVidro.jpg',
  '26': '/assets/SuporteDeToalha.jpg',
  '27': '/assets/PanoDePia.jpg',
  '28': '/assets/CopoMedidor.jpg',
  '29': '/assets/Petisqueira.jpg',
  '30': '/assets/Boleira.jpg', 
  '31': '/assets/LixeiraCozinha.jpg',
  '32': '/assets/ToalhasBanho.jpg',
  '33': '/assets/ToalhasRosto.jpg',
  '34': '/assets/Utensilioslavabo.jpg', 
  '35': '/assets/TapeteBanheiro.jpg',
  '36': '/assets/Chuveiro.jpg',
  '37': '/assets/ACentoVaso.jpg',
  '38': '/assets/AcessoriosBanheiro.jpg',
  '39': '/assets/EscovaSanitaria.jpg', 
  '40': '/assets/Organizador.jpg',
  '41': '/assets/Cabides.jpg',
  '42': '/assets/Liquidificador.jpg',
  '43': '/assets/Mixer.jpg',
  '44': '/assets/Processador.jpg', 
  '45': '/assets/Espremedor.jpg',
  '46': '/assets/Batedeira.jpg',
  '47': '/assets/FerroDePassar.jpg',
  '48': '/assets/Chaleira.jpg',
  '49': '/assets/CochaSorvete.jpg'
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
