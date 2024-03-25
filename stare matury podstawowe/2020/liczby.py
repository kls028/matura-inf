with open('liczby.txt','r')as dane:
    tab=[]
    dane=dane.readlines()
    for i in dane:
        tab.append(i.strip())

def zad1(tab):
    ile_np = 0
    for i in range(len(tab)):
        if int(tab[i])%2==1:
            ile_np+=1
    print(ile_np)
zad1(tab)
def zad2(tab):
    suma_11 = []
    def suma_cyfr(a):
        suma = 0
        while a>0:
            suma+=a%10
            a//=10
        return suma
    for i in tab:
        if suma_cyfr(int(i))==11:
            suma_11.append(i)
    print(suma_11)
zad2(tab)
def zad3(tab):
    def czy_pierwsza(a):
        for i in range(2,int(a**0.5)+1):
            if a%i == 0:
                return False
        return True
    lista= []
    for i in tab:
        if czy_pierwsza(int(i)) == True:
            if int(i)<=5000 and int(i)>=4000:
                lista.append(i)
    print(lista)
zad3(tab)