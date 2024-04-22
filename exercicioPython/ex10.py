#Faça um programa que receba um número inteiro maior que 1, verifique se o número fornecido é primo
#ou não e mostre uma mensagem de número primo ou de número não primo.
#Um número é primo quando é divisível apenas por 1 e por ele mesmo.
n = int(input("Digite seu número para ver se é primo ou não primo "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "não é um número primo")
            break
    else:
        print(n, "é um número primo")
else:
    print(n, "não é um número primo")