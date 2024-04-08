import pprint
with open('dzialki.txt','r')as dane:
    dzialki = []
    for i in range(50):
        dzialka = []
        for y in range(30):
            dzialka.append(dane.readline().strip())
        dane.readline()
        dzialki.append(dzialka)

def zad1(dzialki):
    licznik_dzialek = 0
    for i in dzialki:
        temp_licznik = 0
        for y in i:
            temp_licznik+=y.count("*")
        if temp_licznik >=630:
            licznik_dzialek+=1
    print(licznik_dzialek)
zad1(dzialki)
def zad2(dzialki):
    numery = []
    for i in range(len(dzialki)):
        zwykla = dzialki[i]
        obrocona = []
        for y in range(len(zwykla)-1,-1,-1):
            obrocona.append(zwykla[y][::-1])
        for x in range(len(dzialki)):
            if obrocona == dzialki[x]:
                numery.append(i+1)
                numery.append(x+1)
        if len(numery)>0:
            break
    print(numery)
zad2(dzialki)
def zad3(dzialki):
    def sprawdz_kwadrat(kwadrat,x,y):
        for i in range(x+1):
            for j in range(y+1):
                if kwadrat[i][j]=="X":
                    return False
        return True
    def najwiekszy_kwadrat(dzialka):
        najwiekszy_wymiar = 0
        for i in range(15):
            for j in range(15):
                wymiar_x=j
                wymiar_y=i
                if wymiar_x == wymiar_y:
                    if sprawdz_kwadrat(dzialka,wymiar_x,wymiar_y) == True:
                        najwiekszy_wymiar=max(wymiar_x,najwiekszy_wymiar)
        return najwiekszy_wymiar
    naj = 0
    naj_indeksy = []

    for i in range(len(dzialki)):
        wymiar = najwiekszy_kwadrat(dzialki[i])+1
        if wymiar > naj:
            naj=wymiar
            naj_indeksy.clear()
            naj_indeksy.append(i+1)
        elif wymiar == naj :
            naj_indeksy.append(i+1)
    print(naj,naj_indeksy)
zad3(dzialki)