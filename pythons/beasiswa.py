total_dana = float(input("Masukkan total dana beasiswa (Rp): "))
persen_unggulan = float(input("Masukkan persentase beasiswa unggulan (contoh: 15): "))
penyebut_prestasi = float(input("Masukkan penyebut pecahan tiap beasiswa prestasi (contoh: 10): "))

# a) Beasiswa Unggulan
unggulan = (persen_unggulan / 100) * total_dana

# Sisa setelah unggulan
sisa1 = total_dana - unggulan

# b) Tiap Beasiswa Prestasi (ada 4, masing-masing 1/penyebut dari sisa1)
tiap_prestasi = (1 / penyebut_prestasi) * sisa1
total_prestasi = 4 * tiap_prestasi

# Sisa setelah prestasi
sisa2 = sisa1 - total_prestasi

# 6 Beasiswa Bantuan dengan rasio 7:5:4:3:2:1, total rasio = 22
satu_bagian = sisa2 / 22

bantuan1 = 7 * satu_bagian
bantuan2 = 5 * satu_bagian
bantuan3 = 4 * satu_bagian
bantuan4 = 3 * satu_bagian
bantuan5 = 2 * satu_bagian
bantuan6 = 1 * satu_bagian

# c) Unggulan + 1 Prestasi
gabungan = unggulan + tiap_prestasi

print("a) Dana beasiswa unggulan:", unggulan)
print("b) Dana tiap beasiswa prestasi:", tiap_prestasi)
print("c) Dana unggulan + 1 prestasi:", gabungan)
print("Detail beasiswa bantuan:")
print("   Bantuan 1:", bantuan1)
print("   Bantuan 2:", bantuan2)
print("   Bantuan 3:", bantuan3)
print("   Bantuan 4:", bantuan4)
print("   Bantuan 5:", bantuan5)
print("   Bantuan 6:", bantuan6)