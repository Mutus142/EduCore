 <div align="center">

# 🎓 EduCore

### Sistema de Gerenciamento Acadêmico em Python

**Uma aplicação de terminal para gerenciamento de alunos, turmas, notas, usuários e estatísticas, com persistência de dados em PostgreSQL.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-openSUSE-73BA25?style=for-the-badge&logo=opensuse&logoColor=white)
![Status](https://img.shields.io/badge/Status-Versão_Funcional-28A745?style=for-the-badge)
![Version](https://img.shields.io/badge/Versão-1.0.0-blue?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

O **EduCore** é um sistema de gerenciamento acadêmico desenvolvido em Python, com interface de linha de comando (CLI) e integração com PostgreSQL.

O projeto surgiu como uma reconstrução completa do antigo [Student Manager](https://github.com/Mutus142/Student-Manager), um dos meus primeiros projetos de programação.

Nesta nova versão, o objetivo foi desenvolver uma aplicação mais organizada, modular e funcional, aplicando conhecimentos adquiridos em Python, SQL, bancos de dados relacionais e desenvolvimento de sistemas.

O EduCore permite realizar operações de cadastro, consulta, edição e gerenciamento de informações acadêmicas, mantendo os dados armazenados em PostgreSQL.

A **versão 1.0** marca a conclusão do desenvolvimento dos cinco módulos principais: autenticação, alunos, turmas, notas e estatísticas.

O desenvolvimento também proporcionou a aplicação prática de conceitos como validação de dados, tratamento de exceções, relacionamentos SQL, controle de transações e integração entre diferentes módulos Python.

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
- Persistência dos registros no banco de dados.

**Status:** módulo funcional na versão 1.0, com melhorias de segurança previstas para futuras atualizações.

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

**Status:** funcionalidades principais desenvolvidas e testadas manualmente.

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
- Persistência das alterações no PostgreSQL.

As turmas são identificadas por valores numéricos inteiros.

**Status:** módulo funcional na versão 1.0.

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
- Recuperação de múltiplas notas utilizando `fetchall()`.

O sistema permite registrar múltiplas avaliações para um mesmo estudante, armazenando seus valores e descrições no banco de dados.

**Status:** cadastro, edição e consulta desenvolvidos para a versão 1.0.

### 📊 Estatísticas gerais

Módulo responsável pela consulta de indicadores do sistema através de funções de agregação SQL.

**Funcionalidades implementadas:**

- Consulta do total de alunos ativos.
- Consulta do total de usuários ativos, apresentados como professores na interface.
- Contagem de registros utilizando `COUNT(*)`.
- Filtragem de registros ativos.
- Navegação entre os indicadores.
- Integração com PostgreSQL.

As estatísticas são calculadas diretamente no banco de dados, permitindo consultar os totais atualizados conforme os registros são modificados.

**Status:** módulo inicial concluído e funcional na versão 1.0.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3 | Linguagem principal |
| PostgreSQL | Banco de dados relacional |
| Psycopg 3 | Integração Python e PostgreSQL |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| SQL | Consultas e manipulação de dados |
| Git | Controle de versões |
| GitHub | Hospedagem do código |
| Linux / openSUSE | Ambiente de desenvolvimento |
| VS Code | Editor de código |

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
- Comandos `SELECT`, `INSERT`, `UPDATE` e `DELETE`.
- Funções de agregação como `COUNT(*)`.
- Métodos `fetchone()` e `fetchall()`.
- Controle de transações com PostgreSQL.
- Organização e navegação em aplicações CLI.

---

## 🏗️ Arquitetura do projeto

O EduCore utiliza uma estrutura modular, dividindo suas funcionalidades em diferentes diretórios para facilitar a manutenção e evolução do sistema.

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
├── estatisticas/
│   ├── menu.py
│   └── services.py
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

*Estrutura representativa dos principais módulos da versão 1.0. Os arquivos internos de gerenciamento de alunos podem ser consultados diretamente no repositório.*

### Organização

| Módulo | Função |
|---|---|
| `main.py` | Inicialização e navegação inicial |
| `login/` | Autenticação e cadastro de usuários |
| `menu/` | Menu principal do sistema |
| `alunos/` | Gerenciamento de estudantes |
| `notas/` | Cadastro, consulta e edição de notas |
| `turmas/` | Cadastro, edição e exclusão de turmas |
| `estatisticas/` | Contagem de alunos e usuários ativos |
| `database/` | Conexão e comunicação com PostgreSQL |

---

## 🗄️ Banco de dados

O EduCore utiliza PostgreSQL como sistema gerenciador de banco de dados relacional.

A arquitetura funcional da versão 1.0 trabalha com quatro tabelas principais:

| Tabela | Responsabilidade |
|---|---|
| `usuarios` | Credenciais e situação dos usuários |
| `alunos` | Informações dos estudantes |
| `turmas` | Identificação e turno das turmas |
| `notas` | Notas e avaliações vinculadas aos alunos |

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

O número da turma também é armazenado no cadastro do estudante. Sua integração com a tabela `turmas` poderá receber melhorias de integridade referencial em atualizações futuras.

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

### Exemplo de estatística SQL

```sql
SELECT COUNT(*)
FROM alunos
WHERE ativo = TRUE;
```

Essa consulta retorna o número total de alunos ativos cadastrados no EduCore.

---

## 💻 Interface CLI

A aplicação utiliza uma interface de terminal padronizada, com menus numerados, mensagens de retorno e separadores visuais.

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

### Estatísticas gerais

```text
========================================
         EDUCORE | ESTATÍSTICAS
========================================
 [1] Total de alunos
 [2] Total de professores
 [3] Voltar ao menu principal
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

### Exemplo de estatística

```text
========================================
       EDUCORE | TOTAL DE ALUNOS
========================================
 Total de alunos ativos: 15
========================================
```

*Os exemplos representam o formato da interface utilizado na versão 1.0.*

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

Crie um banco de dados PostgreSQL e configure as tabelas necessárias para a aplicação.

Na raiz do projeto, crie o arquivo `.env`:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=educore
DB_USER=postgres
DB_PASSWORD=sua_senha
```

Os nomes das variáveis devem corresponder às configurações utilizadas em `database/conector.py`.

**Importante:** nunca publique o arquivo `.env`, credenciais de acesso ou senhas reais no GitHub.

### 5. Iniciar o sistema

```bash
python main.py
```

Após a inicialização, o EduCore apresentará o menu inicial com as opções de login e cadastro.

**Observação:** a versão 1.0 possui seus módulos funcionais, mas ainda exige configuração manual do banco de dados.

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
- [x] Integrar autenticação com PostgreSQL.
- [ ] Implementar armazenamento seguro de senhas com Argon2.
- [ ] Finalizar testes automatizados de autenticação.

### Alunos

- [x] Cadastrar alunos.
- [x] Consultar alunos.
- [x] Editar nome e turma.
- [x] Implementar desativação lógica.
- [x] Testar as operações principais manualmente.
- [ ] Melhorar identificação de alunos por ID.

### Notas

- [x] Desenvolver cadastro de notas.
- [x] Desenvolver edição de notas.
- [x] Desenvolver consulta de notas.
- [x] Relacionar notas e alunos.
- [ ] Implementar cálculo de médias.
- [ ] Melhorar identificação das avaliações por ID.

### Turmas

- [x] Desenvolver cadastro de turmas.
- [x] Desenvolver edição de turmas.
- [x] Desenvolver remoção de turmas.
- [x] Implementar validações de número e turno.
- [x] Concluir os testes manuais das operações principais.

### Estatísticas

- [x] Criar módulo de estatísticas.
- [x] Implementar contagem de alunos ativos.
- [x] Implementar contagem de usuários ativos.
- [x] Aplicar funções de agregação SQL.
- [x] Integrar estatísticas ao menu principal.

### Finalização

- [x] Concluir os cinco módulos principais.
- [x] Padronizar a interface CLI.
- [x] Integrar os módulos ao PostgreSQL.
- [x] Finalizar o desenvolvimento funcional da versão 1.0.
- [ ] Revisar a integridade referencial do banco.
- [ ] Melhorar tratamento de erros.
- [ ] Criar testes automatizados.
- [ ] Publicar a release estável após as melhorias de segurança.

---

## 🔮 Próximas versões

Após a conclusão funcional da versão 1.0, o projeto poderá evoluir com:

- Armazenamento seguro de senhas com Argon2.
- Identificação de registros utilizando IDs.
- Cálculo automático de médias.
- Interface gráfica para desktop.
- Sistema de permissões por perfil.
- Relatórios acadêmicos avançados.
- Exportação de boletins.
- Histórico de alterações.
- Registro de atividades administrativas.
- Refatoração para arquitetura orientada a objetos.
- Ampliação dos testes automatizados.

---

## 🔒 Segurança e limitações

O EduCore é um projeto desenvolvido para fins educacionais e de portfólio.

A implementação inicial de autenticação ainda utiliza senhas em texto puro. Por isso, o sistema não deve ser utilizado em produção ou com credenciais reais até que seja implementado um mecanismo seguro de armazenamento e verificação de senhas, como Argon2.

Também estão previstas melhorias na identificação de registros, nas relações entre tabelas e nos testes automatizados.

---

## 👨‍💻 Desenvolvedor

**Mateus Ribeiro Simão**

Desenvolvedor em formação, com interesse em Python, bancos de dados,