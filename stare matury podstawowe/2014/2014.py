# a)
def wielokrotnosci(pairs):
    count = 0
    for pair in pairs:
        if pair[0] % pair[1] == 0 or pair[1] % pair[0] == 0:
            count += 1
    return count

# b)
def pary_liczb_względnie_pierwszych(pairs):
    def nwd(a, b):
        while b:
            a, b = b, a % b
        return a

    count = 0
    for pair in pairs:
        if nwd(pair[0], pair[1]) == 1:
            count += 1
    return count

# c)
def rowne_sumy_cyfr(pairs):
    def suma_cyfr(n):
        return sum(int(i) for i in str(n))

    count = 0
    for pair in pairs:
        if suma_cyfr(pair[0]) == suma_cyfr(pair[1]):
            count += 1
    return count


pary = []
with open("PARY_LICZB.TXT") as file:
    for i in file:
        para = tuple(map(int, i.split()))
        pary.append(para)


with open("ZADANIE5.TXT", "w") as file:
    file.write("a) " + str(wielokrotnosci(pary)) + "\n")
    file.write("b) " + str(pary_liczb_względnie_pierwszych(pary)) + "\n")
    file.write("c) " + str(rowne_sumy_cyfr(pary)) + "\n")
