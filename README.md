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

O **EduCore** é um sistema de gerenciamento acadêmico desenvolvido em Python, com interface de linha de comando (CLI) e persistência de dados em PostgreSQL.

O projeto surgiu como uma reconstrução completa do antigo [Student Manager](https://github.com/Mutus142/Student-Manager), um dos meus primeiros projetos de programação.

Nesta nova versão, o objetivo é desenvolver uma aplicação mais organizada, modular e funcional, utilizando conhecimentos adquiridos em Python, SQL, bancos de dados relacionais e desenvolvimento de sistemas.

O EduCore permite realizar operações de cadastro, consulta, edição e gerenciamento de informações acadêmicas, mantendo os dados armazenados em um banco PostgreSQL.

O desenvolvimento também tem como objetivo aprofundar conhecimentos em validação de dados, tratamento de exceções, integração entre módulos e organização de código.

---

## ⚙️ Funcionalidades

### 🔐 Gerenciamento de usuários

O módulo de autenticação controla o acesso às funcionalidades do sistema.

**Funcionalidades implementadas:**

- Cadastro de usuários no PostgreSQL.
- Login com nome de usuário e senha.
- Verificação de usuários existentes.
- Validação da situação do usuário (ativo/inativo).
- Tratamento de credenciais incorretas.
- Redirecionamento para cadastro.
- Acesso ao menu principal após autenticação.

**Status:** funcionalidade implementada em versão inicial, com melhorias de segurança pendentes.

### 👨‍🎓 Gerenciamento de alunos

Módulo responsável pelas operações de cadastro e manutenção dos estudantes.

**Funcionalidades implementadas:**

- Cadastro de alunos.
- Verificação de alunos já existentes.
- Consulta de alunos pelo nome.
- Visualização da turma do estudante.
- Edição de nome.
- Alteração de turma.
- Desativação lógica de alunos.
- Validação de entradas.
- Integração com PostgreSQL.

A remoção utiliza uma abordagem de **exclusão lógica (soft delete)**, alterando a situação do aluno para inativo sem excluir permanentemente seu registro.

**Status:** CRUD inicial implementado, em fase de testes e aprimoramento.

### 🏫 Gerenciamento de turmas

Módulo responsável pela organização das turmas acadêmicas.

**Funcionalidades implementadas:**

- Cadastro de novas turmas.
- Verificação de turmas duplicadas.
- Definição do turno (manhã ou tarde).
- Edição do número da turma.
- Alteração do turno.
- Remoção de turmas mediante confirmação.
- Validação de números e opções.

As turmas são identificadas por valores numéricos inteiros.

**Status:** operações principais implementadas, com testes de integração pendentes.

### 📝 Gerenciamento de notas

Módulo destinado ao registro e acompanhamento do desempenho dos alunos.

**Funcionalidades implementadas:**

- Cadastro de notas entre 0 e 10.
- Associação de notas aos alunos através de `id_aluno`.
- Registro de descrição da avaliação.
- Consulta de notas por aluno.
- Edição de notas existentes.
- Validação de valores.
- Utilização de `INNER JOIN` para consultas relacionais.

O sistema permite registrar múltiplas avaliações para um mesmo estudante.

**Status:** cadastro, edição e consulta desenvolvidos, em processo de validação e testes.

### 📊 Estatísticas gerais

Funcionalidade planejada para apresentar indicadores acadêmicos utilizando consultas SQL.

**Funcionalidades previstas:**

- Total de alunos cadastrados.
- Quantidade de alunos ativos e inativos.
- Distribuição de alunos por turma.
- Quantidade de avaliações registradas.
- Média geral de notas.
- Médias individuais.
- Estatísticas de desempenho acadêmico.

**Status:** planejado para conclusão da versão 1.0.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia       | Aplicação                        |
| ---------------- | -------------------------------- |
| Python 3         | Linguagem principal              |
| PostgreSQL       | Banco de dados relacional        |
| Psycopg 3        | Integração Python e PostgreSQL   |
| python-dotenv    | Variáveis de ambiente            |
| SQL              | Consultas e manipulação de dados |
| Git              | Controle de versões              |
| GitHub           | Hospedagem do código             |
| Linux / openSUSE | Ambiente de desenvolvimento      |
| VS Code          | Editor de código                 |

### Conceitos aplicados

- Programação modular.
- Funções e estruturas de repetição.
- Tratamento de exceções.
- Validação de entradas.
- Consultas parametrizadas.
- Operações CRUD.
- Chaves primárias e estrangeiras.
- Relacionamentos entre tabelas.
- Consultas utilizando `INNER JOIN`.
- Controle de transações com PostgreSQL.

---

## 🏗️ Arquitetura do projeto

O EduCore possui uma arquitetura modular, dividindo suas funcionalidades em diferentes diretórios para facilitar manutenção e evolução.

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
│   └── [módulos de gerenciamento]
│
├── notas/
│   ├── menu.py
│   └── services.py
│
├── turmas/
│   ├── menu.py
│   └── service.py
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

*Estrutura representativa da organização atual. Os arquivos internos do módulo de alunos devem ser consultados no repositório.*

### Responsabilidade dos módulos

| Módulo      | Função                                |
| ----------- | ------------------------------------- |
| `main.py`   | Inicialização e navegação inicial     |
| `login/`    | Autenticação e cadastro de usuários   |
| `menu/`     | Menu principal do sistema             |
| `alunos/`   | Gerenciamento de estudantes           |
| `notas/`    | Cadastro, consulta e edição de notas  |
| `turmas/`   | Cadastro, edição e exclusão de turmas |
| `database/` | Conexão e comunicação com PostgreSQL  |

---

## 🗄️ Banco de dados

O EduCore utiliza PostgreSQL para armazenar as informações de forma persistente.

A arquitetura atual trabalha com quatro tabelas principais:

| Tabela     | Responsabilidade                         |
| ---------- | ---------------------------------------- |
| `usuarios` | Credenciais e situação dos usuários      |
| `alunos`   | Informações dos estudantes               |
| `turmas`   | Identificação e turno das turmas         |
| `notas`    | Notas e avaliações vinculadas aos alunos |

### Relacionamento entre alunos e notas

Cada aluno possui um identificador único (`id_aluno`).

Esse identificador é utilizado para relacionar os registros da tabela `notas` aos estudantes.

```text
ALUNOS
├── id_aluno (PK)
├── nome
├── turma
└── ativo
       │
       │ 1:N
       ▼
NOTAS
├── id_nota (PK)
├── id_aluno (FK)
├── valor
└── descricao
```

Um aluno pode possuir várias notas, mas cada nota está associada a um único aluno.

O número da turma também é armazenado no cadastro do estudante. Sua integração com a tabela `turmas` ainda poderá receber melhorias de integridade referencial.

### Exemplo de consulta SQL

```sql
SELECT
    a.nome,
    a.turma,
    n.descricao,
    n.valor
FROM alunos a
INNER JOIN notas n
    ON a.id_aluno = n.id_aluno
ORDER BY a.nome;
```

A consulta permite recuperar as avaliações dos estudantes utilizando um relacionamento entre tabelas.

---

## 💻 Interface CLI

A aplicação utiliza uma interface de terminal padronizada, com menus numerados e mensagens de retorno.

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

### Gerenciamento de notas

```text
========================================
           EDUCORE | NOTAS
========================================
 [1] Adicionar nota
 [2] Editar nota
 [3] Visualizar notas de um aluno
 [4] Voltar ao menu principal
========================================
```

### Gerenciamento de turmas

```text
========================================
           EDUCORE | TURMAS
========================================
 [1] Adicionar turma
 [2] Editar turma
 [3] Remover turma
 [4] Voltar ao menu principal
========================================
```

### Exemplo de cadastro

```text
========================================
       EDUCORE | CADASTRO DE ALUNO
========================================

 > Nome do aluno: João Silva
 > Turma do aluno: 100

----------------------------------------
      ALUNO CADASTRADO COM SUCESSO!
----------------------------------------
```

*Os exemplos representam o formato da interface utilizado no desenvolvimento.*

---

## 🚀 Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/Mutus142/EduCore.git
cd EduCore
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install "psycopg[binary]" python-dotenv
```

### 4. Configurar o PostgreSQL

Crie um banco de dados PostgreSQL e configure as tabelas utilizadas pelo sistema.

Na raiz do projeto, crie um arquivo `.env` com as informações de conexão:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=educore
DB_USER=postgres
DB_PASSWORD=sua_senha
```

As variáveis devem corresponder às configurações utilizadas em `database/conector.py`.

**Segurança:** o arquivo `.env` deve permanecer fora do controle de versão. Não publique credenciais reais.

### 5. Executar o EduCore

```bash
python main.py
```

Após a inicialização, o sistema apresentará as opções de login e cadastro.

**Observação:** a versão atual ainda está em desenvolvimento. A configuração do esquema PostgreSQL e algumas funcionalidades exigem ajustes antes de uma instalação automatizada.

---

## 📈 Roadmap — EduCore 1.0

### Estrutura inicial

- [x] Criar repositório GitHub.
- [x] Configurar ambiente Python.
- [x] Integrar PostgreSQL.
- [x] Criar estrutura modular.
- [x] Padronizar menus e mensagens.

### Usuários

- [x] Implementar cadastro inicial.
- [x] Implementar login inicial.
- [x] Validar usuários existentes.
- [ ] Implementar armazenamento seguro de senhas com Argon2.
- [ ] Finalizar validações e testes de autenticação.

### Alunos

- [x] Cadastrar alunos.
- [x] Consultar alunos.
- [x] Editar nome e turma.
- [x] Implementar desativação lógica.
- [ ] Melhorar identificação de alunos por ID.
- [ ] Concluir testes do módulo.

### Notas

- [x] Desenvolver cadastro de notas.
- [x] Desenvolver edição de notas.
- [x] Desenvolver consulta de notas.
- [ ] Finalizar testes de integração.
- [ ] Implementar cálculo de médias.
- [ ] Melhorar identificação das avaliações por ID.

### Turmas

- [x] Desenvolver cadastro de turmas.
- [x] Desenvolver edição de turmas.
- [x] Desenvolver remoção de turmas.
- [x] Validar relacionamentos com alunos.
- [x] Concluir testes do módulo.

### Finalização

- [ ] Desenvolver estatísticas gerais.
- [ ] Revisar a integridade do banco de dados.
- [ ] Melhorar tratamento de erros.
- [ ] Criar testes automatizados.
- [ ] Finalizar documentação técnica.
- [ ] Publicar release estável 1.0.0.

---

## 🔮 Próximas versões

Após a conclusão da versão 1.0, o EduCore poderá receber novas funcionalidades:

- Interface gráfica para desktop.
- Perfis e permissões de usuários.
- Relatórios acadêmicos avançados.
- Exportação de boletins.
- Histórico de alterações.
- Registro de atividades administrativas.
- Refatoração para arquitetura orientada a objetos.
- Ampliação dos testes automatizados.

---

## 👨‍💻 Desenvolvedor

**Mateus Ribeiro Simão**

Desenvolvedor em formação, com interesse em Python, bancos de dados, desenvolvimento de sistemas e cibersegurança.

O EduCore integra meu portfólio de projetos e representa a evolução dos conhecimentos adquiridos desde o desenvolvimento do Student Manager.

**GitHub:** [@Mutus142](https://github.com/Mutus142)

**Repositório:** [EduCore](https://github.com/Mutus142/EduCore)

---

\<div align="center">

**EduCore 1.0 — Em desenvolvimento**

*Uma nova evolução do Student Manager, agora com Python e PostgreSQL.*

\</div>
