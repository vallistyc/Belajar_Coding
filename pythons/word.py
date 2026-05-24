while True :
    kal = input ("Masukkan kalimat (ketik q untuk keluar): ").lower()
    if kal.lower() in ["q", "quit", "exit", "keluar", "metu"]:
        print("program selesai")
        break
    ter = input ("Masukkan Kata Terlarang (ketik q untuk keluar): ").lower()
    if ter.lower() in ["q", "metu", "keluar", "exit"]:
        print("program selesai")
        break
    char = "-"
    kata = kal.split()
    kata_filtered = [part
                    for katas in kata
                    for part in 
                    (katas.split(char) if char in katas else [word])]
    
    # Menggunakan "in" untuk mengecek apakah suatu string cocok dengan salah satu elemen di string array
    if ter in kata_filtered or kata:
        print ("Kalimat mengandung kata", ter)
    else : 
        print ("Kalimat TIDAK mengandung kata terlarang")
    