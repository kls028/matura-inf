with open('slowa.txt','r')as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip())
    #print(tab)
def zad1(tab):
    slownik ={}
    for i in range(1,13):
        slownik[i]=0
    for i in tab:
        slownik[len(i)]+=1
    print(slownik)
zad1(tab)
with open('nowe.txt','r')as dane:
    tab1 = []
    dane = dane.readlines()
    for i in dane:
        tab1.append(i.strip())
    #print(tab1)
def zad2(tab,tab1):
    lista = []
    lista_lustrzane = []
    for i in tab1:
        lista.append(i)
        lista_lustrzane.append(i[::-1])
    slownik = {}
    slownik_lust={}
    for i in lista:
        slownik[i]=0
    for i in lista_lustrzane:
        slownik_lust[i]=0
    for i in tab:
        if i in slownik.keys():
            slownik[i]+=1
        if i in slownik_lust.keys():
            slownik_lust[i]+=1

    lista_koncowa=[]

    for i in range(len(tab1)):
        lista_koncowa.append([tab1[i]])
    licznik=0
    for i in slownik.items():
        lista_koncowa[licznik].append(i[1])
        licznik+=1
    licznik=0
    for i in slownik_lust.items():
        lista_koncowa[licznik].append(i[1])
        licznik+=1
    print(lista_koncowa)
zad2(tab,tab1)

