while True :
    n = input ("Masukkan jumlah perulangan (ketik q untuk keluar):")
    if n == "q":
        break
    try:
        n = int(n)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        continue
    
    for line in range (1, n+1):
        for number in range (1, line+1):
            print(number,end=" ")
        print()
    
    for line in range (n, 1, -1):
        for number in range (1, line): 
            print(number,end=" ")
        print()