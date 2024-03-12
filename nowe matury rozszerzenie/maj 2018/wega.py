with open('sygnaly.txt','r')as dane:
    tab=[]
    for i in dane:
        tab.append(i.strip())
    #print(tab)
def zad1(tab):
    przeslanie = ""
    for i in range(39,len(tab),40):
        przeslanie+=tab[i][9]
    print(przeslanie)
def zad2(tab):
    maxi = 0
    slowo_max=""
    for i in tab:
        slownik = {}
        for y in i:
            if y not in slownik.keys():
                slownik[y]=1
        if len(slownik)>maxi:
            maxi = len(slownik)
            slowo_max=i
    print(slowo_max,maxi)
def zad3(tab):
    def czy_oddalone_o_10(a):
        for i in range(len(a)-1):
            if abs(ord(a[i])-ord(a[i+1]))>10:
                return False
        return True
    lista = []
    for i in tab:
        if czy_oddalone_o_10(i)==True:
            lista.append(i)
    print(lista)
zad1(tab)
zad2(tab)
zad3(tab)