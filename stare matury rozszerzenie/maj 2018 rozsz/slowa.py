with open('slowa.txt') as dane:
    tab = []
    tab_p = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip().split())
    for i in dane:
        i = i.strip().split()
        for y in i:
            tab_p.append(y)
    print(tab)
    print(tab_p)
def zad_1(tab_p):
    licznik = 0
    for i in tab_p:
        if i[-1] == "A":
            licznik+=1
    print(licznik)
zad_1(tab_p)
def zad2(tab):
    licznik = 0
    for i in tab:
        if i[0] in i[1]:
            licznik+=1
    print(licznik)
zad2(tab)
def zad3(tab):
    def czyAnagram(a, b):
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        return sorted_a == sorted_b
    licznik = 0
    pary_anagramow = []
    for i in tab:
        if czyAnagram(i[0], i[1]):
            licznik += 1
            pary_anagramow.append((i[0], i[1]))
    print(licznik,pary_anagramow)
zad3(tab)