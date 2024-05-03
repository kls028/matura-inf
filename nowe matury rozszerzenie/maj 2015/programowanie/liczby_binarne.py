with open('liczby.txt','r') as dane:
    tab = []
    for i in dane:
        tab.append(i.strip())

def zad1(tab):
    licznik = 0
    for i in tab:
        zera = i.count('0')
        jedynki = i.count('1')
        if zera>jedynki:
            licznik+=1
    print(licznik)
zad1(tab)
def zad2(tab):
    ile_parzystych = 0
    ile_przez_8 = 0
    for i in tab:
        if int(i,2)%2==0:
            ile_parzystych+=1
            if int(i,2)%8==0:
                ile_przez_8+=1
    print(ile_parzystych,ile_przez_8)
zad2(tab)
def zad3(tab):
    min_wiersz=0
    min_wart=100000000000000000000000000000000000000000000000
    max_wiersz=0
    max_wart=0
    for i in range(len(tab)):
        if int(tab[i],2)<min_wart:
            min_wart=int(tab[i],2)
            min_wiersz = i
        elif int(tab[i],2)>max_wart:
            max_wart=int(tab[i],2)
            max_wiersz=i
    print(min_wiersz+1,max_wiersz+1)#numeracja zaczyna się od 1 a nie 0
zad3(tab)