import { useState } from 'react'
import axios from 'axios'
 
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
 
export default function LoginForm({ onLoginSuccess }) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [erro, setErro] = useState('')
  const [sucesso, setSucesso] = useState('')
  const [modoRegistro, setModoRegistro] = useState(false)
  const [senhaVisivel, setSenhaVisivel] = useState(false)
 
  const handleSubmit = async (e) => {
    e.preventDefault()
    setErro('')
    setSucesso('')
    setLoading(true)
 
    try {
      const endpoint = modoRegistro ? '/api/registrar' : '/api/login'
      const response = await axios.post(`${API_URL}${endpoint}`, {
        email,
        password
      })
 
      if (modoRegistro) {
        // Registro bem-sucedido
        setSucesso('✅ Usuário criado! Faça login agora.')
        setModoRegistro(false)
        setEmail('')
        setPassword('')
      } else {
        // Login bem-sucedido
        const { access_token } = response.data
        localStorage.setItem('token', access_token)
        localStorage.setItem('email', email)
        setSucesso('✅ Login realizado com sucesso!')
        
        // Chamada de callback
        if (onLoginSuccess) {
          onLoginSuccess(access_token)
        }
        
        // Limpar form
        setEmail('')
        setPassword('')
      }
    } catch (error) {
      const mensagem = error.response?.data?.detail || 'Erro ao processar requisição'
      
      if (modoRegistro && 'Email já registrado' in mensagem) {
        setErro('❌ Este email já está registrado. Faça login!')
      } else if (!modoRegistro && 'Email ou senha incorretos' in mensagem) {
        setErro('❌ Email ou senha incorretos')
      } else {
        setErro(`❌ ${mensagem}`)
      }
    } finally {
      setLoading(false)
    }
  }
 
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-2xl p-8 w-full max-w-md">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">🔐 Login</h1>
          <p className="text-gray-600">
            {modoRegistro 
              ? 'Crie sua conta para começar' 
              : 'Entre na sua conta'}
          </p>
        </div>
 
        {/* Mensagens */}
        {erro && (
          <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-red-700 text-sm">{erro}</p>
          </div>
        )}
 
        {sucesso && (
          <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
            <p className="text-green-700 text-sm">{sucesso}</p>
          </div>
        )}
 
        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Email */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              📧 Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="seu@email.com"
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
            />
          </div>
 
          {/* Senha */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              🔑 Senha
            </label>
            <div className="relative">
              <input
                type={senhaVisivel ? 'text' : 'password'}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                required
                minLength="6"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
              />
              <button
                type="button"
                onClick={() => setSenhaVisivel(!senhaVisivel)}
                className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
              >
                {senhaVisivel ? '🙈' : '👁️'}
              </button>
            </div>
          </div>
 
          {/* Botão de Submit */}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-2 rounded-lg font-semibold hover:from-blue-700 hover:to-indigo-700 transition disabled:opacity-50 disabled:cursor-not-allowed mt-6"
          >
            {loading 
              ? '⏳ Processando...' 
              : (modoRegistro ? '✅ Criar Conta' : '🔓 Entrar')
            }
          </button>
        </form>
 
        {/* Toggle Login/Registro */}
        <div className="mt-6 text-center">
          <p className="text-gray-600 text-sm">
            {modoRegistro 
              ? 'Já tem uma conta?' 
              : 'Não tem uma conta?'
            }
            {' '}
            <button
              type="button"
              onClick={() => {
                setModoRegistro(!modoRegistro)
                setErro('')
                setSucesso('')
                setEmail('')
                setPassword('')
              }}
              className="text-blue-600 font-semibold hover:text-blue-700 transition"
            >
              {modoRegistro ? 'Faça Login' : 'Crie uma'}
            </button>
          </p>
        </div>
 
        {/* Teste Sem Registro */}
        {!modoRegistro && (
          <div className="mt-6 pt-6 border-t border-gray-200">
            <p className="text-gray-600 text-xs text-center mb-3">
              🧪 Teste sem se registrar:
            </p>
            <button
              type="button"
              onClick={() => {
                setEmail('demo@example.com')
                setPassword('demo123456')
              }}
              className="w-full text-sm bg-gray-100 text-gray-700 py-2 rounded-lg hover:bg-gray-200 transition font-medium"
            >
              Usar Credenciais Demo
            </button>
          </div>
        )}
      </div>
    </div>
  )
}