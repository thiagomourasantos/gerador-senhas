import { useState, useEffect } from 'react';
import { listarHistorico } from '../services/api';

export default function PasswordHistory({ refreshKey }) {
  const [senhas, setSenhas] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const carregarHistorico = async () => {
      setLoading(true);
      try {
        const data = await listarHistorico('token-mock');
        setSenhas(data.senhas || []);
      } catch (error) {
        console.error('Erro:', error);
      } finally {
        setLoading(false);
      }
    };
    carregarHistorico();
  }, [refreshKey]);

  if (loading) return <div className="text-center">⏳ Carregando...</div>;

  return (
    <div className="bg-white rounded-lg shadow-lg p-8">
      <h2 className="text-2xl font-bold mb-6">📜 Histórico</h2>
      
      {senhas.length === 0 ? (
        <p className="text-gray-600">Nenhuma senha gerada ainda</p>
      ) : (
        <div className="space-y-3 max-h-96 overflow-y-auto">
          {senhas.map((item, idx) => (
            <div key={idx} className="bg-gray-50 p-3 rounded border border-gray-200">
              <p className="font-mono text-sm break-all">{item.password_text}</p>
              <p className="text-xs text-gray-500 mt-1">
                {item.password_type === 'random' ? '🔐 Aleatória' : '🎲 Passphrase'} 
                {item.length ? ` • ${item.length} caracteres` : ''}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}