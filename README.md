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

## Fluxo do Git

### ATENÇÃO: Não dê commit na branch main ou na dev em hipótese alguma.

Nós vamos utilizar uma coisa chamada Git Flow para organizar nosso projeto sem ter dor de cabeça.

<img src="https://wac-cdn.atlassian.com/dam/jcr:34c86360-8dea-4be4-92f7-6597d4d5bfae/02%20Feature%20branches.svg?cdnVersion=1998" width="1000">

Perceba que para criarmos as features do nosso jogo, precisamos sempre criar uma branch diretamente da dev, para depois mergearmos. 

Se não fizermos isso, podem acontecer conflitos que vão ter que ser resolvidos na mão.

Portando, quando for codar, siga os seguintes passos:

Na raiz da pasta do jogo, escreva no terminal:

```
git checkout dev #Trocando pra branch dev

git pull origin dev #Verificando se existem alterações no repositório do GitHub

git branch "feature/nome_da_feature" #Criando nova branch, diretamente da dev

git checkout feature/nome_da_feature #Trocando pra nova branch
```

Se você criar uma nova branch com base na dev e fizer alterações lá sem a dev estar atualizada, vai dar pau.

Após codar:

```
git add . #Fazendo o git adicionar os novos arquivos que serão mudados

git commit -m "feat/nome_da_feature: escreva aqui uma mensagem curta explicando o que foi feito, ex: added new weapon"

git push origin feat/nome_da_feature
```

Se você não se sente confortável de interagir com o terminal, pode tentar fazer tudo aqui pelo GitHub. Mas certifique-se que está fazendo a branch diretamente da dev.

Vamos sempre tentar fazer os merges juntos, para se der conflito, poder resolver.

Agora você está pronto para interagir com o projeto.
