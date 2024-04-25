with open('slowa.txt','r') as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip())


def zad1(tab):
    slowa = []
    for i in tab:
        if i.count('w') == i.count('k'):
            slowa.append(i)
    print(slowa)
zad1(tab)
def zad2(tab):
    ile = []
    for i in tab:
        ilosc = 0
        slownik = {'w':0,'a':0,'k':0,'c':0,'j':0,'e':0}
        for y in i:
            if y in slownik.keys():
                slownik[y]+=1
        if min(slownik.values())==0:
            ilosc = 0
        elif slownik['a']>=2*min(slownik.values()):
            ilosc=min(slownik.values())
        else:
            maxi = 0
            for i in range(0,min(slownik.values())+1):
                if i*2<=slownik['a']:
                    maxi= max(i,maxi)
            ilosc=maxi

        ile.append(ilosc)
    print(ile)
zad2(tab)


#nowe_slowo = ""
#litery = ["w","a","k","a","c","j","e"]
#while len(slowo)>0:
#    if slowo[0] in litery:
#        if slowo[0]==slowo[1]:
#            licznik=1
#            for y in range(len(slowo) - 1):
#                if slowo[y]==slowo[y+1]:
#                    licznik+=1
#                else:
#                    break
#            nowe_slowo+=slowo[0]
#            slowo = slowo[licznik:]
#
#        else:
#            nowe_slowo += slowo[0]
#            slowo=slowo[1:]
#    else:
#        slowo = slowo[1:]
#
#print(nowe_slowo)
def zad3(tab):
    def najmniejsze(slowo):
        litery = ["w","a","k","a","c","j","e"]
        wzor = "wakacje"
        nowe=""
        j=0
        for i in range(len(slowo)):
            if slowo[i]==wzor[j%7]:
                nowe+=slowo[i]
                j+=1
            else:
                continue
        dodatkowe_usuniecia = len(nowe) - nowe.count('wakacje')*7
        return (len(slowo)-len(nowe)+dodatkowe_usuniecia)
    ile_wykreslic = []
    for i in tab:
        ile_wykreslic.append(najmniejsze(i))
    print(ile_wykreslic)
zad3()
