import { useState } from 'react';
import PasswordGenerator from './components/PasswordGenerator';
import PasswordHistory from './components/PasswordHistory';

export default function App() {
  const [lastPassword, setLastPassword] = useState(null);
  const [refreshHistory, setRefreshHistory] = useState(0);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-12 text-gray-800">
          🔐 Gerador de Senhas Seguras
        </h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <PasswordGenerator 
            onPasswordGenerated={() => setRefreshHistory(r => r + 1)}
            setLastPassword={setLastPassword}
          />
          <PasswordHistory refreshKey={refreshHistory} />
        </div>
      </div>
    </div>
  );
}