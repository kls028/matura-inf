import pprint as pp
with open('gra.txt', 'r')as dane:
    dane = dane.readlines()
    tab=[]
    tab1=[]
    for i in dane:
        tab.append(i.strip())
    for i in tab:
        tab_tym = []
        for y in i:
            tab_tym.append(y)
        tab1.append(tab_tym)
    print(tab1)
tab2= tab1
#X - żywa      . - martwa
#żywa jeśli
# -żyje ma 2 lub 3 sąsiadów żywych
# -martwa ale ma 3 sasiadów żywych


def zlicz_sasiadow(tab,y,z):
    licznik = 0
    indeks_wiersz_dol=y+1
    indeks_wiersz_gora = y - 1
    indeks_kolumna_prawo = z + 1
    indeks_kolumna_lewo = z - 1

    #kontrola wychodzenia za obszar
    if y+1==12:
        indeks_wiersz_dol=0
    elif y-1==-1:
        indeks_wiersz_gora=11
    if z+1 ==20:
        indeks_kolumna_prawo=0
    elif z-1==-1:
        indeks_kolumna_lewo = 19
    #warunki
    if tab[indeks_wiersz_dol][z] == "X": licznik += 1
    if tab[indeks_wiersz_dol][indeks_kolumna_prawo] == "X": licznik += 1
    if tab[indeks_wiersz_dol][indeks_kolumna_lewo] == "X": licznik += 1
    if tab[indeks_wiersz_gora][z] == "X": licznik += 1
    if tab[indeks_wiersz_gora][indeks_kolumna_prawo] == "X": licznik += 1
    if tab[indeks_wiersz_gora][indeks_kolumna_lewo] == "X": licznik += 1
    if tab[y][indeks_kolumna_prawo] == "X": licznik += 1
    if tab[y][indeks_kolumna_lewo] == "X": licznik += 1
    return licznik

#37 pokolenie
def symulacja(tab,n):
    tab_wynik = tab.copy()
    for i in range(n):
        tab_new = tab_wynik
        for y in range(12):
            for z in range(20):
                if tab_wynik[y][z]=="X":
                    if zlicz_sasiadow(tab_wynik,y,z)==2 or zlicz_sasiadow(tab_wynik,y,z)==3:
                        tab_new[y][z]="X"
                    else:
                        tab_new[y][z] = "."
                elif tab_wynik[y][z]=="." and zlicz_sasiadow(tab_wynik,y,z)==3:
                    tab_new[y][z] = "X"
                else:
                    tab_new[y][z] = "."
        tab_wynik=tab_new
    return tab_wynik
def zad2(tab1): # o jeden za dużo ???
    wynik_2 = symulacja(tab1,2)
    print(wynik_2)
    suma= 0
    for i in wynik_2:
        for y in i:
            if y =='X':
                suma+=1
    print(suma)

def zad1(tab1): #działa
    wynik_37 = symulacja(tab1,37)
    print(zlicz_sasiadow(wynik_37,1,18))
#zad1(tab1)
zad2(tab1)
#zad3???
