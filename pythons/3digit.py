n = int(input("Masukkan bilangan 3 digit: "))

r = n // 100
p = (n % 100) // 10
s = n % 10

print(f"Bilangan {n} = {r*100} + {p*10} + {s}")