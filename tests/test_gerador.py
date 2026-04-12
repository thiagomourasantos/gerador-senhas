import pytest
from src.gerador import gerar_senha


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
