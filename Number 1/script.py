def nominal(bil):
    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    hsl = ""
    n2 = int(bil)
    n = abs(n2)
    if n>= 0 and n <= 11:
        hsl = angka[n]
    elif n <20:
        hsl = nominal (n-10) + " Belas "
    elif n <100:
        hsl = nominal (n/10) + " Puluh " + nominal (n%10)
    elif n <200:
        hsl = "Seratus " + nominal (n-100)
    elif n <1000:
        hsl = nominal (n/100) + " Ratus " + nominal (n%100)
    elif n <2000:
        hsl = "Seribu " + nominal (n-1000)
    elif n <1000000:
        hsl = nominal (n/1000) + " Ribu " + nominal (n%1000)
    elif n <1000000000:
        hsl = nominal (n/1000000) + " Juta " + nominal (n%1000000)
    else:
        hsl = "Value Max 100 Juta"
    return hsl

def main(bil):
    if bil<0:
        hsl = "Minus " + nominal(n)
    else:
        hsl = nominal(n)
    return hsl

a=1
while a!= 0:
    n = int(input("Input: "))
    run = main(n)
    print (run)
    continue