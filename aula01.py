# Aula 01 - Exibindo mensagens no terminal com print("")
#TIPOS DE DADOS
# String (texto) -> sempre entre aspas dupla
# Int, Float (inteiro,nº quebrados) -> sem aspas dupla

#print(" Olá Mundo!") #texto (string)
#print(10) # n inteiro  (int)
#print(5.99) # n quebrado (float)

#operações matematicas + - / *
#print("10" + "10") # SOMANDO TEXTO (concatenação)
#print(10 + 10) # somando numero 
 

#parametros no print
#print(a,b,c,d,e..... ) até 128 parametros 
#print("escola senai")
#print("escola" , "senai")

#ex1 
#print("daniel 26 999-999-999-99")
#print("daniel", "26", "999.999.999-99")

#Formatações Sep E End -> Final do print()
#sep -> operador de sepração  (troca o caracter , por outro caracter)
#end -> operador final  (coloca o caracter no final do print)


# #sep * OBRIGATORIO USAR PARAMETROS
# print("Hoje","é","dia","06")
# print("Hoje","é","dia","06",sep="!")
# #end -> Coloca o caractere no final e deixa os prints na mesma linha
# #\n -> quebra linha
# print("Curso de python",end=" no senai ")
# print("\naprendendo operadores no print")
# #usando sep e end no mesmo print
# print("Cade", "minha", "mesa com regulagem de altura",sep="*()*",end=" espero que comprem!")


# Curso_de_python%%
# *no senai rio claro em parceria com a fatec@
# _-_-_logica_-_-_de_-_-_programação


# print("Curso","de","python",sep="_",end="%%\n")
# print("* no senai rio claro em parceria com a fatec",end="@\n")
# print("","logica","de","programação",sep="_-_-_")

#ex3 
# python@@@versao3[]
# logica#de#programação
# &uso&do&print()

# print("python","versao",sep="@@@",end="3[]")
# print("\nlogica","de","programação",sep="#")
# print("","uso","do","print", sep="&",end="()")


print("*"*10,"LOJA DO SENAI", "*"*10)



print("Soma 100 + 50 = ", 100+50)

print("Multiplicando 30*3,33 = ", 30*3.33) 


print("#"*20,"PADARIA PÃO DE ONTEM","#"*20)
print("."*10,"TABELA DE PREÇOS","."*10)
print("AGUA :      ","."*10,"R$:10,00")
print("COCA-COLA : ","."*10,"R$:5,00")
print("PÃO MURCHO: ","."*10,"R$:1,25")