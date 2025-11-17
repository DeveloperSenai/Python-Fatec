import os
os.system("cls")
os.system("color 6")

#FUNÇOES
#organizar o codigo e evitar a duplicidade
#def nomeFuncao():
#A funcao so sera executada ao ser chamada pelo nome 

#FUNCAO SEM PARAMETRO E FUNCAO SEM RETORNO
# def Conteudo():
#     print("AULA DE FUNÇÕES")
#     print("Estudando funcoes sem parametro e retorno!")
    
# #Chamando a funcao pelo nome para ser executada
# Conteudo()   

#FUNCAO SEM PARAMETRO E COM RETORNO
# def FuncaoRetornaNumero():
#     #print("Essa funcao retorna o numero 10 :)")
#     return 100
#     # APOS O COMANDO RETURN , A FUNCAO NÃO É MAIS EXECUTADA

# # print(FuncaoRetornaNumero())
# # x= FuncaoRetornaNumero()
# # print(x)

# def FuncaoExecutaNumero():
#     print(100)

# x = FuncaoRetornaNumero()
# y = FuncaoExecutaNumero()


# print(f"o valor de x,{x}")
# print(f"o valor de y , {y}")

#Uma varivel so ira armazenar o valor de uma funcao se a função tiver o comando return


#FUNCAO SEM RETORNO E COM PARAMETRO()

# def ExecutaSoma(num1,num2):
#     print(num1 + num2)


# #TODA FUNCAO COM PARAMETRO AO SER CHAMADA É OBRIGATÓRIO PASSAR OS PARAMETROS ENTRE PARENTESES()
# ExecutaSoma(15,20)
# ExecutaSoma(100,200)


#FUNCAO COM PAREMTRO E COM RETORNO()
# def RetornaSoma(num1,num2):
#     return num1+num2

# print(RetornaSoma(5,10))

# def ExecutaOperacoesMatematicas(n1,n2):
#     print(n1+n2)
#     print(n1-n2)
#     print(n1*n2)
#     print(n1/n2)    
    
# ExecutaOperacoesMatematicas(10,10)

#ESCOPO DE FUNCAO

# numero = 100 

# def Escopo(numero=200):
#     print(numero)

# print(numero)
# Escopo()

#VARIAVEIS DECLARADAS FORA DE UMA FUNCAO. SÃO CONSIDERADAS VARIAVIES GLOBAIS
#VARIAVEIS DECLARADAS NO PARAMETRO DE UMA FUNCAO OU DENTRO DE UM FUNCAO, APENAS A FUNCAO ENXERGA

# x=10

# def Exemplo():
#     global x #O COMANDO GLOBAL SERVE PARA ACESSAR VARIAVEIS FORA DA FUNCAO
#     x=15
    
# Exemplo()
# print(x)

#1
# def Multiplicacao(n1,n2):
#     return n1*n2

# print(Multiplicacao(5,10))

#2-

def Dolar_Real():
    moeda = float(input("Digite a quantidade de Dolar para converter para real R$: "))
    print(f"Voce tem R$: {moeda*5.30:.2f}")

def Real_Dolar():
    moeda = float(input("Digite a quantidade de Real para converter para Dolar $: "))
    print(f"Voce tem $: {moeda/5.30:.2f}")

def Menu():
    print("PROGRAMA DE CONVERSÃO DOLAR E REAL ")
    print("""
          1-Convete dolar para real
          2-Converte real para dolar
          3-Sai do programa
          """)

opcao = 0 

while opcao !=3:
    Menu()
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao ==1:
        Dolar_Real()
    elif opcao ==2:
        Real_Dolar()
    elif opcao ==3:
        print("Saiu do programa")
    else:
        print("opção invalida")