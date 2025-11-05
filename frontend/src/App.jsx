import { useState, useEffect } from 'react'
import cores from '/assets/Cores.png'
import CardComImagem from './components/ui/cardImg.jsx'
import { Button } from './components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './components/ui/card.jsx'
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from './components/ui/dialog.jsx'
import { Input } from './components/ui/input.jsx'
import { Label } from './components/ui/label.jsx'
import { Gift, Heart, CheckCircle, AlertCircle } from 'lucide-react'
import './style.css'


function App() {
  const [presentes, setPresentes] = useState([])
  const [presenteSelecionado, setPresenteSelecionado] = useState(null)
  const [nomeConvidado, setNomeConvidado] = useState('')
  const [dialogAberto, setDialogAberto] = useState(false)
  const [mensagem, setMensagem] = useState('')
  const [tipoMensagem, setTipoMensagem] = useState('sucesso') // 'sucesso' ou 'erro'
  const [carregando, setCarregando] = useState(false)

  // URL base da API - ajustar conforme necessário
  const API_BASE = 'https://sjsena.pythonanywhere.com/'
  // const API_BASE = 'http://localhost:5000'

  useEffect(() => {
    carregarPresentes()
  }, [])

  const carregarPresentes = async () => {
    try {
      setCarregando(true)
      const response = await fetch(`${API_BASE}/presentes`)
      if (response.ok) {
        const data = await response.json()
        setPresentes(data)
      } else {
        throw new Error('Erro ao carregar presentes')
      }
    } catch (error) {
      console.error('Erro ao carregar presentes:', error)
      setMensagem('Erro ao carregar a lista de presentes. Tente recarregar a página.')
      setTipoMensagem('erro')
    } finally {
      setCarregando(false)
    }
  }

  const handleEscolherPresente = (presente) => {
    setPresenteSelecionado(presente)
    setDialogAberto(true)
  }

  const handleConfirmarEscolha = async () => {
    if (!nomeConvidado.trim()) {
      setMensagem('Por favor, digite seu nome.')
      setTipoMensagem('erro')
      return
    }

    try {
      setCarregando(true)

      const dadosEscolha = {
        convidado: nomeConvidado.trim(),
        presente: presenteSelecionado.nome,
      }

      const response = await fetch(`${API_BASE}/escolher-presente`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',

        },
        body: JSON.stringify(dadosEscolha)
      })

      const resultado = await response.json()

      if (response.ok) {
        // Sucesso - recarregar lista de presentes
        await carregarPresentes()

        setMensagem(`Obrigado, ${nomeConvidado}! Sua escolha foi registrada: ${presenteSelecionado.nome}.`)
        setTipoMensagem('sucesso')

        // Limpar formulário e fechar dialog
        setNomeConvidado('')
        setPresenteSelecionado(null)
        setDialogAberto(false)

        // Limpar mensagem após 5 segundos
        setTimeout(() => setMensagem(''), 5000)
      } else {
        // Erro do servidor
        setMensagem(resultado.erro || 'Erro ao registrar sua escolha. Tente novamente.')
        setTipoMensagem('erro')
      }

    } catch (error) {
      console.error('Erro ao confirmar escolha:', error)
      setMensagem('Erro de conexão. Verifique sua internet e tente novamente.')
      setTipoMensagem('erro')
    } finally {
      setCarregando(false)
    }
  }

  const handleCancelar = () => {
    setNomeConvidado('')
    setPresenteSelecionado(null)
    setDialogAberto(false)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 to-rose-100 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Cabeçalho */}
        <div className="text-center mb-8">
          <div className="flex justify-center items-center gap-2 mb-4">
            <Heart className="text-rose-500 w-8 h-8" />
            <h1 className="text-4xl font-bold text-gray-800">Chá de Cozinha Da Talita</h1>
            <Heart className="text-rose-500 w-8 h-8" />
          </div>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto text-center">
            O casamento vem aí e o nosso novo lar está ganhando forma!
            Preparamos esta lista com muito carinho para montar cada cantinho da casa com amor. 
            Vai ser um prazer celebrar esse momento tão especial ao lado de mulheres incríveis como você!
          </p><br />

          <p className="text-lg text-gray-600 max-w-2xl mx-auto text-center">
            Observação: Assim que escolher o presente, por favor selecione no link <br /> ou me avise,
            para que possamos evitar duplicidades.
          </p><br />

          <p className="text-lg text-gray-600 max-w-2xl mx-auto text-center">
            Necessário confirmar presença.
          </p><br />

          <p className="text-lg text-gray-600 max-w-2xl mx-auto text-center">
            Com carinho, Talita.
          </p><br />

          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Escolha um itém da paleta de cor abaixo.
          </p>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
                        Branco - Preto - Inox.
            </p>
          <div style={{backgroundImage: `url(${cores})`,
          backgroundSize: 'centeer',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
          width: '100%',
          height: '100px'
          }}>  
          </div>
      </div>

      {/* Mensagem de feedback */}
      {mensagem && (
        <div className={`mb-6 p-4 border rounded-lg text-center ${tipoMensagem === 'sucesso'
            ? 'bg-green-100 border-green-200 text-green-800'
            : 'bg-red-100 border-red-200 text-red-800'
          }`}>
          {tipoMensagem === 'sucesso' ? (
            <CheckCircle className="inline w-5 h-5 mr-2" />
          ) : (
            <AlertCircle className="inline w-5 h-5 mr-2" />
          )}
          {mensagem}
        </div>
      )}

      {/* Indicador de carregamento */}
      {carregando && (
        <div className="text-center mb-6">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-rose-500"></div>
          <p className="mt-2 text-gray-600">Carregando...</p>
        </div>
      )}

      {/* Lista de presentes */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        {presentes.map((presente) => (
          <Card key={presente.id} className="hover:shadow-lg transition-shadow duration-300 bg-white">
            <CardHeader className="text-center">
              <CardComImagem key={presente.id}
                             presenteId={presente.id}
                             presenteSelecionado={presente.nome}>
           </CardComImagem>
              <CardTitle className="text-xl text-gray-800">{presente.nome}</CardTitle>
            </CardHeader>
            <CardContent className="text-center">
              <Button
                onClick={() => handleEscolherPresente(presente)}
                className="w-full bg-rose-500 hover:bg-rose-600 text-white"
                disabled={carregando}
              >
                Escolher este presente
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Mensagem quando não há presentes */}
      {!carregando && presentes.length === 0 && (
        <div className="text-center py-12">
          <h3 className="text-2xl font-semibold text-gray-600 mb-2">
            Todos os presentes foram escolhidos!
          </h3>
          <p className="text-gray-500">
            Obrigado a todos pela participação em nosso chá de cozinha!
          </p>
        </div>
      )}

      {/* Dialog de confirmação */}
      <Dialog open={dialogAberto} onOpenChange={setDialogAberto}>
        <DialogContent className="sm:max-w-md">
          <DialogHeader>
            <DialogTitle>Confirmar Escolha</DialogTitle>
            <DialogDescription>
              Você escolheu: <strong>{presenteSelecionado?.nome}</strong>
            </DialogDescription>
          </DialogHeader>
          <div className="space-y-4">
            <div>
              <Label htmlFor="nome">Seu nome</Label>
              <Input
                id="nome"
                value={nomeConvidado}
                onChange={(e) => setNomeConvidado(e.target.value)}
                placeholder="Digite seu nome completo"
                className="mt-1"
                disabled={carregando}
              />
            </div>
          </div>
          <DialogFooter className="gap-2">
            <Button variant="outline" onClick={handleCancelar} disabled={carregando}>
              Cancelar
            </Button>
            <Button
              onClick={handleConfirmarEscolha}
              className="bg-rose-500 hover:bg-rose-600"
              disabled={carregando}
            >
              {carregando ? 'Confirmando...' : 'Confirmar Escolha'}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* Rodapé */}
      <div className="text-center mt-12 pt-8 border-t border-gray-200">
        <p className="text-gray-600">
          💕 Com amor e carinho, espero você em minha celebração! 💕
        </p>
      </div>
    </div>
    </div >
  )
}

export default App