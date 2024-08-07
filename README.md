
<p align="center">
  <img src="https://github.com/user-attachments/assets/3abb0350-5112-4688-b9fe-f92b3ab7b2f2" width="570" height="570">
</p>

Peritech é um calouro do curso de Ciência da Computação do período de 2024.1 do CIn UFPE. Durante um fatídico dia, em que estudava operações matemáticas em Python no GRAD5, Peritech efetuou uma divisão por zero, que por meio de mecanismos físicos ainda desconhecidos, gerou um Buraco Negro que começou a consumir o CIn de dentro pra fora. 

## Capturas de Tela
<div style="display: flex">
  <p>
      <img src="https://github.com/user-attachments/assets/a71c2905-6650-45a3-8273-4a6df6963751" width="570" height="570">
      <img src="https://github.com/user-attachments/assets/ac9d598b-83ed-48a3-9a5e-89a4751ed0f8" width="570" height="570">
      <img src="https://github.com/user-attachments/assets/f0da958f-1f87-4ce7-bf8b-d6f7f5015996" width="570" height="570">
      <img src="https://github.com/user-attachments/assets/242cfef3-2dff-47c4-91f9-c0c92ff745c5" width="570" height="570">
</p>
</div>

## Membros: 
* Breno Filho (bonof)
* Bernardo Siqueira (bsb)
* Danilo Barrote (drb)
* João Pedro (jpgp)
* Toni Amorim (tca)
* Vitor Buarque (vbgm)

## Divisão de tarefas:
| **Equipe** | **Cargo** | **Tarefas** |
| :---: | :--: |:--:|
| bonof | Project Lead | Refatoraçao do Código e Repositório Git |
| bsb | Art Director | Sprites/áudio |
| drb | Art Director | Design gráfico + Sprites |
| jpgp | Quality Assurance | Identificação e correção de bugs |
| tca | Lead Developer | Código principal do jogo e protótipo/classes |
| vbgm | Main Developer + Art Director | Classes + Sprites |

## Ferramentas, Frameworks e bibliotecas: 
* Pygame
> Pygame é uma biblioteca de desenvolvimento de jogos em Python que facilita a criação de jogos e aplicações multimídia. Ela fornece módulos para gráficos, som, entrada do usuário e manipulação de imagens, permitindo que desenvolvedores construam jogos de forma mais rápida e eficiente.
* Os
> O módulo `os` em Python fornece uma maneira de interagir com o sistema operacional. Ele inclui funcionalidades para manipulação de arquivos e diretórios, gerenciamento de processos, e acesso a variáveis de ambiente. Isso permite que scripts Python realizem tarefas como criação e remoção de arquivos, navegação em diretórios e execução de comandos do sistema.
* Math
> O módulo `math` em Python oferece funções matemáticas básicas e avançadas. Ele inclui operações como trigonometria, logaritmos, fatoriais, e constantes matemáticas (como π e e). Esse módulo é útil para cálculos matemáticos precisos e eficientes em uma ampla gama de aplicações científicas e de engenharia.

## Organização do código
O código é modularizado e dividido em branches diferentes. Utilizamos a branch `main` para as versões finais do nosso código e a branch `dev` para criar as novas features. 
Além disso, dividimos o código com arquivos diferentes para cada tipo de funcionalidade, como loop principal, configurações, entre outros.
O jogo é executado através de `main.py`.
./ 
├── src/ 
│   ├── config.py 
│   ├── graficos.py 
│   ├── jogo.py 
│   ├── objetos.py 
│   └── utils.py 
├── assets/ 
├── main.py 
├── tela_final.py 
└── tela_inicial.py 
Hierarquia e Objetos Principais 

`main.py`: Ponto de entrada do jogo
Objeto principal: `GameLoop`


`tela_inicial.py`: Gerencia a tela inicial e a tela de história
Objetos: `TelaInicial`, `TelaHistoria`


`tela_final.py`: Gerencia a tela final do jogo
Objeto: `TelaFinal`


`src/jogo.py`: Contém a lógica principal do jogo
Classe principal: `GameLoop`


`src/objetos.py`: Define os objetos do jogo
Classes: `Notification`, `Player`, `Food`


`src/graficos.py`: Gerencia a renderização gráfica
Classe principal: `Graficos`


`src/config.py`: Armazena configurações globais do jogo
`src/utils.py`: Contém funções utilitárias

## Análise individual dos arquivos
## `src/graficos.py` - Gerencia a renderização gráfica do jogo.
Classe principal: `Graficos`

Métodos:

`__init__()`: Inicializa texturas
`setup()`: Configura a tela
`update()`: Atualiza offsets
`textura()`: Renderiza texturas
`circle()`: Desenha círculos
`quadrado()`: Desenha quadrados



## `src/jogo.py` - Contém a lógica principal do jogo.
Classe principal: `GameLoop`

Métodos:

`__init__()`: Inicializa o jogo
`desenhar_tiles()`: Desenha o grid de fundo
`run()`: Loop principal do jogo

Funcionalidades:

Gerencia o movimento do jogador
Spawna e gerencia objetos (comida)
Controla colisões e crescimento do jogador
Implementa sistema de estágios e temporizador



## `src/objetos.py` - Define os objetos principais do jogo.
Classes:

`Notification`: Gerencia notificações na tela
`Player`: Representa o jogador (buraco negro)
`Food`: Representa os objetos que o jogador pode absorver

## `src/utils.py` - Contém funções utilitárias.
Funções:

limpar(): Limpa a tela do console
displaysegundos(): Formata segundos para exibição

## Loops Principais

Loop em main.py:
- Inicializa o jogo e chama GameLoop.run()

Loop principal do jogo:
- Gerencia eventos, atualiza posições, renderiza objetos
- Controla a lógica de progressão do jogo (estágios, temporizador)

Loops em tela_inicial.py e tela_final.py: 
- Gerenciam as telas de início e fim do jogo

## Conceitos:
* Programação Orientada a Objetos
> A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o software em torno de "objetos", que são instâncias de "classes". Cada objeto pode conter dados (atributos) e comportamentos (métodos). POO facilita a modularidade, reutilização de código e manutenção, promovendo conceitos como encapsulamento, herança e polimorfismo.
* Laços de Repetição
> Laços de repetição são estruturas de controle de fluxo que permitem a execução repetida de um bloco de código. Em Python, os principais laços de repetição são `for` e `while`. O `for` é usado para iterar sobre uma sequência (como uma lista ou string), enquanto o `while` continua a execução enquanto uma condição específica é verdadeira. Eles são essenciais para automatizar tarefas repetitivas e processar conjuntos de dados de forma eficiente.
* Estruturas Condicionais
> Estruturas condicionais permitem a execução de blocos de código baseados em condições específicas. Em Python, as principais estruturas condicionais são `if`, `elif` e `else`. Elas permitem que o programa tome decisões e execute diferentes blocos de código dependendo do valor de expressões booleanas (verdadeiro ou falso). Essas estruturas são fundamentais para controlar o fluxo de um programa e implementar lógica de tomada de decisão.
* Funções
> Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Em Python, uma função é definida usando a palavra-chave `def`, seguida pelo nome da função, parênteses e um bloco de código indentado. Funções podem aceitar argumentos, retornar valores e ajudar a tornar o código mais modular e organizado. Elas são essenciais para evitar a repetição de código e facilitar a manutenção e compreensão de programas.

## Desafios:
* Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
> Pensar em um projeto muito complexo para um curto espaço de tempo. Decidimos nos reposicionar e apenas programar funcionalidades e um mapa mais centrais.
* Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
> Certamente foi a utilização do git como ferramenta de versionamento e lidar com um projeto mantido por múltiplas pessoas. Lidamos com esse problema capacitando os membros com git e tentando seguir boas práticas de utilização.
* Quais as lições aprendidas durante o projeto?
> A importância de manter um código organizado e bem documentado em um projeto com múltiplos integrantes. Também percebemos a versatilidade da linguagem Python.

#
###### _Projeto referente a cadeira de Programação 1/CIN-UFPE no período 2024.1._
