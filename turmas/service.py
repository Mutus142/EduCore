from database.conector import conectar_banco

def add_turma():

    while True:

        print("Bem vindo ao cadastro de turmas!")

        try:
            turma_nova = int(input("Nome da Turma nova: "))
        except ValueError:
            print("Invalido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select nome from turmas where nome = %s", (turma_nova,)
                )

                resultado = cursor.fetchone()

                if resultado is None:

                    try:
                        turno = str(input("Em qual turno? Manha/Tarde "))
                    except ValueError:
                        print("invalido!")
                        continue

                    cursor.execute(
                        "insert into turmas (nome, turno) values (%s, %s)", (turma_nova, turno)
                    )