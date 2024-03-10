with open('NAPIS.TXT', 'r') as plik:
    tab = []
    a = plik.readlines()
    for i in a:
        tab.append(i.strip())
    print(tab)
def zad1(tab):
    def czyPierwsza(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5)+1):
            if n%i== 0:
                return False
        return True
    licznik = 0
    for i in tab:
        suma = 0
        for y in i:
            suma+=ord(y)
        if czyPierwsza(suma):
            licznik +=1
    print(licznik)
zad1(tab)
def zad2(tab):
    def czyNapisPierwszy(a):
        for i in range(1,len(a)):
            #print(a[i])
            if ord(a[i])<=ord(a[i-1]):
                return False
        return True
    lista = []
    for i in tab:
        if czyNapisPierwszy(i):
            lista.append(i)
    print(lista)
zad2(tab)
def zad3(tab):
    s = {}
    lista=[]
    for i in tab:
        if i not in s:
            s[i] = 1
        else:
            s[i]+=1
    for i,y in s.items():
        if y != 1:
            lista.append(i)
    print(lista)
zad3(tab)