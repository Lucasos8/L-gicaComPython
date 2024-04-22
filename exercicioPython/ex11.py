#Faça um programa que receba vários números, calcule e mostre:
#a soma dos números digitados;
#a quantidade de números digitados;
#a média dos números digitados;
#o maior número digitado;
#o menor número digitado;
#a média dos números pares;
#a porcentagem dos números ímpares entre todos os números digitados.
#Finalize a entrada de dados com a digitação do número 30.000.
print("Bem vindo, escreva números a vontade e para finalizar gigite o número 30000")
contador = 0
soma = 0
maior = 0
menor = 9999999999999
contadorPar = 0
contadorImpar = 0
porcentagemImpar = 0
par = 0
n = 0
while n != 30000:
  #contar números digitados
  contador = contador + 1
  n = float(input("Digite um número "))
  #somar números digitados
  soma = soma + n
  #calcular a média dos números digitados
  media = soma / contador
  #definir qual é o maior
  if n > maior:
    maior = n
  #definir qual é o menor
  if n < menor:
    menor = n
  #definir se o número é par ou impar 
  if n % 2 == 0:
    contadorPar = contadorPar + 1     
    par = par + n
    mediaPar = par / contadorPar
  else:
    contadorImpar = contadorImpar + 1
#descobri porcentagem de números impares
porcentagemImpar = ((contadorImpar/contadorPar)* 100)
print("A soma de todos os números é = ", soma)
print("A quantidade de numeros digitados é = ", contador)  
print("A média dos números digitados é = ", media)  
print("O maior número digitado é = ", maior)    
print("O menor número digitado é = ", menor)
print("A média dos números pares é = ",mediaPar)
print("A porcentagem de número impar entre dosos os números digitados é = ", porcentagemImpar, "%")    