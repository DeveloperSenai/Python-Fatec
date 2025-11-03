import os 
os.system("cls")
os.system("color 6")

#Estrutura de repetição FOR
#O numero colocado no range é a quantidade de vezes a ser repetido
#por convenção usa-se a variavel i no for, porem pode ser qualquer nome

#for com 1 parametro
# for i in range(10):# i começa em 0 e vai até range -1 (de 0 a 9)
#     print(f"hello word! {i}")
# else:
#     print("acabou o for")


#for com 2 parametros
# for i in range(1,10): #i começa em 1 e vai até range -1  (1 a 10)
#     print(f"hello word {i}")

# for com 3 parametros
# for i in range(1,10,2): #i começa em 1 , vai até range(-1) e incrementa de 2 em 2 
#     print(i)
    
#é possivel tambem porcorrer com negativos
# for i in range(-10, -20,-1):
#     print(i)

#30 a 47

# for i in range(30,48):
#     print(i)    

#0 a -50
# for i in range(0,-51,-1):
#     print(i)

#taboada
# numero = int(input("Digite um numero para taboada: "))

# for i in range(1,11):
#     print(f"{numero} X {i} = {numero*i}")


#padaria


# print("*"*30,"PADARIA PAO DE ONTEM","*"*30)

# precoPao = float(input("Digite o preço do pao: "))

# for i in range(1,51):
#     print(i , f" - R$: {precoPao*i:.2f}")

# qtd = int(input("Digite a quantidade que gostaria de levar: "))
# total = precoPao*qtd

# print(f"TOTAL DA COMPRA SEM DESCONTO  R$: {total:.2f}")

# cupom = input("Digite um cupom de desconto: ").lower()

# if cupom == "paomurcho":
#     total = total -(total*0.10)
#     print("CUPOM VALIDO APLICADO 10% DE DESCONTO!")
# else:
#     print("CUPOM INVALIDO DESCONTO NAO APLICADO!")
     
# print(f"TOTAL DA COMPRA COM/SEM CUPOM R$: {total:.2f}")

# pagto = int(input("DIGITE A FORMA DE PAGTO (APENAS O VALOR): NOTA 2 | NOTA 5 | NOTA 10 | NOTA 50: "))

# if pagto > total:
#     print(f"TROCO DE R$: {pagto-total:.2f}")
# elif pagto < total:
#     print(f" DINHEIRO INSULFICIENTE , FALTAM R$: {total-pagto:.2f}")
# else:
#     print("NÃO TEM TROCO, PAGAMENTO OK!")
    
    
    
#desafio ! 

#Faça um programa que leia 5 números 
# e informe o maior número. 

#DICA USEM 2 VARIAVEIS
#NUMERO
#MAIORNUMERO

maiornumero=0
numero=0


for i in range(5):
    numero = float(input("Digite um numero: "))
    
    # if i ==0:  #- validação para numeros negativos!
    #     maiornumero=numero 
    
    if numero > maiornumero:
        maiornumero = numero

print(maiornumero)