import { useState } from 'react';
import { gerarSenha, gerarPassphrase } from '../services/api';

export default function PasswordGenerator({ onPasswordGenerated, setLastPassword }) {
  const [tamanho, setTamanho] = useState(16);
  const [senha, setSenha] = useState('');
  const [loading, setLoading] = useState(false);
  const [tipo, setTipo] = useState('random');

  const handleGerar = async (tipo) => {
    setLoading(true);
    try {
      const data = tipo === 'random' 
        ? await gerarSenha(tamanho)
        : await gerarPassphrase();
      setSenha(data.senha);
      setTipo(data.tipo);
      setLastPassword(data);
      onPasswordGenerated();
    } catch (error) {
      alert('❌ ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-8">
      <h2 className="text-2xl font-bold mb-6">Gerar Senha</h2>
      
      <div className="mb-6">
        <label className="block text-sm font-medium mb-2">Comprimento da Senha</label>
        <input
          type="range"
          min="6"
          max="32"
          value={tamanho}
          onChange={(e) => setTamanho(Number(e.target.value))}
          className="w-full"
        />
        <p className="text-sm text-gray-600 mt-2">{tamanho} caracteres</p>
      </div>

      <div className="space-y-3 mb-6">
        <button
          onClick={() => handleGerar('random')}
          disabled={loading}
          className="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700"
        >
          {loading ? '⏳' : '🔐'} Gerar Senha Aleatória
        </button>
        
        <button
          onClick={() => handleGerar('passphrase')}
          disabled={loading}
          className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700"
        >
          {loading ? '⏳' : '🎲'} Gerar Passphrase
        </button>
      </div>

      {senha && (
        <div className="bg-gray-100 p-4 rounded-lg">
          <p className="text-sm text-gray-600 mb-2">Sua senha:</p>
          <p className="text-lg font-mono font-bold break-all select-all">{senha}</p>
          <button
            onClick={() => navigator.clipboard.writeText(senha)}
            className="mt-3 w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
          >
            📋 Copiar
          </button>
        </div>
      )}
    </div>
  );
}