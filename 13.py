a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if (a>b) and (b>c):
  print(a,b,c)
if (a>c) and (c>b):
  print(a,c,b)

if (b>a) and (a>c):
  print(b,a,c)
if (b>c) and (c>a):
  print(b,c,a)

if (c>b) and (b>a):
  print(c,a,b)
if (c>a) and (a>b):
  print(c,b,a)