with open('slowa.txt', 'r')as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip())

def zad1(tab):
    jednorazowe = []
    najw_haslo=""
    najw_dl = 0
    najm_haslo = ""
    najm_dl = 31
    for i in tab:
        jednorazowe.append(i[::-1])
        if len(i)>najw_dl:
            najw_dl=len(i)
            najw_haslo=i
        elif len(i)<najm_dl:
            najm_dl=len(i)
            najm_haslo=i
    print(jednorazowe)
    print("a: ",najw_haslo,najw_dl,najm_haslo,najm_dl)
zad1(tab)
def tworzenie_hasła(a):
    if a == a[::-1]:
        return a
    else:
        max_dl = 0
        naj_slowo = ""
        indeks = 0
        for y in range(1,len(a)+1):
            slowo=a[:y]
            if slowo==slowo[::-1]:
                if max_dl<len(slowo):
                    naj_slowo = slowo
                    max_dl = len(slowo)
                    indeks=y
        return a[indeks:][::-1]+naj_slowo+a[indeks:]
jednorazowe = []
hasla_12 = []
najkrotsze = ""
min_dl=31
max_dl=0
najdluzsze = ""
suma_dl = 0
for i in tab:
    haslo = tworzenie_hasła(i)
    jednorazowe.append(haslo)
    if len(haslo)==12:
        hasla_12.append(haslo)
    if len(haslo)<min_dl:
        min_dl=len(haslo)
        najkrotsze=haslo
    elif len(haslo)>max_dl:
        max_dl=len(haslo)
        najdluzsze=haslo
    suma_dl+=len(haslo)
print(jednorazowe)
print("b: ",hasla_12,najdluzsze,najkrotsze,suma_dl)