with open("dane.txt","r")as dane:
    tab= []
    for i in dane:
        tab.append(i.strip())

def zad1(tab):
    kobiety=0
    mezczyzni = 0
    for i in tab:
        if int(i[-2])%2==0:
            kobiety+=1
        else:
            mezczyzni+=1
    print(kobiety, mezczyzni)
zad1(tab)
def zad2(tab):
    ile_listopad = 0
    for i in tab:
        msc = int(i[2:4])
        if msc>20:
            msc-=20
        if msc == 11:
            ile_listopad+=1
    print(ile_listopad)
zad2(tab)
def zad3(tab):
    def czy_poprawny(a):
        suma=0
        for i in range(len(a)-1):
            if (i+1)%4==1:
                suma+=int(a[i])
            elif (i+1)%4==2:
                suma += int(a[i]) * 3
            elif (i + 1) % 4 == 3:
                suma += int(a[i]) * 7
            elif (i + 1) % 4 == 0:
                suma+=int(a[i])*9
        suma+=int(a[-1])
        if suma%10!=0:
            return False
        return True
    niepoprawne = []
    for i in tab:
        if czy_poprawny(i) == False:
            niepoprawne.append(i)
    print(niepoprawne)
zad3(tab)