with open('dane5-1.txt', 'r') as dane1:
    tab1 = []
    dane=dane1.readlines()
    for i in dane:
        tab1.append(int(i.strip()))
with open('dane5-2.txt', 'r') as dane2:
    tab2 = []
    dane=dane2.readlines()
    for i in dane:
        tab2.append(int(i.strip()))
with open('dane5-3.txt', 'r') as dane3:
    tab3 = []
    dane=dane3.readlines()
    for i in dane:
        tab3.append(int(i.strip()))
def najlepsza_suma(a):
    naj_suma = 0
    for i in range(len(a)):
        current_suma = 0
        for y in range(i,len(a)):
            current_suma+=a[y]
            if current_suma>naj_suma:
                naj_suma = current_suma
    print(naj_suma)
najlepsza_suma(tab1)
najlepsza_suma(tab2)
najlepsza_suma(tab3)
def najpopularniejszy_element(a):
    max_licznik = 0
    liczby_max = []
    slownik = {}
    for i in a:
        if i in slownik.keys():
            slownik[i]+=1
        else:
            slownik[i]=1
    maxim = max(slownik.values())
    tab = sorted(slownik.items(),key= lambda x: x[1],reverse=True)

    for i in tab:
        if i[1] ==maxim:
            liczby_max.append(i[0])
    print(liczby_max)
najpopularniejszy_element(tab1)
najpopularniejszy_element(tab2)
najpopularniejszy_element(tab3)


