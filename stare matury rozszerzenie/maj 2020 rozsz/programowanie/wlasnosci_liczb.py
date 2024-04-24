with open('dane.txt','r') as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(int(i.strip()))

def zad1(tab):
    def czy_pierwsza(a):
        if a<=1:
            return False
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
    min_liczba = 1000000000
    max_liczba = 0
    licznik=0
    for i in tab:
        if czy_pierwsza(i)==True:
            licznik+=1
            min_liczba=min(min_liczba,i)
            max_liczba=max(max_liczba,i)
    print(licznik,max_liczba,min_liczba)
def zad2(tab):
    def czy_palindrom(a):
        b2= bin(a)[2:]
        if b2[0] == "1":
            if b2==b2[::-1]:
                return "palindromiczna"
            else:
                dl = len(b2)
                licznik=0
                i = 1
                kontrolna =0
                while kontrolna!= -1:
                    if b2[-i]=="0":
                        licznik+=1
                        i +=1
                    else:
                        kontrolna = -1
                nowy = "0"*licznik+b2
                if nowy == nowy[::-1]:
                    return "prawie palindromiczna"
                else:
                    return False
    pal = 0
    prawie_pal = 0
    for i in tab:
        if czy_palindrom(i)=='prawie palindromiczna':
            prawie_pal+=1
        elif czy_palindrom(i)=='palindromiczna':
            pal+=1
    print(pal+prawie_pal)

def zad3(tab):
    unikalne = set()
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            if set(str(tab[i])) == set(str(tab[j])):
                para = tuple(sorted([tab[i],tab[j]]))
                unikalne.add(para)
    print(len(unikalne))
