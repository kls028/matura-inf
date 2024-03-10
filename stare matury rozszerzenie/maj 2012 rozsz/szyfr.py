with open('tj.txt','r') as dane:
    dane=dane.readlines()
    tekst=[]
    for i in dane:
        tekst.append(i.strip())
with open('klucze1.txt','r') as dane:
    dane=dane.readlines()
    klucze=[]
    for i in dane:
        klucze.append(i.strip())
def zad1(tekst,klucze):
    wynik_szyfrowania = []
    for i in range (len(tekst)):
        litery = ""
        if len(tekst[i])==len(klucze[i]):
            for y in range(len(tekst[i])):
                suma=ord(tekst[i][y])+ord(klucze[i][y])-64
                if suma>90:
                    litery+=chr(suma-26)
                else:
                    litery+=chr(suma)
        else:
            klucz=""
            ile_calosci = len(tekst[i])//len(klucze[i])
            ile_reszt = len(tekst[i])%len(klucze[i])
            klucz+=ile_calosci*klucze[i]
            klucz+=klucze[i][:ile_reszt]
            for y in range(len(tekst[i])):
                suma=ord(tekst[i][y])+ord(klucz[y])-64
                if suma>90:
                    litery+=chr(suma-26)
                else:
                    litery+=chr(suma)
        wynik_szyfrowania.append(litery)
    print(wynik_szyfrowania)
zad1(tekst,klucze)
with open('sz.txt','r') as dane:
    dane=dane.readlines()
    szyfrogram=[]
    for i in dane:
        szyfrogram.append(i.strip())
with open('klucze2.txt','r') as dane:
    dane=dane.readlines()
    klucze=[]
    for i in dane:
        klucze.append(i.strip())
def zad2(szyfrogram,klucze):
    wynik_odszyfrowania = []
    for i in range (len(szyfrogram)):
        litery = ""
        if len(szyfrogram[i])==len(klucze[i]):
            for y in range(len(szyfrogram[i])):
                suma=ord(szyfrogram[i][y])-(ord(klucze[i][y])-64)
                if suma<65:
                    litery+=chr(suma+26)
                else:
                    litery+=chr(suma)
        else:
            klucz=""
            ile_calosci = len(szyfrogram[i])//len(klucze[i])
            ile_reszt = len(szyfrogram[i])%len(klucze[i])
            klucz+=ile_calosci*klucze[i]
            klucz+=klucze[i][:ile_reszt]
            for y in range(len(szyfrogram[i])):
                suma=ord(szyfrogram[i][y])-(ord(klucz[y])-64)
                if suma<65:
                    litery+=chr(suma+26)
                else:
                    litery+=chr(suma)
        wynik_odszyfrowania.append(litery)
    print(wynik_odszyfrowania)
zad2(szyfrogram,klucze)