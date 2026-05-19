# data mk kro kelas, tak taruh sini biar program optimal.
# Klo tak taruh loop, data bakal ke generate ulang terus tiap kali user input, jadi program bakal berat.
data = [
    ["MK101", "A"],
    ["MK101", "B"],
    ["MK202", "A"],
    ["MK203", "C"],
    ["MK304", "B"]
    ]

while True : 
    mk = input("Masukkan kode matkul (ketik q untuk keluar) :")
    if mk.lower() in ["q", "quit", "exit", "keluar"]:
        print("Program Selesai")
        break
    kls = input("Masukkan kelas (ketik q untuk keluar) :")
    if kls.lower() in ["q", "quit", "exit", "keluar"]:
        print("Program Selesai")
        break
    
    # Gawe nyocokno mk kro kelas e
    if [mk, kls] in data:
        print("Kelas tersedia untuk matkul", mk, "kelas", kls)
    else:
        print("Kelas tidak tersedia untuk matkul", mk, "kelas", kls)