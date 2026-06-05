# FUNCTION HITUNG KONSONAN
def hitungKonsonan(kalimat, daftarHuruf):
    jumlah = 0
    konsonan = []

    for kata in kalimat.split():
        i = 0
        while i < len(kata):
            # cek 2 huruf dulu
            dua = kata[i:i+2].lower()
            if dua in daftarHuruf:
                jumlah += 1
                konsonan.append(f"{dua} pada '{kata}'")
                i += 2
                continue
            # cek 1 huruf
            satu = kata[i].lower()
            if satu in daftarHuruf:
                jumlah += 1
                konsonan.append(f"{satu} pada '{kata}'")
            i += 1
    return jumlah, konsonan

# FUNCTION MAIN
kalimat = input("Masukkan kalimat: ")

bibir = ["p","b","m"]
gigi = ["t", "d", "n", "l", "r"]
lagit = ["c", "j", "k", "g", "ng"]
lain = ["s", "w", "y", "f", "v", "z", "sy", "kh", "ny"]

hbibir=hitungKonsonan(kalimat, bibir)
hgigi=hitungKonsonan(kalimat, gigi)
hlagit=hitungKonsonan(kalimat, lagit)
hlain=hitungKonsonan(kalimat, lain)

print(f"Jumlah konsonan bibir: {hbibir[0]} pada {hbibir[1]}")
print(f"Jumlah konsonan gigi: {hgigi[0]} pada {hgigi[1]}")
print(f"Jumlah konsonan langit: {hlagit[0]} pada {hlagit[1]}")
print(f"Jumlah konsonan lain: {hlain[0]} pada {hlain[1]}")
