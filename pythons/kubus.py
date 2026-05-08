import math

R = float(input("Masukkan sisi kubus: "))
r = float(input("Masukkan jari-jari: "))
h = float(input("Masukkan tinggi: "))

volume_kubus = R**3
volume_kerucut = (1/3) * math.pi * r**2 * h

volume_sisa = volume_kubus - volume_kerucut

luas_kubus = 6 * R**2
luas_lubang = math.pi * r**2
s = math.sqrt(r**2 + h**2)
selimut = math.pi * r * s

luas_sisa = luas_kubus - luas_lubang + selimut

print("Volume sisa:", volume_sisa)
print("Luas permukaan sisa:", luas_sisa)