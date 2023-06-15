import sqlite3
import getpass
from functions.usuario_db import create_user, list_user, login_user
from functions.medicacao_db import register_medicine, list_medicine, update_medicine, delete_medicine, validate

conn = sqlite3.connect('farmacia.db')
c = conn.cursor()

def menuLogin():
  print('\n1 - Cadastrar Usuário')
  print('2 - Fazer Login')
  print('3 - Sair')
  opcaoUser = input('\nDigite uma opção para prosseguir: ')
  
  return int(opcaoUser)

def cadastrarUsuario():
  user = input('Informe seu novo usuário: ')
  password = getpass.getpass('Informe sua nova senha: ')
  create_user(conn, user, password)
  
def listarUsuario():
  usuario = list_user(conn)
  print(usuario)
  
def fazerLogin():
  user = input('Digite seu usuário: ')
  password = getpass.getpass('Digite sua senha: ')
  cursor = login_user(conn, user, password)
  if cursor: 
    print('\nLogin realizado com sucesso!')
    return True
  else:
    print('\n Usuário e/ou senha inválido!')
    return False
  
def menuPrincipal():
  print('\n1 - Cadastrar novo medicamento: ')
  print('2 - Listar medicamentos: ')
  print('3 - Alterar medicamento: ')
  print('4 - Excluir medicamento: ')
  print('5 - Sair')
  opcaoMenu = input('\nDigite a opção desejada: ')
  
  return int(opcaoMenu)
  
def cadastrarMedicamento():
  nome = input('\nInforme o nome do medicamento: ')
  quantidade = input('\nInforme a quantidade em estoque: ')
  preco = float(input('\nInforme o preço do medicamento: '))
  register_medicine(conn, nome, quantidade, preco)
  
def listarMedicamento():
  produto = list_medicine(conn)
  print(produto)
  
def atualizarMedicamento():
  produto_id = int(input('Informe o código do medicamento que deseja atualizar: '))
  if validate(conn, produto_id):
    return print('\nEste produto não está cadastrado no sistema!')
  quantidade = int(input('\nInforme o valor atualizado do estoque: '))
  preco = float(input('\nInforme o preço atualizado do medicamento: '))
  update_medicine(conn, produto_id, quantidade, preco)

def excluirMedicamento():
   produto_id = input('Informe o código do medicamento que deseja excluir: ')
   delete_medicine(conn, produto_id)

print("\n=============================================\n")
print("==== BEM-VINDO(A) AO SISTEMA DA FARMÁCIA ====")
print("\n=============================================\n")
print('\nEscolha uma opção: \n')

opcaoUser = 0

while True:
    opcaoUser = menuLogin()
    if opcaoUser == 1:
        cadastrarUsuario()
    elif opcaoUser == 2:
        if fazerLogin():
            break
    elif opcaoUser == 3:
        exit()
    else: 
        print("\nOpção inválida. Digite uma opção de 1 a 3.")

opcaoMenu = 0 

while opcaoMenu != 5:
    opcaoMenu = menuPrincipal()

    if opcaoMenu == 1:
        cadastrarMedicamento()
    elif opcaoMenu == 2:
        listarMedicamento()
    elif opcaoMenu == 3:
        atualizarMedicamento()
    elif opcaoMenu == 4:
        excluirMedicamento()
    elif opcaoMenu == 5:
        break
    else:
        print("\nOpção inválida. Digite uma opção de 1 a 5.")