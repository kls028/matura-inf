def suma_cyfr(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

def czy_rosna(n):
  cyfra_przed = n % 10
  n //= 10
  while n > 0:
    cyfra_po = n % 10
    if cyfra_po >= cyfra_przed:
      return False
    cyfra_przed = cyfra_po
    n //= 10
  return True


with open("cyfry.txt") as f:
  numbers = [int(line.strip()) for line in f]

parzyste = len([x for x in numbers if x % 2 == 0])


max_sum = max(numbers, key=suma_cyfr)
min_sum = min(numbers, key=suma_cyfr)


rosnace = [x for x in numbers if czy_rosna(x)]

with open("zadanie4.txt", "w") as f:
  f.write(f"a) Ilość liczb parzystych: {parzyste}\n")
  f.write(f"b) Największa suma cyfr: {max_sum}, Najmniejsza suma cyfr: {min_sum}\n")
  f.write("c) Liczby z ciągiem rosnącym:\n")
  for x in rosnace:
    f.write(f"{x}\n")
