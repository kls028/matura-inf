with open('dane.txt', 'r')as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip())
    #print(tab)
def zad1(tab):
    slowo_max_wyst= ""
    max_wyst=0
    licznik=0
    slownik = {}
    for i in tab:
        if i in slownik.keys():
            slownik[i]+=1
        else:
            slownik[i]=1
    for i in slownik.items():
        if i[1]>1:
            licznik+=1
            if i[1]>max_wyst:
                max_wyst=i[1]
                slowo_max_wyst=i[0]
    print(licznik,slowo_max_wyst,max_wyst)
zad1(tab)
def zad2(tab):
    licznik = 0
    for i in tab:
        i = int(i,16)
        if i%2==0:
            licznik+=1
    print(licznik)
zad2(tab)
def zad3(tab):
    def czyPalindrom(a):
        if a == a[::-1]:
            return True
        return False
    licznik = 0
    for i in tab:
        if czyPalindrom(i)== True:
            licznik+=1
    print(licznik)
zad3(tab)