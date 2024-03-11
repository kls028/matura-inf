with open('dane_6_1.txt','r')as dane1:
    tab1=[]
    for i in dane1:
        tab1.append(i.strip())
    #print(tab1)
with open('dane_6_2.txt','r')as dane2:
    tab2=[]
    for i in dane2:
        tab2.append(i.strip().split())
    #print(tab2)
with open('dane_6_3.txt','r')as dane3:
    tab3=[]
    for i in dane3:
        tab3.append(i.strip().split())
    #print(tab3)
def zad1(tab1):
    def szyfrowanie(a,k):
        nowe=""
        for i in a:
            k=k%26
            litera = ord(i)+k
            if litera>90:
                litera=litera%90+64
            nowe+=chr(litera)
        return nowe
    lista=[]
    for i in tab1:
        lista.append(szyfrowanie(i,107))
    print(lista)
def zad2(tab2):
    def odszyfrowanie(a,k):
        nowe=""
        for i in a:
            k%=26
            litera=ord(i)-k
            if litera<65:
                litera=91-(65-litera)
            nowe+=chr(litera)
        return nowe

    lista=[]

    for i in tab2:
        lista.append(odszyfrowanie(i[0],int(i[1])))

#zad2(tab2) przy zadaniu nr 2 występuje chyba błąd ze strony autorów -
#niektóre wiersze nie mają kluczy!!!

def zad3(tab3):
    def czy_bledne(a,b):
        klucze=[]
        for i in range(len(a)):
            l1=ord(a[i])
            l2=ord(b[i])
            if l2<l1:
                klucze.append(l2-65+91-l1)
            else:
                klucze.append(l2-l1)
        for i in range(len(klucze)-1):
            if klucze[i]!=klucze[i+1]:
                return False
        return True
    lista=[]
    for i in tab3:
        if czy_bledne(i[0],i[1])==False:
            lista.append(i[0])
    print(lista)
zad1(tab1)

zad3(tab3)

