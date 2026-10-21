from database.conector import conectar_banco


def add_turma():

    while True:

        print("""
========================================
        EDUCORE | CADASTRAR TURMA
========================================
""")

        try:
            turma_nova = int(input(" > Número da turma: "))
        except ValueError:
            print("[ERRO] Turma inválida!")
            continue

        if turma_nova <= 0:
            print("[ERRO] Informe um número positivo!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT nome FROM turmas WHERE nome = %s",
                    (turma_nova,)
                )

                resultado = cursor.fetchone()

                if resultado is None:

                    turno = input(" > Turno (Manhã/Tarde): ").strip().capitalize()

                    if turno not in ("Manhã", "Tarde"):
                        print("[ERRO] Turno inválido!")
                        continue

                    cursor.execute(
                        "INSERT INTO turmas (nome, turno) VALUES (%s, %s)",
                        (turma_nova, turno)
                    )

                    print(f"""
----------------------------------------
      TURMA CADASTRADA COM SUCESSO!
----------------------------------------
 Turma : {turma_nova}
 Turno : {turno}
----------------------------------------
""")

                else:
                    print("\n[ERRO] Essa turma já está cadastrada!")

        print("""
----------------------------------------
          OPÇÕES DISPONÍVEIS
----------------------------------------
 [1] Adicionar outra turma
 [2] Editar uma turma
 [3] Voltar ao menu
----------------------------------------
""")

        try:
            escolha = int(input(" > Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
            continue

        if escolha == 1:
            continue

        elif escolha == 2:
            editar_turma()
            return

        elif escolha == 3:
            print("[AVISO] Retornando ao menu...")
            return

        else:
            print("[ERRO] Opção inválida!")
            continue

def editar_turma():

    while True:

        try:
            turma = int(input("Turma: "))
        except ValueError:
            print("Invalido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select nome from turmas where nome = %s", (turma,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("Turma não encontrada!")
                    continue

                else:
                    print('''
                    Voce quer alterar o que?
                    1 - Nome
                    2 - Turno
                    ''')

                    try:
                        escolha = int(input("Escolha uma opção: "))
                    except ValueError:
                        print("Invalido!")
                        continue

                    if escolha == 1:

                        try:
                            nome_novo = int(input("Nome novo da Turma: "))
                        except ValueError:
                            print("Invalido!")
                            continue

                        cursor.execute(
                            "update turmas set nome = %s where nome = %s", (nome_novo, turma)
                        )

                        print("Nome alterado com sucesso!")

                    elif escolha == 2:

                        turno_novo = input("Turno novo Manha/Tarde : ")

                        if turno_novo is not in ("Manha" , "Tarde")
                            print("Invalido! Digite Manha ou Tarde!")

                        else:
                            cursor.execute(
                                "update turmas set turno = %s where nome = %s", (turno_novo, turma)
                            )

                            print("Turno Alterado com sucesso!")


                    else:

                        print("Opção invalida!")