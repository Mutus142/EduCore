from database.conector import conectar_banco

def add_notas():

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
                    try:
                        nota = float(input("Valor da nota a ser adicionada: "))

                        if nota < 0.0 and > 10.0
                            raise

                    except ValueError:
                        print("Nota invalida! Precisa ser tipo float!")