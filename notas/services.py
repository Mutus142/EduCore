from database.conector import conectar_banco


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
                    SELECT m.id_matricula
                    FROM alunos a
                    INNER JOIN matriculas m
                        ON a.id_aluno = m.id_aluno
                    WHERE a.nome = %s
                      AND a.ativo = TRUE
                    """,
                    (nome,)
                )

                resultado = cursor.fetchall()

                if not resultado:
                    print("\n[ERRO] Aluno ou matrícula não encontrada!")
                    continue

                if len(resultado) > 1:
                    print("[ERRO] Mais de uma matrícula encontrada!")
                    print("[AVISO] Selecione a matrícula pelo ID.")
                    return

                id_matricula = resultado[0][0]

                try:
                    nota = float(input(" > Valor da nota (0 a 10): "))

                    if not math.isfinite(nota) or nota < 0 or nota > 10:
                        raise ValueError

                except ValueError:
                    print("[ERRO] Nota inválida! Informe um valor entre 0 e 10.")
                    continue

                descricao = input(" > Descrição da avaliação: ").strip()

                if not descricao:
                    print("[ERRO] Descrição obrigatória!")
                    continue

                cursor.execute(
                    """
                    INSERT INTO notas
                        (id_matricula, valor, descricao)
                    VALUES (%s, %s, %s)
                    """,
                    (id_matricula, nota, descricao)
                )

                print("""
----------------------------------------
       NOTA ADICIONADA COM SUCESSO!
----------------------------------------
""")
                return


def editar_nota():

    while True:
        print()