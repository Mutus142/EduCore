
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
        try:
            nome = str(input("Nome do Aluno: "))
        except ValueError:
            print("Invalido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select nome from alunos where nome = %s", (nome,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("Aluno não encontrado!")
                    continue

                else:
                    print('''
                    O que voce quer editar?
                    1 - Nome
                    2 - Turma                
                    ''')

                    try:
                        escolha = int(input("Escolha uma opção: "))
                    except ValueError:
                        print("Invalido!")
                        continue

                    if escolha == 1:

                        try:
                            nome_novo = str(input("Nome novo: "))
                        except ValueError:
                            print("Invalido!")
                            continue

                        cursor.execute(
                            "update alunos set nome = %s where nome = %s", (nome_novo, nome)
                        )

                    elif escolha == 2:

                        try:
                            turma = int(input("Turma nova: "))
                        except ValueError:
                            print("Valor invalido!")
                            continue

                        cursor.execute(
                            "update alunos set turma = %s where nome = %s", (turma, nome)
                        )

                    else:
                        print("Opção invalida!")
                        continue