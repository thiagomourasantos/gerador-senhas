import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_gerar_senha_endpoint():
    """Testa endpoint GET /gerar-senha"""
    response = client.post("/api/gerar-senha", json={"tamanho": 12})
    assert response.status_code == 200
    assert "senha" in response.json()
    assert len(response.json()["senha"]) == 12

def test_gerar_passphrase_endpoint():
    """Testa endpoint /gerar-passphrase"""
    response = client.post("/api/gerar-passphrase")
    assert response.status_code == 200
    assert "senha" in response.json()

def test_historico_endpoint():
    """Testa endpoint /historico"""
    response = client.get("/api/historico")
    assert response.status_code == 200
    assert "senhas" in response.json()

def test_gerar_senha_tamanho_invalido():
    """Testa validação de tamanho"""
    response = client.post("/api/gerar-senha", json={"tamanho": -5})
    assert response.status_code == 400