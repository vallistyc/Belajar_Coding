n1 = 65
n2 = 68
n3 = 72
n4 = 75
z = 65 + 22  # z = 87, dari selisih max - min = 22

# Input x dengan validasi
while True:
    x = int(input("Masukkan nilai x: "))
    if x > 0 and x < z:
        break
    print("x harus bilangan bulat positif dan kurang dari", z)

# Input y dengan validasi
while True:
    y = int(input("Masukkan nilai y: "))
    if y > x and y < z:
        break
    print("y harus lebih besar dari", x, "dan kurang dari", z)

# Simpan semua nilai
nilai = [n1, n2, n3, n4, x, y, z]

# Urutkan pakai bubble sort
for i in range(7):
    for j in range(6 - i):
        if nilai[j] > nilai[j + 1]:
            temp = nilai[j]
            nilai[j] = nilai[j + 1]
            nilai[j + 1] = temp

# Median = elemen ke-4 (index 3) dari 7 data terurut
median = nilai[3]

# Hitung rata-rata
total = 0
for i in range(7):
    total = total + nilai[i]

rata_rata = total / 7

# Output
print("Nilai terurut:", nilai)
print("Median:", median)
print("Rata-rata:", rata_rata)