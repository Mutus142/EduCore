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

        print("""
========================================
         EDUCORE | EDITAR TURMA
========================================
""")

        try:
            turma = int(input(" > Número da turma: "))
        except ValueError:
            print("[ERRO] Turma inválida!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT nome FROM turmas WHERE nome = %s",
                    (turma,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("\n[ERRO] Turma não encontrada!")
                    continue

                else:
                    print("""
----------------------------------------
          OPÇÕES DE EDIÇÃO
----------------------------------------
 [1] Alterar número da turma
 [2] Alterar turno
----------------------------------------
""")

                    try:
                        escolha = int(input(" > Escolha uma opção: "))
                    except ValueError:
                        print("[ERRO] Opção inválida!")
                        continue

                    if escolha == 1:

                        try:
                            nome_novo = int(input(" > Novo número da turma: "))
                        except ValueError:
                            print("[ERRO] Número inválido!")
                            continue

                        if nome_novo <= 0:
                            print("[ERRO] Informe um número positivo!")
                            continue

                        cursor.execute(
                            "SELECT nome FROM turmas WHERE nome = %s",
                            (nome_novo,)
                        )

                        if cursor.fetchone() is not None:
                            print("[ERRO] Já existe uma turma com esse número!")
                            continue

                        cursor.execute(
                            "UPDATE turmas SET nome = %s WHERE nome = %s",
                            (nome_novo, turma)
                        )

                        print("""
----------------------------------------
     TURMA ATUALIZADA COM SUCESSO!
----------------------------------------
""")
                        return

                    elif escolha == 2:

                        turno_novo = input(" > Novo turno (Manha/Tarde): ").strip().capitalize()

                        if turno_novo not in ("Manha", "Tarde"):
                            print("[ERRO] Turno inválido! Digite Manha ou Tarde.")
                            continue

                        else:
                            cursor.execute(
                                "UPDATE turmas SET turno = %s WHERE nome = %s",
                                (turno_novo, turma)
                            )

                            print("""
----------------------------------------
      TURNO ATUALIZADO COM SUCESSO!
----------------------------------------
""")
                            return

                    else:
                        print("[ERRO] Opção inválida!")
                        continue

]
def remover_turma():

    while True:

        try:
            turma = int(input("Turma que deseja excluir: "))
        except ValueError:
            print("Invalido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select nome from turmas where nome = %s", (turma)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("Turma não encontrada!")
                    continue

                else:

                    confirmacao = input("Tem certeza dessa operação? S/N").upper()

                    if confirmacao not in ("S" , "N"):
                        print("Invalido! Utilize S/N")

                    elif confirmacao == "S":

                        cursor.execute(
                            "delete from turmas where nome = %s", (turma,)
                        )

                        print("Turma removida!")

                    elif confirmacao == "N":
                        print("Operação abortada!")
                        return

            return