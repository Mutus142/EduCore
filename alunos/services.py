
from database.conector import conectar_banco


def cad_aluno():

    while True:

        print("""
========================================
       EDUCORE | CADASTRO DE ALUNO
========================================
""")

        nome = input(" > Nome do aluno: ").strip()

        if not nome:
            print("[ERRO] Nome inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT nome FROM alunos WHERE nome = %s",
                    (nome,)
                )

                resultado = cursor.fetchone()

                if resultado is not None:
                    print("\n[ERRO] Aluno já cadastrado!")
                    continue

                else:
                    turma = input(" > Turma do aluno: ").strip()

                    if not turma:
                        print("[ERRO] Turma inválida!")
                        continue

                    cursor.execute(
                        "INSERT INTO alunos (nome, turma) VALUES (%s, %s)",
                        (nome, turma)
                    )

                    print("""
----------------------------------------
      ALUNO CADASTRADO COM SUCESSO!
----------------------------------------
""")
                    return



def ver_aluno():

    while True:

        print("""
========================================
        EDUCORE | CONSULTAR ALUNO
========================================
""")

        try:
            nome = str(input(" > Nome do aluno: "))
        except ValueError:
            print("[ERRO] Nome inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT nome FROM alunos WHERE nome = %s",
                    (nome,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("\n[ERRO] Aluno não encontrado!")
                    continue

                else:

                    cursor.execute(
                        "SELECT turma FROM alunos WHERE nome = %s",
                        (nome,)
                    )

                    turma = cursor.fetchone()

                    print(f"""
----------------------------------------
          DADOS DO ALUNO
----------------------------------------
 Nome  : {nome}
 Turma : {turma[0]}
----------------------------------------
""")
                    return


def remover_aluno():

    while True:

        print("""
========================================
        EDUCORE | REMOVER ALUNO
========================================
""")

        try:
            nome = str(input(" > Nome do aluno: "))
        except ValueError:
            print("[ERRO] Nome inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT nome FROM alunos WHERE nome = %s AND ativo = TRUE",
                    (nome,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("\n[ERRO] Aluno não encontrado ou já está inativo!")
                    continue

                else:

                    print(f"""
----------------------------------------
       CONFIRMAÇÃO DE REMOÇÃO
----------------------------------------
 Aluno : {nome}

 Deseja realmente desativar este aluno?
----------------------------------------
""")

                    confirmacao = input(" > Confirmar (S/N): ").strip().upper()

                    if confirmacao == 'S':

                        cursor.execute(
                            "UPDATE alunos SET ativo = FALSE WHERE nome = %s",
                            (nome,)
                        )

                        print("""
----------------------------------------
       ALUNO DESATIVADO COM SUCESSO!
----------------------------------------
""")
                        return

                    elif confirmacao == 'N':
                        print("\n[AVISO] Operação cancelada!")
                        return

                    else:
                        print("[ERRO] Opção inválida! Utilize S ou N.")
                        continue

def editar_aluno():

    while True:

        print("""
========================================
         EDUCORE | EDITAR ALUNO
========================================
""")

        nome = input(" > Nome do aluno: ").strip()

        if not nome:
            print("[ERRO] Nome inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT nome FROM alunos WHERE nome = %s AND ativo = TRUE",
                    (nome,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("\n[ERRO] Aluno não encontrado!")
                    continue

                else:
                    print("""
----------------------------------------
         OPÇÕES DE EDIÇÃO
----------------------------------------
 [1] Editar nome
 [2] Editar turma
 [0] Cancelar
----------------------------------------
""")

                    try:
                        escolha = int(input(" > Escolha uma opção: "))
                    except ValueError:
                        print("[ERRO] Opção inválida!")
                        continue

                    if escolha == 1:

                        nome_novo = input(" > Novo nome: ").strip()

                        if not nome_novo:
                            print("[ERRO] Nome inválido!")
                            continue

                        cursor.execute(
                            """
                            UPDATE alunos
                            SET nome = %s
                            WHERE nome = %s AND ativo = TRUE
                            """,
                            (nome_novo, nome)
                        )

                        print("""
----------------------------------------
       NOME ATUALIZADO COM SUCESSO!
----------------------------------------
""")
                        return

                    elif escolha == 2:

                        try:
                            turma = int(input(" > Nova turma: "))
                        except ValueError:
                            print("[ERRO] Turma inválida! Digite um número inteiro.")
                            continue

                        if turma <= 0:
                            print("[ERRO] A turma deve ser um número positivo!")
                            continue

                        cursor.execute(
                            """
                            UPDATE alunos
                            SET turma = %s
                            WHERE nome = %s AND ativo = TRUE
                            """,
                            (turma, nome)
                        )

                        print("""
----------------------------------------
      TURMA ATUALIZADA COM SUCESSO!
----------------------------------------
""")
                        return

                    elif escolha == 0:
                        print("\n[AVISO] Edição cancelada!")
                        return

                    else:
                        print("[ERRO] Opção inválida!")
                        continue
