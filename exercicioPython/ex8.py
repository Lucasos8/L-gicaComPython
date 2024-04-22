#Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura 
#de um retângulo. O programa deve imprimir o retângulo informado com caracteres ’#’ na saída.
print("Digite a altura e a largura do retângulo para que ele possa ser feito em #, utilize apenas números inteiros.")
a = int(input("Coloque a altura "))
l = int(input("Coloque a largura "))

for i in range(1, a+1):
  print("#" * l)