import re

print("Ketik 'quit' untuk mengakhiri program")

hasil = 0
run = True

def kalkulator():
    global hasil, run
    hitung = ""

    if hasil == 0:
        hitung = input("Masukan nilai : ")
    else:
        hitung = input(str(hasil))

    if hitung  == 'quit':
        print("GoodBye!")
        run = False
    else:
        hitung = re.sub('[a-zA-Z,.:()""]', '', hitung)

        if hasil == 0 :
            hasil = eval(hitung)
        else:
            hasil = eval(str(hasil)+hitung)

while run:
    kalkulator()