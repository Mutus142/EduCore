from database.conector import conectar_banco
import psycopg
import time

def login_user():
    print("Bem vindo ao EduCore!")

    try:
        user = str(input("Qual é seu usuario? "))
    except ValueError:
        print("Valor invalido!")
        return

    with conectar_banco() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "select usuario from usuarios where usuario = %s and situacao = "True" "), (user,
                )

            resultado = cursor.fetchone()

            if resultado is None:
                print("Usuário não encontrado!")
                time.sleep(2)

                print("Voce quer tentar novamente ou cadastrar- se? ")

                print('''
                1 - Tentar novamente
                2 - Cadastrar-se
                ''')

                try:
                    escolha = int(input("Escolha uma opção: "))
                except ValueError:
                    print("Valor invalido!")
                    return

                if escolha == 1:
                    return

                elif escolha == 2:
                    cad_user()

                else:
                    print("Opção invalida!")
                    return

            else:
                print("Usuário validado!")

                time.sleep(2)

                try:
                    senha = str(input("Digite a sua senha: "))
                except ValueError:
                    print("Valor invalido!")
                    return

                with conectar_banco() as conexao:
                    with conexao.cursor() as cursor:
                        cursor.execute(
                            "select senha from usuarios where usuario = %s and senha = %s",(user, senha)
                        )
                        
                        resultado2 = cursor.fetchone()

                        if resultado2 is None:
                            print("Senha invalida!")
                            return
                        
                        else:
                            print("Senha validada!")
                            time.sleep(2)

                            menu()