
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
