 <div align="center">

# 🎓 EduCore

### Sistema de Gerenciamento Acadêmico em Python

**Uma aplicação de terminal para gerenciamento de alunos, turmas, notas e usuários, com persistência de dados em PostgreSQL.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-openSUSE-73BA25?style=for-the-badge&logo=opensuse&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-orange?style=for-the-badge)
![Version](https://img.shields.io/badge/Versão-1.0-blue?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

O **EduCore** é um sistema de gerenciamento acadêmico desenvolvido em Python, com interface de linha de comando (CLI) e integração com PostgreSQL.

O projeto é uma reconstrução completa do antigo **Student Manager**, um dos meus primeiros projetos de programação.

O objetivo desta nova versão é aplicar conceitos mais avançados de desenvolvimento, como modularização, programação orientada a objetos, manipulação de bancos de dados relacionais, validação de informações e autenticação de usuários.

O sistema foi pensado para centralizar operações acadêmicas e permitir o gerenciamento de estudantes de maneira organizada.

## ⚙️ Funcionalidades

### 🔐 Gerenciamento de usuários

- Cadastro de usuários.
- Login com validação no PostgreSQL.
- Verificação de usuários existentes.
- Controle de situação do usuário (ativo/inativo).
- Acesso ao menu principal após autenticação.

**Status:** implementação inicial desenvolvida, com melhorias de segurança pendentes.

### 👨‍🎓 Gerenciamento de alunos

- Cadastrar novos alunos.
- Consultar alunos cadastrados.
- Editar nome e turma.
- Desativar alunos sem excluir o registro do banco.
- Verificar a existência de alunos.
- Associar alunos a turmas.

**Status:** funções iniciais desenvolvidas, em fase de testes e aprimoramento.

### 🏫 Gerenciamento de turmas

- Cadastrar turmas.
- Consultar turmas existentes.
- Editar informações.
- Gerenciar vínculos com alunos.

**Status:** estrutura planejada para a versão 1.0.

### 📝 Gerenciamento de notas

- Registrar notas entre 0 e 10.
- Associar notas aos registros acadêmicos dos alunos.
- Consultar notas.
- Editar e remover registros.
- Calcular médias.

**Status:** cadastro de notas em desenvolvimento; demais operações planejadas.

### 📊 Estatísticas gerais

- Quantidade de alunos cadastrados.
- Quantidade de alunos ativos e inativos.
- Distribuição de alunos por turma.
- Médias acadêmicas.
- Relatórios gerais do sistema.

**Status:** planejado.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3 | Desenvolvimento do sistema |
| PostgreSQL | Armazenamento dos dados |
| Psycopg 3 | Comunicação entre Python e PostgreSQL |
| python-dotenv | Gerenciamento das variáveis de ambiente |
| SQL | Consultas, inserções e atualizações |
| Git e GitHub | Versionamento e gerenciamento do código |
| Linux / openSUSE | Ambiente de desenvolvimento |

---

## 🏗️ Arquitetura do projeto

O EduCore utiliza uma estrutura modular, com separação das responsabilidades de cada componente.

Estrutura principal e organização prevista:

```text
EduCore/
│
├── main.py
│
├── login/
│   ├── __init__.py
│   ├── user.py
│   └── cadastro.py
│
├── menu/
│   ├── __init__.py
│   └── menu.py
│
├── alunos/
│   ├── menu.py
│   ├── cadastro.py
│   ├── visualizar.py
│   ├── editar.py
│   └── remover.py
│
├── notas/
│   └── ...
│
├── turmas/
│   └── ...
│
├── database/
│   ├── __init__.py
│   └── conector.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

*A estrutura poderá ser ajustada conforme o desenvolvimento. Os diretórios de notas e turmas representam módulos previstos.*

### Organização

- **main.py:** ponto de entrada do sistema.
- **login/:** cadastro e autenticação dos usuários.
- **menu/:** navegação pelo menu principal.
- **alunos/:** operações relacionadas ao cadastro e gerenciamento de estudantes.
- **notas/:** funcionalidades de avaliação acadêmica.
- **turmas/:** gerenciamento das turmas.
- **database/:** configuração e conexão com PostgreSQL.

---

## 🗄️ Banco de dados

O EduCore utiliza PostgreSQL como sistema gerenciador de banco de dados relacional.

O modelo acadêmico foi planejado com cinco tabelas principais:

| Tabela | Responsabilidade |
|---|---|
| usuarios | Armazenar usuários e informações de acesso |
| alunos | Armazenar dados dos estudantes |
| turmas | Organizar turmas acadêmicas |
| matriculas | Relacionar alunos e turmas |
| notas | Armazenar avaliações e notas |

O sistema utiliza comandos SQL como `SELECT`, `INSERT`, `UPDATE` e consultas parametrizadas por meio do Psycopg.

A modelagem e os relacionamentos ainda poderão passar por ajustes durante a implementação da versão 1.0.

---

## 💻 Prévia da aplicação

### Menu principal

```text
========================================
          EDUCORE | MENU PRINCIPAL
========================================
 [1] Gerenciamento de Alunos
 [2] Gerenciamento de Notas
 [3] Gerenciamento de Turmas
 [4] Estatísticas Gerais
 [5] Sair
========================================

Escolha uma opção:
```

### Gerenciamento de alunos

```text
========================================
           EDUCORE | ALUNOS
========================================
 [1] Cadastrar aluno
 [2] Visualizar alunos
 [3] Editar aluno
 [4] Remover aluno
 [5] Voltar ao menu principal
========================================
```

### Cadastro de aluno

```text
========================================
       EDUCORE | CADASTRO DE ALUNO
========================================

 > Nome do aluno: João Silva
 > Turma do aluno: 3

----------------------------------------
      ALUNO CADASTRADO COM SUCESSO!
----------------------------------------
```

*Exemplos ilustrativos da interface CLI.*

---

## 🚀 Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/Mutus142/EduCore.git
cd EduCore
```

### 2. Criar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
python -m pip install "psycopg[binary]" python-dotenv
```

### 4. Configurar o PostgreSQL

Crie um banco de dados PostgreSQL para o projeto e configure as tabelas necessárias, conforme a estrutura utilizada na versão em desenvolvimento.

Na raiz do projeto, crie o arquivo `.env`:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=educore
DB_USER=postgres
DB_PASSWORD=sua_senha
```

Os nomes das variáveis devem corresponder aos utilizados em `database/conector.py`.

**Importante:** nunca publique o arquivo `.env`, credenciais de acesso ou senhas reais no GitHub.

### 5. Iniciar o sistema

```bash
python main.py
```

O menu inicial será apresentado no terminal.

*Nota: enquanto o projeto estiver em desenvolvimento, alguns módulos e etapas de configuração poderão ainda não estar disponíveis.*

---

## 📈 Roadmap — EduCore 1.0

- [x] Criar o repositório e iniciar o projeto.
- [x] Configurar conexão Python com PostgreSQL.
- [x] Desenvolver estrutura inicial de login e cadastro.
- [x] Desenvolver estrutura inicial do CRUD de alunos.
- [x] Padronizar a interface CLI.
- [ ] Finalizar validação e segurança da autenticação.
- [ ] Concluir e testar o gerenciamento de alunos.
- [ ] Implementar gerenciamento de turmas.
- [ ] Finalizar gerenciamento de notas.
- [ ] Implementar estatísticas acadêmicas.
- [ ] Revisar a modelagem do banco de dados.
- [ ] Realizar testes e corrigir problemas.
- [ ] Publicar a versão estável 1.0.0.

---

## 🔮 Próximas versões

Após a conclusão da versão 1.0, o projeto poderá evoluir com:

- Interface gráfica.
- Sistema de permissões por perfil.
- Relatórios acadêmicos avançados.
- Exportação de boletins.
- Histórico de alterações.
- Melhorias de arquitetura e testes automatizados.

---

## 👨‍💻 Desenvolvedor

**Mateus Ribeiro Simão**

Desenvolvedor em formação, com interesse em desenvolvimento de software, banco de dados e cibersegurança.

O EduCore faz parte do meu portfólio pessoal e representa a evolução dos meus conhecimentos em Python e SQL.

**GitHub:** [@Mutus142](https://github.com/Mutus142)

**Repositório:** [EduCore](https://github.com/Mutus142/EduCore)

---

<div align="center">

**EduCore 1.0 — Em desenvolvimento**

*Do Student Manager a uma nova arquitetura de gerenciamento acadêmico.*

</div>