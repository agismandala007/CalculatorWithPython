def penjumlahan(a, b):
  return a+b

def pengurangan(a, b):
  return a-b

def pembagian(a, b):
  return a/b

def perkalian(a, b):
  return a*b

a = int(input("Masukan a : "))
b = int(input("Masukan b : "))

operator = input("Masukan operator : ")
if operator == '+':
  print(penjumlahan(a, b))
elif operator == '-':
  print(pengurangan(a, b))
elif operator == '/':
  print(pembagian(a, b))
elif operator == '*':
  print(perkalian(a, b))
