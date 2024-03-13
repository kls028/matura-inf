
with open("napisy.txt") as f:
    lines = f.readlines()


parzysta_dl = 0
rowno_zera_jedynki = 0
tylko_zera = 0
tylko_jedynki = 0
dlugosc_k = [0] * 15


for line in lines:
    dl = len(line.strip())
    zera = line.count("0")
    jedynki = line.count("1")


    if dl % 2 == 0:
        parzysta_dl += 1
    if zera == jedynki:
        rowno_zera_jedynki += 1
    if zera == dl:
        tylko_zera += 1
    if jedynki == dl:
        tylko_jedynki += 1
    dlugosc_k[dl-2] += 1


with open("zadanie4.txt", "w") as f:

    f.write("a) Ilość napisów o parzystej długości: {}\n".format(parzysta_dl))
    f.write("b) Ilość napisów zawierających taką samą liczbę zer i jedynek: {}\n".format(rowno_zera_jedynki))
    f.write("c) Ilość napisów składających się z samych zer: {}\n".format(tylko_zera))
    f.write("c) Ilość napisów składających się z samych jedynek: {}\n".format(tylko_jedynki))
    for i in range(2, 17):
        f.write("d) Ilość napisów o długości {}: {}\n".format(i, dlugosc_k[i-2]))
