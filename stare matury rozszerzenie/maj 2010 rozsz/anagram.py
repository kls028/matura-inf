with open('anagram.txt', 'r')as dane:
    tab = []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.strip().split(" "))
print(tab)
def zad1(tab):
    wiersze = []
    for i in tab:
        dl = len(i[0])
        licznik = 0
        for y in i:
            if len(y)==dl:
                licznik+=1
        if licznik==5:
            wiersze.append(i)
    print(wiersze)

def czyAnagram(a):
    tab=[]
    for i in a:
        tab.append("".join(sorted(i)))
    dl = len(tab[0])
    for i in range(1,len(tab)):
        if len(tab[i]) != dl:
            return False
        else:
            if tab[i]!=tab[i-1]:
                return False
    return True
wiersze = []
for i in tab:
    if czyAnagram(i)==True:
        wiersze.append(i)
print(wiersze)
