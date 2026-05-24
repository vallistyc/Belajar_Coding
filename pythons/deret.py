hasil = 0
strA = []

while True : 
    n = input("Masukkan jumlah deret (keluar ketik 'q') :")
    if n == 'q':
        break
    try : 
        n = int(n)
    except ValueError :
        print("Input tidak valid. Harap masukkan angka.")   
        continue
    for i in range (1, n+1):
        a = 5**i
        hasil = hasil + a
        strA.append("5^" + str(i))
    
    print("Deret yang dihitung:")
    print(" + ".join(strA) + " = ", hasil)
    print()