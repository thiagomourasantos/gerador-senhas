# Gerador de Senhas Seguras

![CI Build](https://github.com/thiagomourasantos/gerador-senhas/actions/workflows/ci.yml/badge.svg)

### O Problema:
Muitas pessoas, especialmente idosos ou usuários leigos, têm o hábito de utilizar senhas fracas, curtas ou previsíveis, devido à dificuldade de inventar e memorizar códigos complexos. Isso as torna alvos fáceis para ataques cibernéticos, fraudes e roubo de dados

### A Proposta de Solução
Uma ferramenta rápida e de fácil uso que gera senhas fortes de forma automatizada e imprevisível. Em vez de depender do usuário para "pensar" em uma senha, o sistema faz o trabalho pesado utilizando padrões criptográficos seguros

### Público-Alvo
Pessoas idosas, usuários leigos de tecnologia ou qualquer pessoa que precise criar uma senha forte rapidamente para proteger suas contas online

## Funcionalidades Principais
 Geração de senhas contendo letras (maiúsculas e minúsculas), números e símbolos
 Escolha personalizada do tamanho da senha
 Validação contra entradas inválidas (tamanhos negativos)
 Uso da biblioteca `secrets` para geração das senhas

## Tecnologias Utilizadas
Linguagem: Python
Testes Automatizados: `pytest`
Análise Estática (Linting): `flake8`
Integração Contínua (CI): GitHub Actions

## Como Executar o Projeto

### Pré-requisitos
Ter o Python 3 instalado em sua máquina

# 1. Clonar o repositório e Instalar
git clone https://github.com/thiagomourasantos/gerador-senhas.git

# 2. cole o codigo abaixo para entrar na pasta do projeto
cd gerador-senhas

# 3.Instale as dependencias
pip install -r requirements.txt