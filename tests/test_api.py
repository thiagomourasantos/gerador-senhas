import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from main import app
from src.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

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


# =====================================================================
# TESTES DE AUTENTICAÇÃO
# =====================================================================

def test_hash_e_verificacao_de_senha():
    """Testa se a senha está sendo criptografada corretamente"""
    senha_pura = "minha_senha_123"
    senha_criptografada = hash_password(senha_pura)

    assert senha_criptografada != senha_pura
    assert verify_password(senha_pura, senha_criptografada) is True
    assert verify_password("senha_errada", senha_criptografada) is False


def test_criacao_do_token_jwt():
    """Testa se o token de acesso está gerando uma string válida"""
    token = create_access_token(user_id="12345", email="thiago@example.com")
    assert token is not None
    assert isinstance(token, str)


@pytest.mark.asyncio
async def test_get_current_user_valido():
    """Testa se consegue extrair o user_id com um token válido"""
    token_valido = create_access_token(
        user_id="thiago_id", email="thiago@example.com"
    )
    credenciais = HTTPAuthorizationCredentials(
        scheme="Bearer", credentials=token_valido
    )

    user_id = await get_current_user(credentials=credenciais)
    assert user_id == "thiago_id"


@pytest.mark.asyncio
async def test_get_current_user_invalido():
    """Testa se dá erro 401 ao passar um token totalmente quebrado"""
    credenciais_ruins = HTTPAuthorizationCredentials(
        scheme="Bearer", credentials="token_completamente_errado"
    )

    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(credentials=credenciais_ruins)

    assert exc_info.value.status_code == 401
