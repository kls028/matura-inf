with open('liczby.txt', 'r')as dane:
    tab=[]
    dane= dane.readlines()
    for i in dane:
        tab.append(i.strip())
print(tab)
#1
licznik = 0
for i in tab:
    if int(i,2) %2 ==0:
        licznik+=1
print(licznik)
#2
max_dec = 0
max_bin = ''
for i in tab:
    if int(i,2) > max_dec:
        max_dec = int(i,2)
        max_bin = i
print(max_bin,max_dec)
#3
licznik = 0
suma = 0
for i in tab:
    if len(i)==9:
        licznik+=1
        suma+=int(i,2)
print(licznik,str(bin(suma))[2:])