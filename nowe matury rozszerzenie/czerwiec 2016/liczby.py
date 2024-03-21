with open("liczby.txt","r")as dane:
    tab= []
    for i in dane:
        tab.append(i.strip())
    print(tab)
def zad1(tab):
    licznik = 0
    for i in tab:
        if i[-1]=="8":
            licznik+=1
    print(licznik)
zad1(tab)
def zad2(tab):
    licznik = 0
    for i in tab:
        if i[-1]=="4":
            if "0" not in i:
                licznik+=1
    print(licznik)
zad2(tab)
def zad3(tab):
    licznik = 0
    for i in tab:
        if i[-1] == "2":
            liczba = int(i[:-1],2)
            if liczba%2==0:
                licznik+=1
    print(licznik)
zad3(tab)
def zad4(tab):
    suma = 0
    for i in tab:
        if i[-1]=="8":
            liczba = int(i[:-1],8)
            suma+=liczba
    print(suma)
zad4(tab)
def zad5(tab):
    min_l = 10000000000000000000000000000000000000
    max_l = 0
    kod_max = ""
    kod_min = ""
    for i in tab:
        liczba = int(i[:-1],int(i[-1]))
        if liczba > max_l:
            kod_max = i
            max_l = liczba
        if liczba < min_l:
            kod_min = i
            min_l = liczba
    print(kod_min,int(kod_min[:-1],int(kod_min[-1])))
    print(kod_max, int(kod_max[:-1], int(kod_max[-1])))
zad5(tab)
