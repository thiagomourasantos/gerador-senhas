import secrets
import string
from typing import List, Optional

import requests

from src.supabase_config import get_supabase


class PasswordGenerator:
    """Gerador de senhas com BD"""

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.supabase = get_supabase()

    @staticmethod
    def gerar_senha(tamanho: int) -> str:
        """Gera senha com letras, números e símbolos"""
        if tamanho <= 0:
            raise ValueError("Tamanho deve ser > 0")

        caracteres = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        return "".join(
            secrets.choice(caracteres)
            for _ in range(tamanho)
        )

    @staticmethod
    def gerar_passphrase_da_api() -> str:
        """Busca palavras de API pública"""
        url = "https://random-word-api.herokuapp.com/word?number=3"

        try:
            resposta = requests.get(url, timeout=5)

            if resposta.status_code == 200:
                return "-".join(resposta.json())

            return "erro-na-api-tente-novamente"

        except Exception:
            sufixo = "".join(
                secrets.choice(string.ascii_lowercase)
                for _ in range(10)
            )
            return f"sem-conexao-{sufixo}"

    def salvar_senha(
        self,
        senha: str,
        tipo: str,
        tamanho: Optional[int] = None,
    ):
        """Salva no Supabase"""
        try:
            response = (
                self.supabase
                .table("generated_passwords")
                .insert(
                    {
                        "user_id": self.user_id,
                        "password_text": senha,
                        "password_type": tipo,
                        "length": tamanho,
                    }
                )
                .execute()
            )

            return response.data[0] if response.data else None

        except Exception as e:
            print(f"❌ Erro: {e}")
            return None

    def listar_senhas(
        self,
        limit: int = 10,
    ) -> List[dict]:
        """Lista senhas do usuário"""
        try:
            response = (
                self.supabase
                .table("generated_passwords")
                .select("*")
                .eq("user_id", self.user_id)
                .order("created_at", desc=True)
                .limit(limit)
                .execute()
            )

            return response.data

        except Exception as e:
            print(f"❌ Erro: {e}")
            return []
