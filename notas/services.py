
from database.conector import conectar_banco
import math


def add_nota():

    while True:

        print("""
========================================
        EDUCORE | ADICIONAR NOTA
========================================
""")

        nome = input(" > Nome do aluno: ").strip()

        if not nome:
            print("[ERRO] Nome inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT id_aluno, nome, turma
                    FROM alunos
                    WHERE nome = %s AND ativo = TRUE
                    """,
                    (nome,)
                )

                resultados = cursor.fetchall()

                if not resultados:
                    print("\n[ERRO] Aluno não encontrado!")
                    continue

                if len(resultados) > 1:
                    print("[ERRO] Existem alunos com esse nome!")
                    print("[AVISO] Será necessário consultar pelo ID.")
                    return

                id_aluno, nome_aluno, turma = resultados[0]

                print(f"""
----------------------------------------
          ALUNO ENCONTRADO
----------------------------------------
 Nome  : {nome_aluno}
 Turma : {turma}
----------------------------------------
""")

                try:
                    nota = float(input(" > Valor da nota (0 a 10): "))

                    if not math.isfinite(nota) or nota < 0 or nota > 10:
                        raise ValueError

                except ValueError:
                    print("[ERRO] Nota inválida! Use um valor entre 0 e 10.")
                    continue

                descricao = input(" > Descrição da avaliação: ").strip()

                if not descricao:
                    print("[ERRO] Descrição obrigatória!")
                    continue

                cursor.execute(
                    """
                    INSERT INTO notas (id_aluno, valor, descricao)
                    VALUES (%s, %s, %s)
                    """,
                    (id_aluno, nota, descricao)
                )

        print("""
----------------------------------------
       NOTA ADICIONADA COM SUCESSO!
----------------------------------------
""")
        return

def editar_nota():

    print("""
========================================
         EDUCORE | EDITAR NOTA
========================================
""")

    print("[AVISO] Funcionalidade em desenvolvimento!")