#Escreva um programa que lê um número inteiro N do teclado e imprime "SIM" se o número for par e maior  
#do que 10, ou for ímpar e menor do que 50. Caso contrário o programa deve imprimir "NAO".
n = int(input("Escreva um número inteiro  "))

if n % 2 == 0 and n > 10 or n % 2 == 1 and n < 50:
  print("SIM")
else:
  print("NAO")