import random

R = random.randint(0,255)
print(R)
maxguess=12

for i in range (1,maxguess+1):
    guess = int(input("Masukkan R:"))
    
    if guess == R :
        print("BENAR")
        break
    elif R-guess <= 10:
        print("PANAS")
        print("Banyak percobaan:",i)
    elif 11 <= R-guess <= 30:
        print("HANGAT")
        print("Banyak percobaan:",i)
    elif R-guess >=31:
        print("DINGIN")
        print("Banyak percobaan:",i)
        
    if i == maxguess+1:
        print("KESEMPATAN MENEBAK HABIS")
        break