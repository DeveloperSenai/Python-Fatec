import os 
os.system("cls")
# #IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
# #ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO

# #NO CASO DE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("Digite sua idade: "))

# if idade <12:
#     print("CRIANÇA")
# if idade <18:
#     print("ADOLESCENTE")
# if idade <60:
#     print("ADULTO")
# else:
#     print("IDOSO")
    
# #SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# idade = int(input("Digite sua idade: "))

# if idade <12:
#     print("CRIANÇA")
# elif idade <18:
#     print("ADOLESCENTE")
# elif idade <60:
#     print("ADULTO")
# else:
#     print("IDOSO")

#MEDIA
# nota1= float(input("Digite sua primeira nota: "))
# nota2= float(input("Digite sua segunda nota: "))

# media = (nota1+nota2)/2

# print(f"Sua media é: {media}")

# if media <5:
#     print("REPROVADO")
# elif media >=5 and media <=7:
#     print("EM RECUPERAÇÃO")
# else:
#     print("APROVADO")
    
# #IMC
# altura = float(input("Digite sua altura: "))
# peso = float(input("Digite seu peso: "))
# imc = peso/(altura*altura)

# print(f"Seu imc é {imc:.2f}")


# if imc < 17:
#     print("muito abaixo do peso")
# elif imc >=17 and imc <=18.49:
#     print("abaixo do peso")
# elif imc >=18.5 and imc <=24.99:
#     print("peso normal")
# elif imc >=25 and imc <=29.99:
#     print("Acima do peso")
# elif imc >=30 and imc <=34.99:
#     print("Obesidade 1")
# elif imc >=35 and imc <=39.99:
#     print("Obesidade 2")
# else:
#     print("Mórbida")