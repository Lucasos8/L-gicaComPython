#Faça um programa que lê n números inteiros do teclado, e no final informa qual foi
#o maior número lido. O programa deve encerrar quando o usuário digita 0.
print("digite varios numeros e o programa identificarar o maior digitado, para encerrar digite 0")
n = -1
nMaior = 0
while(n != 0):
    n = int(input("digite o numero inteiro"))
    if n > nMaior:
      nMaior = n
print("O número maior é ", nMaior)