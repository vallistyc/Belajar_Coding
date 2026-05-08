penghasilan = int(input("Masukkan penghasilan: ")) 
# saya jadikan  variabel tersendiri agar lebih mudah untuk memahami kode secara keseluruhan
# pun ketika akan dikembangkan lagi, data inputan masih tersimpan, sehingga tidak perlu mengubah kode yang lain, cukup mengubah variabel penghasilan saja

sisa = penghasilan
total = 0

if sisa > 500_000_000:
    lap4 = (sisa - 500_000_000) * 0.30
    sisa = 500_000_000
else:
    lap4 = 0

if sisa > 250_000_000:
    lap3 = (sisa - 250_000_000) * 0.25
    sisa = 250_000_000
else:
    lap3 = 0

if sisa > 50_000_000:
    lap2 = (sisa - 50_000_000) * 0.15
    sisa = 50_000_000
else:
    lap2 = 0

lap1 = sisa * 0.05

total = lap1 + lap2 + lap3 + lap4

print("Lapisan 1:", lap1)
print("Lapisan 2:", lap2)
print("Lapisan 3:", lap3)
print("Lapisan 4:", lap4)
print("Total Pajak:", total)