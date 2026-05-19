while True:
    suhu = input("Masukkan suhu dalam Celsius (ketik 'q' untuk keluar): ")
    if suhu.lower() in ["q", "quit", "exit", "keluar"]:
        print("Selesai.")
        break

    try:
        suhu = float(suhu)
    except ValueError:
        print("Masukkan angka yang valid atau ketik 'q' untuk keluar.")
        continue

    if suhu > 0 and suhu < 100:
        print("Cair")
    elif suhu >= 100:
        print("Uap (Gas)")
    else:
        print("Beku (Padat)")
