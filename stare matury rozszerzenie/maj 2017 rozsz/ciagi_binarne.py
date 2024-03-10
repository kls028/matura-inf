with open('binarne.txt','r')as dane:
    tab=[]
    dane=dane.readlines()
    for i in dane:
        tab.append(i.strip())
def zad1(tab):
    def czy_dwucykliczny(a):
        dl = len(a)
        if a[:dl//2]==a[dl//2:]:
            return True
        return False
    licznik = 0
    max_dl = 0
    max_dl_napis = ''
    for i in tab:
        if czy_dwucykliczny(i)==True:
            licznik+=1
            if len(i)>max_dl:
                max_dl=len(i)
                max_dl_napis=i
    print(licznik,max_dl_napis,max_dl)
zad1(tab)
def zad2(tab):
    def czy_niepoprawny(a):
        segmenty = len(a)/4
        seg_tab= []
        for i in range(0,len(a),4):
            seg_tab.append(a[i:i+4])
        for i in seg_tab:
            if int(i,2)>9:
                return True
        return False
    licznik = 0
    min_dl = 100000000000000000000000000000000000
    for i in tab:
        if czy_niepoprawny(i)==True:
            licznik+=1
            if len(i)<min_dl:
                min_dl=len(i)
    print(licznik,min_dl)
zad2(tab)
def zad3(tab):
    max_liczba = 0
    max_liczba_bin=0
    for i in tab:
        if int(i,2)<=65535:
            if int(i,2) >max_liczba:
                max_liczba=int(i,2)
                max_liczba_bin = i
    print(max_liczba_bin,max_liczba)
#11 minut