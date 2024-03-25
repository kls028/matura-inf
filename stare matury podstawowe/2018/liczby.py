with open('liczby.txt','r')as dane:
    tab = []
    for i in dane:
        tab.append(i.strip())
def zad1(tab):
    maxi = 0
    for i in tab:
        if int(i)%2==0:
            maxi=max(maxi,int(i))
    print(maxi)
zad1(tab)
def zad2(tab):
    palind = []
    for i in tab:
        if i == i[::-1]:
            palind.append(i)
    print(palind)
zad2(tab)
def zad3(tab):
    def suma_cyfr(a):
        suma = 0
        while a>0:
            suma+= a%10
            a//=10
        return suma
    wieksze_niz_30= []
    for i in tab:
        if suma_cyfr(int(i))>30:
            wieksze_niz_30.append(i)
    print(wieksze_niz_30)
zad3(tab)
