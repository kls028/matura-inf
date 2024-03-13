with open('dane_6.txt','r')as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(int(i.strip()))
    print(tab)

def czyPierwsza(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a %i==0:
            return False
    return True

def zad1(tab):
    licznik = 0
    for i in tab:
        if czyPierwsza(i)==True:
            licznik+=1
    print(licznik)
def zad2(tab):
    pierwsze = []
    for i in tab:
        if czyPierwsza(i)==True:
            pierwsze.append(i)
    print(max(pierwsze),min(pierwsze))
def zad3(tab):
    pary = []
    ilosc = 0
    for i in range(len(tab)-1):
        if czyPierwsza(tab[i]) ==True and czyPierwsza(tab[i+1])==True:
                if abs(tab[i]-tab[i+1])==2:
                    pary.append([tab[i],tab[i+1]])
                    ilosc+=1
    print(f'{ilosc}, {pary}')
zad1(tab)
zad2(tab)
zad3(tab)
