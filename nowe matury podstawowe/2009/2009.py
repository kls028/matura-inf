
def czy_pierwsza(n):
  for i in range(2,int(n**0.5)+1):
    if (n%i) == 0:
      return False
  return True
print(czy_pierwsza(1369))

with open("liczby.txt") as file:
    num = file.readlines()
    num = [int(x.strip()) for x in num]
    prime_sq=[]
    for x in num:
        a = int(x**0.5)
        if czy_pierwsza(a) == True:
            prime_sq.append(str(x) + "\n" )


with open("kwadraty_pierwszych.txt", "w") as file:
    file.writelines(prime_sq)
