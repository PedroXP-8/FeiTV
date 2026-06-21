FEI TV

Sistema de streaming em terminal desenvolvido em Python, permitindo cadastro e login de usuários,
navegação por vídeos, pesquisa de conteúdo e gerenciamento de listas de favoritos.

Sobre o Projeto

O FEI TV é uma aplicação de linha de comando que simula uma plataforma de vídeos. Os usuários podem criar contas, 
acessar conteúdos cadastrados, pesquisar vídeos e organizar listas de favoritos personalizadas.
O projeto foi desenvolvido com foco em modularização, manipulação de arquivos JSON e organização de código em múltiplos módulos Python.


Funcionalidades:

Controle de Acesso:
- Cadastro de usuários
- Login de usuários
- Validação de credenciais
- Controle de sessão do usuário logado

Catálogo de Vídeos:
- Exibição de vídeos disponíveis
- Visualização de informações dos vídeos
- Registro de visualizações

Pesquisa:
- Busca de vídeos por título
- Exibição dos resultados encontrados

Favoritos:
- Criação de listas de favoritos
- Edição de listas existentes
- Exclusão de listas
- Adição e remoção de vídeos
- Visualização de listas salvas

Estrutura do Projeto:
```text
FeiTV/
├── controle_acesso/
│   ├── controle_cadastro.py
│   └── controle_login.py
│
├── dados/
│   ├── usuarios.txt
│   ├── videos.json
│   └── favoritos.json
│
├── globals/
│   └── session.py
│
├── load_favoritos/
│   └── favoritos.py
│
├── load_videos/
│   └── videos.py
│
├── menus/
│   ├── primeiros_menus.py
│   ├── menu_usuario.py
│   ├── menu_busca.py
│   ├── menu_lista_favoritos.py
│   ├── menu_controle_favoritos.py
│   └── menus_video.py
│
└── main.py
```
Como Executar:

Pré-requisitos
- Python 3.10 ou superior

Clone o repositório:
- git clone https://github.com/SEU-USUARIO/FeiTV.git

Acesse a pasta do projeto:
- cd FeiTV
  
Execute o programa:
- python main.py


Armazenamento de Dados:

| Arquivo | Função |
|----------|----------|
| usuarios.txt | Armazena os usuários cadastrados |
| videos.json | Catálogo de vídeos |
| favoritos.json | Listas de favoritos dos usuários |

Tecnologias Utilizadas:

- Python
- JSON
- Programação Modular
- Manipulação de Arquivos
- Interface via Terminal


Este projeto foi desenvolvido para praticar:

- Estruturação de projetos Python
- Modularização de código
- Persistência de dados
- Manipulação de arquivos JSON
- Fluxos de autenticação
- Menus interativos em terminal

Autores:

Projeto desenvolvido pelos alunos da FEI como atividade acadêmica.
