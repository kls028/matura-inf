with open('pi.txt','r')as dane:
    tab=[]
    for i in dane:
        tab.append(i.strip())
    print(tab)
def zad1(tab):
    licznik=0
    for i in range(len(tab)-1):
        if int(tab[i]+tab[i+1])>90:
            licznik+=1
    print(licznik)
zad1(tab)
def zad2(tab):
    slownik={}
    for i in range(len(tab)-1):
        if tab[i]+tab[i+1] not in slownik.keys():
            slownik[tab[i]+tab[i+1]]=1
        else:
            slownik[tab[i] + tab[i + 1]] += 1
    posortowane=sorted(slownik.items(),key=lambda x: x[1])
    minim=posortowane[0][1]
    maxim=posortowane[-1][1]
    min_tab=[]
    max_tab=[]
    for i in posortowane:
        if i[1]==minim:
            min_tab.append(i)
        elif i[1]==maxim:
            max_tab.append(i)
    print(min_tab)
    print(max_tab)
zad2(tab)


def czy_rosnaco_malejacy(ciag):
    licznik_r=1
    for i in range(len(ciag)-1):
        if ciag[i+1]>ciag[i]:
            licznik_r+=1
        else:
            break
    licznik_m=1
    ciag_mal = ciag[licznik_r:]
    len_malejacy=len(ciag[licznik_r:])
    for i in range(licznik_r,len(ciag)-1):
        if ciag[i]>ciag[i+1]:
            licznik_m+=1
        else:
            break
    if licznik_r + licznik_m == len(ciag) and len(ciag)>=4 and licznik_r>1 and ciag[-1]!=ciag[-2] :
        return True
    return False


def zad3(tab):
    licznik=0

    for i in range(len(tab)-5):

        fragment=tab[i:i+6]

        if czy_rosnaco_malejacy(fragment) ==True:
            #print(fragment)
            licznik+=1
    print(licznik)
zad3(tab)
def zad4(tab):# za dlugo
    dl = [1]*len(tab)
    max_ciag = []
    max_pozycja=0
    for i in range(len(tab)-20):
        for j in range(i+1,i+21):
            if len(tab[i:j])>=4:
                if czy_rosnaco_malejacy(tab[i:j]) == True and len(tab[i:j])>len(max_ciag):
                    max_pozycja=i
                    max_ciag=tab[i:j].copy()
    print(max_ciag)
    print(max_pozycja+1)
zad4(tab)

