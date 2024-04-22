#Escreva uma função que calcula o maior valor de três números inteiros a, b e c.
print("Função que calcula o maior valor de três números inteiros")
a = int(input("Escreva o primeiro número "))
b = int(input("Escreva o segundo número "))
c = int(input("Escreva o terceiro número "))

if a > b and a > c:
  print("Maximo = ", a)
elif b > a and b > c:
  print("Maximo = ",b)
else:
  print("Maximo = ",c)