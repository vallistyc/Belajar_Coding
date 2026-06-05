jumlah = 0
konsonan = []
kalimat= "saya makan"
lain = ["s", "w", "y", "f", "v", "z", "sy", "kh", "ny"]
for kata in kalimat.split():
    print(kata)
    for char in kata:
        if char.lower() in lain:
            jumlah += 1
            konsonan.append(f"{char} pada '{kata}'")
print(jumlah)
print(konsonan)