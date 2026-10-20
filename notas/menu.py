from notas.services import add_nota
from notas.services import editar_nota
#from notas.services import ver_notas


def notas():

    while True:

        print('''
        Bem vindo ao modulo de notas!
        
        1 - Adicionar Nota 
        2 - Editar Nota
        3 - Ver notas de um aluno
        4 - Voltar ao menu principal
        ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Invalido!")
            continue

        if escolha == 1:
            add_nota()

        elif escolha == 2:
            editar_nota()

        elif escolha == 3:
            #ver_notas()
            print('teste')

        elif escolha == 4:
            print("Voltando...")
            return

        else:
            print("Opção Invalida!")
            continue