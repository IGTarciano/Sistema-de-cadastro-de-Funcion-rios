# Sistema de cadastro de Funcionarios
# Projeto pessoal para portfolio
# Igor T. Gomes; 07/12/2024
# database.csv (crie este arquivo em branco inicialmente)
# Este arquivo irá armazenar os dados cadastrados
# Utilizaremos os DEF para criar uma função
# mode='a': Significa "append" (adicionar). O arquivo será aberto para adicionar novas linhas sem apagar as existentes.
# newline='': Evita linhas em branco adicionais ao escrever no arquivo CSV
# (uma peculiaridade do Python ao lidar com arquivos CSV no Windows).
# for row in reader: Itera sobre cada linha do CSV. Cada linha é representada como uma lista chamada row
# VARIAVEIS DE ENTRADA

import csv

def cadastro_pessoa(Nome,Idade,Email,CPF): # Definição da função
    with open('DataBase.csv',mode='a',newline='') as file: # O arquivo será aberto, e não excluirá as linhas e nem modificar as existentes
        writer = csv.writer(file)
        writer.writerow([Nome, Idade, Email,CPF])
        print(Nome, 'cadastrado(a) com sucesso!')

def consultar_pessoas():
    with open ('DataBase.csv',mode='r') as file:
        reader = csv.reader(file) # Cria um objeto leitor que interpreta o conteúdo do CSV linha por linha.
        print('Pessoas cadastradas: ')  # Cada linha do arquivo será lida como uma lista, onde cada elemento corresponde a uma célula (coluna) do CSV.
        for row in reader:
            if len(row) == 4: # Verifica se a linha tem exatamente 4 colunas
                print(f"Nome: {row[0]},Idade: {row[1]}, Email: {row[2]}, CPF: {row[3]}")
            else:
                print("Linha com formato inválido:", row)

def menu():
    while True:
        print('\nCadastros Funcionarios')
        print('1.Cadastrar funcionario')
        print('2.Consultar cadastro')
        print('3. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            Nome = input('Nome: ')
            Idade = input('Informe sua idade: ')
            Email = input('Digite seu email: ')
            CPF = input('Digite seu cpf: ')
            print('Funcionario cadastrado com sucesso!')
            cadastro_pessoa(Nome, Idade, Email, CPF) # precisa passar os valores coletados pelo input como argumentos para a função cadastro_pessoa

        elif opcao == '2':
            consultar_pessoas()

        elif opcao == '3':
            break

        else:
            print('Opção inválida, tente novamente!')

menu() #A chamada explícita menu() no final do código é o que faz o Python entrar na função e executar seu conteúdo.

