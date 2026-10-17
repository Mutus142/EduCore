from database.conector import conectar_banco


while True:
    def cad_aluno():

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

                resultado = cursor.fetchone

                if resultado is not None:
                    print("Aluno já cadastrado!")
                    continue

                else:
                    try:
                        turma = int(input("Turma do aluno: "))
                    except ValueError:
                        print("Invalido!")
                        continue

                    with conectar_banco() as conexao:
                        with conexao.cursor() as cursor:
                            cursor.execute(
                                "insert into alunos values(%s, %s)", (nome, turma)
                            )