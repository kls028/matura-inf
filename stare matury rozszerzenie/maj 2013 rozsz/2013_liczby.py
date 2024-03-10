with open('dane.txt', 'r') as plik:
    tab = []
    a = plik.readlines()
    for i in a:
        tab.append(i.strip())
    tab1 = list(map(int,tab))
    print(tab)
def zad1(tab):
    licznik = 0
    for i in tab:
        if i[0]==i[-1]:
            licznik+=1
    print(licznik)
zad1(tab)
def zad2(tab):
    def oct_to_dec(n):
        a = []
        while n:
            a.append(n % 10)
            n //= 10
        liczba = 0
        for i in range(len(a)):
            liczba+=a[i]*8**(i)
        return liczba
    licznik = 0
    for i in tab:
        a = str(oct_to_dec(int(i)))
        if a[0] == a[-1]:
            licznik += 1
    print(licznik)
zad2(tab)
def zad3(tab):
    def czyCyfryNiemalejace(n):
        a = []
        while n:
            a.append(n % 10)
            n //= 10
        for i in range(1,len(a)):
            if a[i]>a[i-1]:
                return False
        return True
    minim = 2000000
    maksym = 0
    licznik = 0
    for i in tab:
        if czyCyfryNiemalejace(i):
            #print(i)
            licznik+=1
            if maksym<i:
                maksym=i
            elif i<minim:
                minim=i
    print(licznik,minim,maksym)
zad3(tab1)
