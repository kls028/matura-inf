with open("liczby.txt",'r')as dane:
    tab = []
    dane= dane.readlines()
    for i in dane:
        tab.append(i.strip())
    print(tab)
def zad1(tab):
    pierwsza = "a"
    licznik= 0
    for i in tab:
        if i[0]==i[-1]:
            licznik+=1
            if pierwsza =="a":
                pierwsza = i
    print(licznik, pierwsza)
zad1(tab)
def zad2(tab):
    def rozklad(n):
        czynniki = []
        dzielnik = 2
        while n>1:
            if n%dzielnik !=0:
                dzielnik+=1
            else:
                czynniki.append(dzielnik)
                n //= dzielnik

        return czynniki
    liczba_czyn =0
    liczba_czyn_s=0
    max_czyn = 0
    max_czyn_s=0
    for i in tab:
        czyn = rozklad(int(i))
        czyn_s = set(czyn)
        if len(czyn)>max_czyn:
            max_czyn = len(czyn)
            liczba_czyn = i
        if len(czyn_s) > max_czyn_s:
            max_czyn_s = len(czyn_s)
            liczba_czyn_s = i
    print(liczba_czyn,max_czyn,liczba_czyn_s,max_czyn_s)
zad2(tab)

tab = list(map(int, tab))
dobre_trojki_licz = 0
dobre_trojki = []
dobre_piatki_licz = 0
for x in range(len(tab)):
    for y in range(len(tab)):
        if x  == y:
            continue
        else:
            for z in range(len(tab)):
                if x ==z or y==z:
                    continue
                else:
                    if tab[y]%tab[x] ==0 and tab[z]%tab[y]==0:
                        dobre_trojki_licz+=1
                        dobre_trojki.append([tab[x],tab[y],tab[z]])
                    #rozw dla piatek dobre, ale zbyt zlozone obliczeniowo
                    #for u in range(len(tab)):
                    #    if x==u or y==u or z==u:
                    #        continue
                    #    else:
                    #        for w in range(len(tab)):
                    #            if x == w or y == w or z == w or u==w:
                    #                continue
                    #            else:
                    #                if tab[y] % tab[x] == 0 and tab[z] % tab[y] == 0 and tab[u] % tab[z] == 0 and tab[w] % tab[u] == 0:
                    #                    dobre_piatki_licz+=1
print(dobre_trojki_licz)
print(dobre_trojki)
print(dobre_piatki_licz)
