valid = False

while not valid:
    num = input("Masukkan nomor:")
    
    # CEK SPASI
    if " " in num:
        print("Error: Nomor telepon tidak boleh mengandung spasi")
        continue
    
    # CEK FORMAT
    if num.startswith("+62"):
        fltdnum=num[3:]
    elif num.startswith("62"):
        fltdnum=num[2:]
    elif num.startswith("0"):
        fltdnum=num[1:]
    else:
        print("Error: format tidak valid")
        continue
    
    # CEK ANGKA
    if not fltdnum.isdigit():
        print("Error: Input wajib berupa angka")
        continue
    
    # CEK PANJANG
    if len(fltdnum) < 10 or len(fltdnum) > 13:
        print("Error: Panjang digit harus di range 10-13")
        continue
    
    # CEK DUA DIGIT AWAL
    dua_digit=int(fltdnum [:2])
    
    if dua_digit < 11 or dua_digit > 99:
        print(f"Error: Dua digit awal ({fltdnum[:2]}) tidak valid")
        continue
    
    # VALIDASI AKHIR
    valid = True
    print(f"Valid! Nomor {num} memenuhi semua syarat.")