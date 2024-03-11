with open('dane.txt','r') as dane:
    tab = []
    for i in dane:
        tab.append(list(map(int,i.split())))
    print(tab)

def zad1(tab):
    maxim = 0
    minim = 256
    for i in tab:
        for y in i:
            maxim = max(y,maxim)
            minim = min(y,minim)
    print(maxim,minim)
zad1(tab)
def zad2(tab):
    def czy_symetria(a):
        for i in range(len(a)):
            if a[i]!=a[-i-1]:
                return False
        return True

    licznik=0
    for i in tab:
        if czy_symetria(i)==False:
            licznik+=1
    print(licznik)
zad2(tab)
def zad3(tab):
    def czy_kontrastujacy(tab,i,y):
        wartosc = tab[i][y]
        if i ==0 and y==0:
            if abs(tab[i+1][y] - wartosc) >128 or abs(tab[i][y+1] - wartosc) > 128:
                return True
        elif i==199 and y==0:
            if abs(tab[i-1][y] - wartosc) >128 or abs(tab[i][y+1] - wartosc) > 128:
                return True
        elif i == 0 and y ==319:
            if abs(tab[i+1][y] - wartosc) >128 or abs(tab[i][y-1] - wartosc) > 128:
                return True
        elif i == 199 and y == 319:
            if abs(tab[i-1][y] - wartosc) >128 or abs(tab[i][y-1] - wartosc) > 128:
                return True
        elif i ==0:
            if abs(tab[i][y-1]-wartosc)>128 or abs(tab[i][y+1]-wartosc)>128 or abs(tab[i+1][y]-wartosc)>128 :
                return True
        elif y==0:
            if abs(tab[i+1][y] - wartosc) > 128 or abs(tab[i-1][y] - wartosc) > 128 or abs(tab[i][y+1] - wartosc) > 128:
                return True
        elif i ==199:
            if abs(tab[i][y-1] - wartosc) > 128 or abs(tab[i - 1][y] - wartosc) > 128 or abs(tab[i][y + 1] - wartosc) > 128:
                return True
        elif y==319:
            if abs(tab[i + 1][y] - wartosc) > 128 or abs(tab[i - 1][y] - wartosc) > 128 or abs(tab[i][y - 1] - wartosc) > 128:
                return True
        else:

            if abs(tab[i + 1][y] - wartosc) > 128 or abs(tab[i - 1][y] - wartosc) > 128 or abs(tab[i][y+1] - wartosc) > 128 or abs(tab[i][y-1] - wartosc) > 128:
                return True
        return False
    licznik = 0
    for i in range(len(tab)):
        for y in range(len(tab[i])):
            if czy_kontrastujacy(tab,i,y)==True:
                licznik+=1
    print(licznik)
zad3(tab)
def zad4(tab):
    najdluzsza = 0
    for i in range(320):
        tymczasowa = 1
        for y in range(200-1):
            if tab[y][i] ==tab[y+1][i]:
                tymczasowa+=1
            else:
                najdluzsza=max(tymczasowa,najdluzsza)
                tymczasowa=1
    print(najdluzsza)
zad4(tab)
