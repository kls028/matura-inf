with open ('instrukcje.txt','r') as dane:
    tab= []
    dane = dane.readlines()
    for i in dane:
        tab.append(i.split())
    print(tab)
def zad1(tab):
    napis=[]
    for i in tab:
        if i[0]== "DOPISZ":
            napis.append(i[1])
        elif i[0]== "ZMIEN":
            napis[-1] = i[1]
        elif i[0]== "USUN":
            del napis[-1]
        elif i[0]== "PRZESUN":
             poz = napis.index(i[1])

             if i[1] == "Z":
                 napis[poz] = "A"
             else:
                 napis[poz] = chr(ord(napis[poz])+1)
    print(len(napis))
zad1(tab)
def zad2(tab):
    max_dl = 0
    max_op = ""
    dl = 0
    op = ""
    for i in range(len(tab)-1):
        if tab[i][0] ==tab[i+1][0]:
            dl+=1
            op=tab[i][0]
        else:
            if max_dl<dl:
                max_dl=dl
                max_op = op
            dl = 1
            op =""
    print(max_op,max_dl)
zad2(tab)
def zad3(tab):
    slownik = {}
    for i in tab:
        if i[0]== "DOPISZ":
            if i[1] not in slownik.keys():
                slownik[i[1]]=1
            else:
                slownik[i[1]] += 1
    print(sorted(slownik.items(),key= lambda x: x[1],reverse=True)[0])
zad3(tab)
def zad4(tab):
    napis = []
    for i in tab:
        if i[0] == "DOPISZ":
            napis.append(i[1])
        elif i[0] == "ZMIEN":
            napis[-1] = i[1]
        elif i[0] == "USUN":
            del napis[-1]
        elif i[0] == "PRZESUN":
            poz = napis.index(i[1])

            if i[1] == "Z":
                napis[poz] = "A"
            else:
                napis[poz] = chr(ord(napis[poz]) + 1)
    napis_koncowy = ""
    for i in napis:
        napis_koncowy+=i
    print(napis_koncowy)
zad4(tab)