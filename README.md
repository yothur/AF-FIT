# API Backend do Sistema de Academia AF-FIT

A aplicação permite que o responsável consiga cadastrar os alunos e consiga fazer o gerenciamento de seus planos para um melhor controle.

## Conteúdos

- [Tecnologias e Dependências](#tecnologias-e-dependências)
- [Ambientes de execução](#ambientes-de-execução)
- [Inicializando a API localmente](#inicializando-a-api-localmente)

## Tecnologias e Dependências

A aplicação foi construída com **Python 3** utilizando o framework **Flask**, com as seguintes dependências principais:

- [**Flask**](https://flask.palletsprojects.com/en/stable/) – Framework web moderno e de alta performance
- [**SQLAlchemy**](https://www.sqlalchemy.org/) – ORM para integração com banco de dados
- [**python-dotenv**](https://pypi.org/project/python-dotenv/) – Gerenciamento de variáveis de ambiente

## Ambientes de execução

Atualmente o projeto utiliza **POSTGRESQL**.

## Inicializando a API localmente

> [!WARNING]
> Todas as variáveis sensíveis devem ser definidas no arquivo `.env` localizado na raiz do projeto.
> (exemplo [.env.template](.env.template) fornecido no repositório)

Siga os passos abaixo para configurar o ambiente de desenvolvimento local da aplicação:

1. Criar ambiente virtual

    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/Mac:
    source .venv/bin/activate
    ```

2. Instalação das dependências

    ```bash
    pip install -r requirements.txt
    ```

3. Configuração do arquivo de ambiente

   Edite o arquivo `.env` utilizando como base o arquivo `.env.template` e preencha os valores necessários.

4. Executar a API localmente

   Executável presente no arquivo `main.py`
