hasil = 0
i = "+"
while i == '+' or i == '-' or i == '*' or i == "/":
  a = int(input("Masukan angka : "))
  if i == '+':
    hasil = hasil + a
  elif i == '-':
    hasil = hasil - a
  elif i == '/':
    hasil = hasil / a
  elif i == '*':
    hasil = hasil * a
  i = input()

print(hasil)
