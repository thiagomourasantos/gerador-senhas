# Gerador de Senhas Seguras

![CI Build](https://github.com/thiagomourasantos/gerador-senhas/actions/workflows/ci.yml/badge.svg)

### O Problema
Muitas pessoas, especialmente idosos ou usuários leigos, têm o hábito de utilizar senhas fracas, curtas ou previsíveis, devido à dificuldade de inventar e memorizar códigos complexos. Isso as torna alvos fáceis para ataques cibernéticos, fraudes e roubo de dados.

### A Proposta de Solução
Uma ferramenta rápida e de fácil uso que gera senhas fortes de forma automatizada e imprevisível. Em vez de depender do usuário para "pensar" em uma senha, o sistema faz o trabalho pesado utilizando padrões criptográficos seguros e conexões confiáveis com APIs públicas.

### Público-Alvo
Pessoas idosas, usuários leigos de tecnologia ou qualquer pessoa que precise criar uma senha forte rapidamente para proteger suas contas online.

### Funcionalidades Principais

* **Geração por Tamanho:** Cria senhas contendo letras (maiúsculas e minúsculas), números e símbolos com tamanho personalizado.
* **Geração de Passphrase (API Pública):** Consome uma API externa para gerar senhas baseadas em palavras aleatórias separadas por hífens, tornando-as seguras e muito mais fáceis de memorizar.
* **Mecanismo de Fallback:** Caso o usuário esteja sem internet, o sistema gera uma passphrase segura localmente sem interromper a execução.
* **Validação de Entradas:** Bloqueio contra tamanhos inválidos (negativos ou zero).
* **Segurança Avançada:** Uso da biblioteca nativa `secrets` para garantir geração criptograficamente segura.

### Tecnologias Utilizadas

* **Linguagem:** Python
* **Testes Automatizados & Integração:** `pytest` e `unittest.mock` (para simulação/mock da API)
* **Análise Estática (Linting):** `flake8`
* **Integração Contínua (CI):** GitHub Actions

---

## Como Executar o Projeto

### Pré-requisitos
Ter o Python 3 instalado em sua máquina.

### 1. Clonar o repositório
```bash
git clone [https://github.com/thiagomourasantos/gerador-senhas.git](https://github.com/thiagomourasantos/gerador-senhas.git)
