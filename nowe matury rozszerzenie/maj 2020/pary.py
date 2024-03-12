with open('pary.txt','r')as dane:
    tab=[]
    dane=dane.readlines()
    for i in dane:
        tab.append(i.strip().split())

def zad1(tab):
    def czyPierwsza(a):
        if a > 1:
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    return False
            return True
        return False
    def goldbach(a):
        if a % 2 == 0 and a > 4:
            maxi = 0
            for i in range(a):
                if czyPierwsza(i) == True and czyPierwsza(a - i) == True:
                    maxi = max(i, maxi)
            return maxi
        else:
            return False

    lista = []
    for i in tab:
        if goldbach(int(i[0]))!=False:
            lista.append([int(i[0]),int(i[0])-goldbach(int(i[0])),goldbach(int(i[0]))])
    print(lista)
def zad2(tab):
    def najdluzszy_ciag(a):
        max_dl=0
        ciag= ""
        temp_ciag=a[0]
        temp_dl = 1
        temp_litera =a[0]
        for i in range(1,len(a)):
           if a[i]==temp_litera:
               temp_ciag+=a[i]
               temp_dl+=1
           else:
               temp_litera=a[i]
               if temp_dl > max_dl:
                   max_dl=temp_dl
                   ciag = temp_ciag
               temp_ciag = a[i]
               temp_dl=1
        if temp_dl > max_dl:
            max_dl = temp_dl
            ciag = temp_ciag
        return [ciag,max_dl]
    lista=[]
    for i in tab:
        lista.append(najdluzszy_ciag(i[1]))
    print(lista)

def zad3(tab):
    def czy_mniejsza(a,b):
        liczba1 = int(a[0])
        slowo1 = a[1]
        liczba2 = int(b[0])
        slowo2 = b[1]
        if liczba2>liczba1 or (liczba2==liczba1 and slowo2>slowo1):
            return True
        return False

    pary=[]
    for i in tab:
        if int(i[0])==len(i[1]):
            pary.append(i)

    para=""
    for i in range(len(pary)):
        znacznik = 0
        for j in range(len(pary)):
            if j!=i and czy_mniejsza(pary[i],pary[j])==False:
                znacznik=1
                break
        if znacznik ==0:
            para = pary[i]
            break
    print(para)
zad1(tab)
zad2(tab)
zad3(tab)