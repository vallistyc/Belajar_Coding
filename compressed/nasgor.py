harga_beli = int(input("Harga beli : "))
harga_jual = int(input("Harga jual : "))

# biaya gas dan bumbu
biaya_tambahan = 0.12 * harga_beli

# keuntungan
keuntungan = harga_jual - harga_beli - biaya_tambahan

print("Harga beli : Rp", harga_beli)
print("Biaya tambahan : Rp", biaya_tambahan)
print("Harga jual : Rp", harga_jual)
print("Keuntungan per porsi : Rp", keuntungan)