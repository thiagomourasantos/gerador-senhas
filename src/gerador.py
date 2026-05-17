import secrets
import string
import requests


def gerar_senha(tamanho: int) -> str:
    """Gera uma senha segura com letras, números e símbolos"""
    if tamanho <= 0:
        raise ValueError("O tamanho da senha deve ser maior que zero")

    # Junta letras maiúsculas/minúsculas, números e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Sorteia os caracteres
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha


def gerar_passphrase_da_api() -> str:
    """Busca 3 palavras aleatórias de uma API pública para gerar uma senha"""
    url = "https://random-word-api.herokuapp.com/word?number=3"
    
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            palavras = resposta.json()
            # Junta as palavras com um hífen
            return "-".join(palavras)
        else:
            return "erro-na-api-tente-novamente"
    except requests.exceptions.RequestException:
        sufixo_seguro = "".join(secrets.choice(string.ascii_lowercase) for _ in range(10))
        return "sem-conexao-" + sufixo_seguro


def main():
    print("=== Gerador de Senhas Seguras ===")
    print("Proteja-se online criando senhas fortes!\n")
    print("1. Gerar senha por tamanho (letras, números, símbolos)")
    print("2. Gerar Passphrase (palavras aleatórias via API externa)")
    
    escolha = input("\nEscolha uma opção (1 ou 2): ")

    if escolha == '1':
        try:
            entrada = input("Digite o tamanho da senha desejada (ex: 12): ")
            tamanho = int(entrada)

            senha_segura = gerar_senha(tamanho)
            print(f"\nSua nova senha é: {senha_segura}")

        except ValueError:
            msg = "Erro: insira um número inteiro válido e maior que zero."
            print(f"\n{msg}")
            
    elif escolha == '2':
        print("\nA gerar a sua nova senha segura...")
        senha = gerar_passphrase_da_api()
        print(f"Sua passphrase é: {senha}")
        
    else:
        print("\nOpção inválida. Por favor, escolha 1 ou 2.")


if __name__ == "__main__":
    main()