const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
console.log(API_URL)
export async function gerarSenha(tamanho) {
  const response = await fetch(`${API_URL}/api/gerar-senha`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tamanho })
  });
  if (!response.ok) throw new Error('Erro ao gerar senha');
  return response.json();
}

export async function gerarPassphrase() {
  const response = await fetch(`${API_URL}/api/gerar-passphrase`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' }
  });
  if (!response.ok) throw new Error('Erro ao gerar passphrase');
  return response.json();
}

export async function listarHistorico(token) {
  const response = await fetch(`${API_URL}/api/historico`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!response.ok) throw new Error('Erro ao carregar histórico');
  return response.json();
}