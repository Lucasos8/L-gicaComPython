#Faça um programa que monte os oito primeiros termos da sequência de Fibonacci. 0-1-1-2-3-5-8-13-21-34-55...
print("sequencia de Fibonacci")
termo = 0
for i in range(1, 9):
  if termo == 0:
    print(0)
    termo = 0 + 1
    print(termo)
  elif termo == 1:
    print(termo)
    termo = 1 + 1
    print(termo)
  elif termo == 2:
    termo = termo + 1
    print(termo)
  elif termo == 3:
    termo = termo + 2
    print(termo)
  elif termo == 5:
    termo = termo + 3
    print(termo)
  elif termo == 8:
    termo = termo + 5
    print(termo)
  elif termo == 13:
    termo = termo + 8
    print(termo)
  else:
    termo = termo + 13
    print(termo," - ")