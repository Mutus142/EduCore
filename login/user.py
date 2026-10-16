from database.conector import conectar_banco
import psycopg
import time
from menu.menu import menu
from login.cadastro import cad_user

def login_user():

    while True:

        print("Bem vindo ao EduCore!")

        try:
            user = str(input("Qual é seu usuario? "))
        except ValueError:
            print("Valor invalido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT usuario FROM usuarios WHERE usuario = %s AND situacao = TRUE",
                    (user,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("Usuário não encontrado!")
                    time.sleep(2)

                    print("Voce quer tentar novamente ou cadastrar-se? ")

                    print('''
                    1 - Tentar novamente
                    2 - Cadastrar-se
                    ''')

                    try:
                        escolha = int(input("Escolha uma opção: "))
                    except ValueError:
                        print("Valor invalido!")
                        continue

                    if escolha == 1:
                        continue

                    elif escolha == 2:
                        cad_user()

                    else:
                        print("Opção invalida!")
                        continue

                else:
                    print("Usuário validado!")
                    time.sleep(2)

                    try:
                        senha = str(input("Digite a sua senha: "))
                    except ValueError:
                        print("Valor invalido!")
                        continue

                    with conectar_banco() as conexao:
                        with conexao.cursor() as cursor:
                            cursor.execute(
                                "SELECT senha FROM usuarios WHERE usuario = %s AND senha = %s",
                                (user, senha)
                            )

                            resultado2 = cursor.fetchone()

                            if resultado2 is None:
                                print("Senha invalida!")
                                continue

                            else:
                                print("Senha validada!")
                                time.sleep(2)

                                menu()
                                return