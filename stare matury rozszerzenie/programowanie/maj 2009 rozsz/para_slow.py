with open('dane.txt', 'r')as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip().split())
print(tab)
def zad1(tab):
    licznik = 0
    for i in tab:
        for y in i:
            if y==y[::-1]:
                licznik+=1
    print(licznik)
def zad2(tab):
    licznik = 0
    for i in tab:
        if i[1] in i[0]:
            licznik+=1
    print(licznik)
def najkrotsze_slowo(para):
    a = para[0]
    b = para[1]
    if b in a:
        return a
    else:
        dl=len(b)
        slowo_min = a+b
        for i in range(dl):
            if b[i:] == a[:len(b[i:])]:
                if len( b[:i]+a)<len(slowo_min):
                    slowo_min =b[:i]+a
        for i in range(dl):
            if b[:i]== a[len(a)-len(b[:i]):]:
                if len(a+b[i:])<len(slowo_min):
                    slowo_min = a+b[i:]
        return slowo_min
def zad3(tab):
    licznik=0
    for i in tab:
        if najkrotsze_slowo(i)==i[0]+i[1]:
            licznik+=1
    print(licznik)
def zad4(tab):
    najkrotsze = []
    for i in tab:
        najkrotsze.append(najkrotsze_slowo(i))
    print(najkrotsze)