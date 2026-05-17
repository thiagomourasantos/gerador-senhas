from unittest.mock import MagicMock
import pytest
from src.gerador import gerar_senha, gerar_passphrase_da_api


def test_gerar_senha_tamanho_correto():
    """Testa se a senha gerada tem exatamente o tamanho solicitado"""
    senha = gerar_senha(12)
    assert len(senha) == 12
    assert isinstance(senha, str)


def test_gerar_senha_tamanho_invalido():
    """Testa bloqueio de senhas com tamanho zero ou negativo"""
    msg = "O tamanho da senha deve ser maior que zero"
    with pytest.raises(ValueError, match=msg):
        gerar_senha(0)

    with pytest.raises(ValueError):
        gerar_senha(-5)


def test_gerar_senha_tamanho_minimo():
    """Testa o menor tamanho possível para uma senha"""
    senha = gerar_senha(1)
    assert len(senha) == 1


def test_gerar_passphrase_com_sucesso(monkeypatch):
    """Testa se a aplicação processa o retorno de sucesso da API"""
    mock_resposta = MagicMock()
    mock_resposta.status_code = 200
    mock_resposta.json.return_value = ["seguranca", "nuvem", "python"]

    monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_resposta)

    resultado = gerar_passphrase_da_api()
    assert resultado == "seguranca-nuvem-python"


def test_gerar_passphrase_com_falha_da_api(monkeypatch):
    """Testa o fallback seguro quando a API retorna erro (ex: 500)"""
    mock_resposta = MagicMock()
    mock_resposta.status_code = 500

    monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_resposta)

    resultado = gerar_passphrase_da_api()
    assert resultado == "erro-na-api-tente-novamente"
