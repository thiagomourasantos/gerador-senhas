import secrets
import string


def gerar_senha(tamanho: int) -> str:
    """Gera uma senha segura com letras, números e símbolos"""
    if tamanho <= 0:
        raise ValueError("O tamanho da senha deve ser maior que zero")

    # Junta letras maiúsculas/minúsculas, números e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Sorteia os caracteres
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    print("=== Gerador de Senhas Seguras ===")
    print("Proteja-se online criando senhas fortes!\n")

    try:
        entrada = input("Digite o tamanho da senha desejada (ex: 12): ")
        tamanho = int(entrada)

        senha_segura = gerar_senha(tamanho)
        print(f"\n Sua nova senha é: {senha_segura}")

    except ValueError:
        msg = " Erro: insira um número inteiro válido e maior que zero."
        print(f"\n{msg}")


if __name__ == "__main__":
    main()