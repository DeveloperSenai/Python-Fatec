import os # importa a biblioteca de sistema operacional
#aula 02 -> variaveis, tipos e input
#tipos de dados
#String -> texto
#int -> Inteiro
#float -> n quebrado

#declaração de variaveis
# escola="senai" 
# #mostrando variavel no print
# #concatenando variavel
# print("o nome da minha escola é " + escola)
# #separando por parametro ,
# print("o nome da minha escola é ",escola)
# # f string {} -> mostra o valor da variavel dentro das aspas
# print(f"o nome da minha escola é {escola}")

#exemplo de variavel int e float
# numeroInteiro=100
# numeroQuebrado=12.5
# soma = numeroInteiro + numeroQuebrado

# print("Somando numeroInteiro com 10", numeroInteiro+10)
# print(f"Subtraindo numeroQuebrado com 5= {numeroQuebrado-5}")
# print(f"Somando numeroInteiro com numeroQuebrado =  {soma}")
# print("Multipliando soma x2", soma*2)

#atividade 1

#os.system("cls") #limpa a tela
#os.system("color 2")# troca a cor no terminal

# nome="daniel"
# cpf="123.456.789-10"
# idade="26"

# print("#"*10,"DADOS CADASTRADOS","#"*10)
# print(f"Nome: {nome}")
# print(f"Cpf: {cpf}")
# print(f"Idade: {idade} anos")


#input("") -> Pergunta algo pro usuario e armazena em uma variavel
#Obrigatoriamente antes do input deve existir uma variavel

# escola = input("Digite algo...: ")
# print(f"Voce estuda no(a) {escola}")

#resumindo...
#input()-> pergunta algo ao usuario e armazena o valor
#print()-> exibe algo ao usuario mas não armazena valor

#atividade 2 
# os.system("cls")
# print("*"*5,"CADASTRO","*"*5)
# nome=input("Digite seu nome: ")
# cpf=input("Digite seu cpf: ")
# rg= input("Digite seu rg: ")
# print("*"*5,"DADOS DE CADASTRO","*"*5)
# print(f"Nome: {nome} \ncpf:{cpf} \nrg:{rg}")


#conversão de dados
#input()-> sempre armazena os valores como string
# n = input("Digite um valor numerico: ")
# print( "tipo : ", type(n))

# #int()-> converte para numero inteiro
# #float()-> converte para numeros inteiros ou quebrados

# n = int(input("Digite um valor numerico: "))
# print( "tipo : ", type(n))

# n = float(input("Digite um valor numerico: "))
# print( "tipo : ", type(n))

#exemplo
# n1 = float(input("Digite o primeiro numero: "))
# n2 = float(input("Digite o segundo numero :"))
# print(f"A soma de {n1} + {n2} = {n1+n2}")


#atividade 3 

# num = int(input("Digite um numero: "))
# print(f"Antecessor: {num-1}\n Sucessor: {num+1}")

#atividade4
# anoNasc = int(input("Digite o ano do seu nascimento: "))
# calculo = 2025 - anoNasc
# print(f"Voce tem  {calculo} anos")

#porcentagem
# print("25% de 100= ", 0.25*100)
# print("4% de 400=", 0.04*400)
# print("99% de 1525=", 0.99*1525)

# #supondo que um produto custa 150 reais
# #e o caixa deu um desconto de 15%

# desconto = 0.15 * 150
# print(desconto)
# print(150-desconto)

#atividade supermercado
print("*"*10,"SUPERMERCADO SENAI", "*"*10)

produto1 = input("Digite o primeiro produto: ")
produto1_valor = float(input("Digite o valor desse produto: "))
desconto1=0

produto2 = input("Digite o segundo produto: ")
produto2_valor = float(input("Digite o valor desse produto: "))
desconto2=0

print("-"*50)
print("*"*10,"CAIXA", "*"*10)

desconto1= produto1_valor*0.10
desconto2= produto2_valor*0.25

print(f"{produto1} custa R$:{produto1_valor} com 10% = {produto1_valor-desconto1} ")
print(f"{produto2} custa R$:{produto2_valor} com 25% = {produto2_valor-desconto2} ")

print("-"*50)
print("*"*10,"TOTAL COMPRA", "*"*10)
print(f"TOTAL DA COMPRA R$: {(produto1_valor-desconto1) + (produto2_valor-desconto2)}")
