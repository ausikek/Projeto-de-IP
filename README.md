# Projeto-de-IP

Projeto de Introdução à Programação 2024.1

## Como baixar o código do GitHub

Você pode fazer da seguinte forma:

### 1. Baixar o código em formato .zip

Vá ao botão verde "<> Code" e clique no botão "Download ZIP"

### 2. Clonar o repositório

Certifique-se que possui o git instalado. Então, no seu terminal preferido, insira:

```
git clone https://github.com/ausikek/Projeto-de-IP.git
```

## Como começar a interagir com o projeto

## Criando um Virtual Enviroment

Após clonar o repositório, entre na raiz do mesmo e insira os seguintes comandos no terminal:

### No Linux

```
python3 -m venv venv
```

### No Windows

```
python -m venv venv
```

Isso irá criar um Virtual Enviroment. O venv serve para que você não precise baixar os módulos externos
globalmente. Isto é, os módulos que o PIP vai baixar só estarão disponíveis quando você estiver dentro da venv.

## Iniciando o venv

### No Linux

No diretório raiz, execute:

```
source venv/bin/activate
```

### No Windows:

No diretório raiz, execute:

```
.\venv\Scripts\Activate
```

## Instalando as dependências

Certifique-se de ter o PIP instalado. Na raiz, rode o seguinte comando:

```
pip install -r requirements.txt
```

Agora você está pronto para interagir com o projeto.