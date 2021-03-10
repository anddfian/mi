import os

txt_filename_history = 'history.txt'

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def CaesarCipherEncrypt():
    clear_screen()
    print("=====================================")
    print("|      Caesar Cipher - Enkripsi     |")
    print("=====================================")
    try:
        plaintext = str(input("Plainteks: "))
        s = int(input("Shift: "))
    except(KeyboardInterrupt):
        back_to_menu()
    ciphertext = ""
    for i in range(len(plaintext)):
        if (plaintext[i].isupper()):
            ciphertext += chr((ord(plaintext[i]) + s - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(plaintext[i]) + s - 97) % 26 + 97)
    print("Cipherteks: " + ciphertext)
    create_history("Casesar Cipher (Enkripsi)", s, 0, plaintext, ciphertext)
    back_to_menu()

def CaesarCipherDecrypt():
    clear_screen()
    print("=====================================")
    print("|      Caesar Cipher - Dekripsi     |")
    print("=====================================")
    try:
        ciphertext = str(input("Cipherteks: "))
        s = int(input("Shift: "))
    except(KeyboardInterrupt):
        back_to_menu()
    plaintext = ""
    for i in range(len(ciphertext)):
        if (ciphertext[i].isupper()):
            plaintext += chr((ord(ciphertext[i]) + -s - 65) % 26 + 65)
        else:
            plaintext += chr((ord(ciphertext[i]) + -s - 97) % 26 + 97)
    print("Plainteks: " + plaintext)
    create_history("Casesar Cipher (Dekripsi)", s, 0, plaintext, ciphertext)
    back_to_menu()

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): #jika panjang kata dan kunci sama
        return(key) #return kunci
    else:
        for i in range(len(string) - len(key)): #sisa kata yang tidak tertutupi kunci
            key.append(key[i % len(key)]) #penambahan key pada kata tidak tertutupi
    return("" . join(key))

def VigènereCipherEncrypt():
    clear_screen()
    print("=====================================")
    print("|     Vigènere Cipher - Enkripsi    |")
    print("=====================================")
    try:
        plaintext = str(input("Plainteks: "))
        kunci = str(input("Kunci: "))
    except(KeyboardInterrupt):
        back_to_menu()
    key = generateKey(plaintext, kunci)
    ciphertext = []
    for i in range(len(plaintext)):
        if(plaintext[i].isupper() and key[i].isupper()):
            x = (ord(plaintext[i]) + ord(key[i])) % 26 #(P + K) mod 26
            x += ord('A') #Angka di mulai dari ord A seterusnya
        else:
            x = (ord(plaintext[i]) + ord(key[i])) % 26 #(P + K) mod 26
            x += ord('a') #Angka di mulai dari ord A seterusnya
        ciphertext.append(chr(x)) #hasil x di masukkan ke dalam list orig text
    print("Cipherteks: " + "" . join(ciphertext))
    create_history("Vigènere Cipher (Enkripsi)", 0, kunci, plaintext, "" . join(ciphertext))
    back_to_menu()

def VigènereCipherDecrypt():
    clear_screen()
    print("=====================================")
    print("|     Vigènere Cipher - Dekripsi    |")
    print("=====================================")
    try:
        ciphertext = str(input("Cipherteks: "))
        kunci = str(input("Kunci: "))
    except(KeyboardInterrupt):
        back_to_menu()
    key = generateKey(ciphertext, kunci)
    plaintext = []
    for i in range(len(ciphertext)):
        if(ciphertext[i].isupper() and key[i].isupper()):
            x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26 #((P - K) + 26) mod 26
            x += ord('A') #Angka di mulai dari ord A seterusnya
        else:
            x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26 #((P - K) + 26) mod 26
            x += ord('a') #Angka di mulai dari ord A seterusnya
        plaintext.append(chr(x)) #hasil x di masukkan ke dalam list orig text
    print("Plainteks: " + "" . join(plaintext))
    create_history("Vigènere Cipher (Dekripsi)", 0, kunci, "" . join(plaintext), ciphertext)
    back_to_menu()

def create_history(tipe, s, kunci, plaintext, ciphertext):
    file_history_in = open(txt_filename_history, "a")
    if(tipe == "Casesar Cipher (Enkripsi)"):
        file_history_in.write("%s | Shift: %d | Plainteks: %s | Cipherteks: %s\n" % (tipe, s, plaintext, ciphertext))
    elif(tipe == "Casesar Cipher (Dekripsi)"):
        file_history_in.write("%s | Shift: %d | Cipherteks: %s | Plainteks: %s\n" % (tipe, s, ciphertext, plaintext))
    elif(tipe == "Vigènere Cipher (Enkripsi)"):
        file_history_in.write("%s | Kunci: %s | Plainteks: %s | Cipherteks: %s\n" % (tipe, kunci, plaintext, ciphertext))
    elif(tipe == "Vigènere Cipher (Dekripsi)"):
        file_history_in.write("%s | Kunci: %s | Cipherteks: %s | Plainteks: %s\n" % (tipe, kunci, ciphertext, plaintext))
    file_history_in.close()

def show_history():
    clear_screen()
    print("=====================================")
    print("|              Riwayat              |")
    print("=====================================")
    file_history_in = open(txt_filename_history, "r")
    print(file_history_in.read())
    file_history_in.close()
    back_to_menu()

def back_to_menu():
    input("\nTekan 'Enter' untuk kembali...")
    show_menu()

def show_menu():
    clear_screen()
    print("=====================================")
    print("|     PROGRAM KRIPTOGRAFI KLASIK    |")
    print("=====================================")
    print("|       OLEH ANGGOTA KELOMPOK       |")
    print("=====================================")
    print("| ANDI ALFIAN BAHTIAR  (2009106002) |")
    print("| DHIMAS PRAKASA HENJO (2009106015) |")
    print("| ALFI SYACHDIAN NOOR  (2009106023) |")
    print("| MUH. FATHIR FAHREZAH (2009106024) |")
    print("| ALAN NUZULAN         (2009106032) |")
    print("=====================================")
    print("| [1] Caesar Cipher - Enkripsi      |")
    print("| [2] Caesar Cipher - Dekripsi      |")
    print("| [3] Vigènere Cipher - Enkripsi    |")
    print("| [4] Vigènere Cipher - Dekripsi    |")
    print("| [5] Riwayat                       |")
    print("| [0] Exit                          |")
    print("=====================================")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        CaesarCipherEncrypt()
    elif(selected_menu == "2"):
        CaesarCipherDecrypt()
    elif(selected_menu == "3"):
        VigènereCipherEncrypt()
    elif(selected_menu == "4"):
        VigènereCipherDecrypt()
    elif(selected_menu == "5"):
        show_history()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

if __name__ == "__main__":
    show_menu()
