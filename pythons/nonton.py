while True :
    print("Paket tersedia :")
    print("1. Paket Basic (SD) : Rp 50.000")
    print("2. Paket Standard (HD) : Rp 100.000")
    print("3. Paket Premium (4K) : Rp 150.000")
    
    pkt = input("Pilih paket (1-3, ketik q untuk keluar) :")
    if pkt.lower() in ["q", "quit", "exit", "keluar"]:
        print("Program Selesai")
        break
    print()
    
    print("Durasi langganan :")
    print("1. Bulanan: +0%")
    print("2. 3 bulan: diskon 5%")
    print("3. 6 bulan: diskon 10%")
    print("4. Tahunan: diskon 15%")
    
    durasi = input("Pilih durasi langganan (1-4, ketik q untuk keluar) :")
    if durasi.lower() in ["q", "quit", "exit", "keluar"]:
        print("Program Selesai")
        break
    print()
    
    print("Jumlah perangkat :")
    print("1. 1 perangkat: +0%")
    print("2. 2 perangkat: +20%")
    print("3. 4 perangkat: +40%")
    
    dev = input("Pilih jumlah perangkat (1-3, ketik q untuk keluar) :")
    if dev.lower() in ["q", "quit", "exit", "keluar"]:
        print("Program Selesai")
        break
    print()
    
    print("Biaya tambahan :")
    print("1. Konten sport: +Rp 25.000 per bulan")
    print("2. Download offline: +Rp 15.000 per bulan")

    add = input("Pilih biaya tambahan (1-2, ketik q untuk keluar) :")
    if add.lower() in ["q", "quit", "exit", "keluar"]:
        print("Program Selesai")
        break
    print()
    
    # Hitung Paket
    if pkt == "1":
        biayaPkt = 50000
        strPkt = "Paket Basic (SD)"
    elif pkt == "2":
        biayaPkt = 100000
        strPkt = "Paket Standard (HD)"
    elif pkt == "3":
        biayaPkt = 150000
        strPkt = "Paket Premium (4K)"
        
    # Durasi
    if durasi == "1":
        diskonDurasi = 0
        strDurasi = "Bulanan"
    elif durasi == "2":
        diskonDurasi = 0.05
        strDurasi = "3 bulan"
    elif durasi == "3":
        diskonDurasi = 0.10
        strDurasi = "6 bulan"
    elif durasi == "4":
        diskonDurasi = 0.15
        strDurasi = "Tahunan"
        
    # Perangkat
    if dev == "1":
        biayaDev = 0
        strDev = "1 perangkat"
    elif dev == "2":
        biayaDev = 0.20
        strDev = "2 perangkat"
    elif dev == "3":
        biayaDev = 0.40
        strDev = "4 perangkat"
        
    # Biaya tambahan
    if add == "1":
        biayaAdd = 25000
        strAdd = "Konten sport"
    elif add == "2":
        biayaAdd = 15000
        strAdd = "Download offline"
    else :
        biayaAdd = 0
        strAdd = "Tidak ada biaya tambahan"
        
    # Hitung total biaya
    total = biayaPkt * (1 - diskonDurasi) * (1 + biayaDev) + biayaAdd
    print ("Paket: " + strPkt)
    print("Durasi: " + strDurasi)
    print("Perangkat: " + strDev)
    print("Biaya Tambahan: " + strAdd)
    print("-----------------------------")
    print(f"Total biaya yang harus dibayar: Rp {total:,}")
    
    #validasi input
    val = input("Reset pilihan? (y/n) :")
    if val.lower() in ["y", "yes"]:
        print("Pilihan direset. Silakan pilih paket lagi.")
        print()
    else:
        print("Program Selesai")
        break