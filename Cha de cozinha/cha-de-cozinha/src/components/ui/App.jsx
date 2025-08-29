import { useState, useEffect } from 'react'
import { Button } from './button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './card.jsx'
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from './dialog.jsx'
import { Input } from './input.jsx'
import { Label } from './label.jsx'
import { Gift, Heart, CheckCircle, AlertCircle } from 'lucide-react'
import './App.css'

function App() {
  const [presentes, setPresentes] = useState([])
  const [presenteSelecionado, setPresenteSelecionado] = useState(null)
  const [nomeConvidado, setNomeConvidado] = useState('')
  const [dialogAberto, setDialogAberto] = useState(false)
  const [mensagem, setMensagem] = useState('')
  const [tipoMensagem, setTipoMensagem] = useState('sucesso') // 'sucesso' ou 'erro'
  const [carregando, setCarregando] = useState(false)

  // Simulação de dados mockados
  useEffect(() => {
    const presentesFake = [
      { id: 1, nome: 'Panela', cor: 'Vermelha' },
      { id: 2, nome: 'Conjunto de Facas', cor: 'Prata' },
      { id: 3, nome: 'Jogo de Pratos', cor: 'Branco' },
    ]
    setPresentes(presentesFake)
  }, [])

  const handleEscolherPresente = (presente) => {
    setPresenteSelecionado(presente)
    setDialogAberto(true)
  }

  const handleConfirmarEscolha = () => {
    if (!nomeConvidado.trim()) {
      setMensagem('Por favor, digite seu nome.')
      setTipoMensagem('erro')
      return
    }

    // Simulação de sucesso
    setMensagem(`Obrigado, ${nomeConvidado}! Sua escolha foi registrada: ${presenteSelecionado.nome} ${presenteSelecionado.cor}.`)
    setTipoMensagem('sucesso')

    setNomeConvidado('')
    setPresenteSelecionado(null)
    setDialogAberto(false)

    setTimeout(() => setMensagem(''), 5000)
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
            <h1 className="text-4xl font-bold text-gray-800">Nosso Chá de Cozinha</h1>
            <Heart className="text-rose-500 w-8 h-8" />
          </div>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Queridos amigos e familiares, escolham um presente especial para nossa nova cozinha! 
            Cada item será uma lembrança carinhosa de vocês em nosso lar.
          </p>
        </div>

        {/* Mensagem de feedback */}
        {mensagem && (
          <div className={`mb-6 p-4 border rounded-lg text-center ${
            tipoMensagem === 'sucesso' 
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

        {/* Lista de presentes */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {(presentes || []).map((presente) => (
            <Card key={presente.id} className="hover:shadow-lg transition-shadow duration-300 bg-white">
              <CardHeader className="text-center">
                <div className="flex justify-center mb-2">
                  <Gift className="w-12 h-12 text-rose-500" />
                </div>
                <CardTitle className="text-xl text-gray-800">{presente.nome}</CardTitle>
                <CardDescription className="text-gray-600">
                  Cor: <span className="font-semibold">{presente.cor}</span>
                </CardDescription>
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
            <Gift className="w-16 h-16 text-gray-400 mx-auto mb-4" />
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
                Você escolheu: <strong>{presenteSelecionado?.nome} {presenteSelecionado?.cor}</strong>
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
            💕 Com amor e carinho, esperamos vocês em nossa celebração! 💕
          </p>
        </div>
      </div>
    </div>
  )
}

export default App
