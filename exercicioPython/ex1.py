#Faça um programa que calcula a soma de todos os números digitados pelo usuário. O
#seu programa deve perguntar para o usuário qual o tamanho da sequência de números
#a ser somada.
print("digite o tamanho da sequencia de numeros que deseja somar")
seq = int(input())
soma = 0

for i in range(1, seq+1):
  n = float(input("digite o numero que deseja somar"))
  soma = soma + n
print("A soma é ",soma)
