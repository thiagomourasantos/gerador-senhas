from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.gerador import PasswordGenerator


router = APIRouter(prefix="/api", tags=["passwords"])


class GeraSenhaRequest(BaseModel):
    tamanho: int


class SenhaResponse(BaseModel):
    senha: str
    tipo: str


# Endpoint público (sem auth por enquanto)
@router.post("/gerar-senha", response_model=SenhaResponse)
async def gerar_senha(request: GeraSenhaRequest):
    """Gera senha aleatória"""
    try:
        user_id = "guest-user"  # Pessoa 2 vai adicionar auth real

        generator = PasswordGenerator(user_id)
        senha = generator.gerar_senha(request.tamanho)

        generator.salvar_senha(
            senha,
            "random",
            request.tamanho,
        )

        return {
            "senha": senha,
            "tipo": "random",
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/gerar-passphrase", response_model=SenhaResponse)
async def gerar_passphrase():
    """Gera passphrase"""
    user_id = "guest-user"

    generator = PasswordGenerator(user_id)
    passphrase = generator.gerar_passphrase_da_api()

    generator.salvar_senha(
        passphrase,
        "passphrase",
    )

    return {
        "senha": passphrase,
        "tipo": "passphrase",
    }


@router.get("/historico")
async def listar_historico():
    """Lista histórico (sem auth por enquanto)"""
    user_id = "guest-user"

    generator = PasswordGenerator(user_id)

    return {
        "senhas": generator.listar_senhas(),
    }