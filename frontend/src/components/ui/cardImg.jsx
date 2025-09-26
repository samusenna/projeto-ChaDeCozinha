import React from 'react';

// Mapeamento de IDs de presentes para caminhos de imagem
// As imagens devem estar na pasta public/images ou em assets/images
const IMAGENS_PRESENTES = {
  '1': 'src/img/AparelhosDeJantar.jpg',
  '2': 'src/img/JogoDePanelas.jpg', 
  '3': 'src/img/JogoDeCopos.jpg',
  '4': 'src/img/JogoDeTalher.jpg',
  '5': 'src/img/JogoDeXicaras.jpg',
  '6': 'src/img/TaçaDeSobremesa.jpg',
  '7': 'src/img/JogoDeTaças.jpg', 
  '8': 'src/img/Faqueiro.jpg',
  '9': 'src/img/Cuzcuzeira.jpg',
  '10': 'src/img/Peneiras.jpg',
  '11': 'src/img/PortaTempeiros.jpg',
  '12': 'src/img/FruteiraDeMesa.jpg', 
  '13': 'src/img/Assadeira.jpg',
  '14': 'src/img/JarraDeSuco.jpg',
  '15': 'src/img/PanoDePrato.jpg',
  '16': 'src/img/TabuaDeMadeira.jpg',
  '17': 'src/img/Lixeira.jpg', 
  '18': 'src/img/PanelaDePressao.jpg',
  '19': 'src/img/AbridorDeLatas.jpg',
  '20': 'src/img/EscorredorDeLouças.jpg',
  '21': 'src/img/Escorredor.jpg',
  '22': 'src/img/Ralador.jpg', 
  '23': 'src/img/Frigideira.jpg',
  '24': 'src/img/PotesHermeticos.jpg',
  '25': 'src/img/PotesDeVidro.jpg',
  '26': 'src/img/SuporteDeToalha.jpg',
  '27': 'src/img/PanoDePia.jpg',
  '28': 'src/img/CopoMedidor.jpg',
  '29': 'src/img/Petisqueira.jpg',
  '30': 'src/img/Boleira.jpg', 
  '31': 'src/img/LixeiraCozinha.jpg',
  '32': 'src/img/ToalhasBanho.jpg',
  '33': 'src/img/ToalhasRosto.jpg',
  '34': 'src/img/Utensilioslavabo.jpg', 
  '35': 'src/img/TapeteBanheiro.jpg',
  '36': 'src/img/Chuveiro.jpg',
  '37': 'src/img/ACentoVaso.jpg',
  '38': 'src/img/AcessoriosBanheiro.jpg',
  '39': 'src/img/EscovaSanitaria.jpg', 
  '40': 'src/img/Organizador.jpg',
  '41': 'src/img/Cabides.jpg',
  '42': 'src/img/Liquidificador.jpg',
  '43': 'src/img/Mixer.jpg',
  '44': 'src/img/Processador.jpg', 
  '45': 'src/img/Espremedor.jpg',
  '46': 'src/img/Batedeira.jpg',
  '47': 'src/img/FerroDePassar.jpg',
  '48': 'src/img/Chaleira.jpg',
  '49': 'src/img/CochaSorvete.jpg'
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
