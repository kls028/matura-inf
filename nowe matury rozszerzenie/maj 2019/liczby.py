with open('liczby.txt', 'r') as plik:
    tab = []
    a = plik.readlines()
    for i in a:
        tab.append(i.strip())
tab = list(map(int,tab))
def zad1(tab):
    def czy_potega_trzy(n):
        while n>1:
            if n%3 !=0:
                return False
            n//=3
        if n==1:
            return True
    #print(czy_potega_trzy(28))
    licznik = 0
    for i in tab:
        if czy_potega_trzy(i):
            licznik +=1
    print(licznik)
zad1(tab)
def zad2(tab):
    def suma_silni_cyfr(n):
        def silnia(n):
            if n == 0:
                return 1
            else:
                return silnia(n - 1) * n
        a = 0
        c = n
        while n:
            a+=silnia(n%10)
            n //= 10
        return a == c
    lista=[]
    for i in tab:
        if suma_silni_cyfr(i):
            lista.append(i)
    print(lista)
zad2(tab)
def zad3(tab):
    def nwd(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    max_dl_ciagu = 0
    max_nwd = 0
    # aktualna_dl_ciagu = 1
    max_pierwsza = 0
    for i in range(0, len(tab) - 1):
        aktualna_dl_ciagu = 1
        aktualne_nwd = tab[i]
        aktualna_pierwsza_liczba_ciagu = tab[i]
        lista_nwd = []
        for y in range(i + 1, len(tab)):
            if nwd(aktualne_nwd, tab[y]) > 1:
                aktualne_nwd = nwd(tab[y], aktualne_nwd)
                aktualna_dl_ciagu += 1
                if aktualna_dl_ciagu > max_dl_ciagu:
                    max_dl_ciagu = aktualna_dl_ciagu
                    max_nwd = aktualne_nwd
                    max_pierwsza = aktualna_pierwsza_liczba_ciagu
            else:
                break

    print(max_pierwsza, max_dl_ciagu, max_nwd)
zad3(tab)