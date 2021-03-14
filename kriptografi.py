import os

txt_filename_history = 'history.txt'

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def CaesarCipherEncrypt():
    clear_screen()
    print("=====================================")
    print("|      Caesar Cipher - Enkripsi     |")
    print("=====================================")
    show_history()
    try:
        plaintext = str(input("Plainteks: "))
        shift = int(input("Bergeser: "))
    except(KeyboardInterrupt):
        back_to_menu()
    ciphertext = ""
    for i in range(len(plaintext)):
        if(plaintext[i].isspace()):
            ciphertext += " "
        elif(plaintext[i].isupper()):
            ciphertext += chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
    print("Cipherteks: " + ciphertext)
    create_history(1, shift, 0, plaintext, ciphertext)
    back_to_menu()

def CaesarCipherDecrypt():
    clear_screen()
    print("=====================================")
    print("|      Caesar Cipher - Dekripsi     |")
    print("=====================================")
    show_history()
    try:
        ciphertext = str(input("Cipherteks: "))
        shift = int(input("Bergeser: "))
    except(KeyboardInterrupt):
        back_to_menu()
    plaintext = ""
    for i in range(len(ciphertext)):
        if(ciphertext[i].isspace()):
            plaintext += " "
        elif(ciphertext[i].isupper()):
            plaintext += chr((ord(ciphertext[i]) + -shift - 65) % 26 + 65)
        else:
            plaintext += chr((ord(ciphertext[i]) + -shift - 97) % 26 + 97)
    print("Plainteks: " + plaintext)
    create_history(2, shift, 0, plaintext, ciphertext)
    back_to_menu()

def generateKey(string, key):
    new_key = ""
    n = len(string)
    for i in range(len(string)):
        if(string[i].isspace()):
            n -= 1
    if n == len(key):
        return key
    j = 0
    for i in range(len(string)):
        if(string[i].isspace()):
            new_key += " "
        else:
            new_key += key[j % len(key)]
            j += 1
    return new_key

def VigènereCipherEncrypt():
    clear_screen()
    print("=====================================")
    print("|     Vigènere Cipher - Enkripsi    |")
    print("=====================================")
    show_history()
    try:
        plaintext = str(input("Plainteks: "))
        kunci = str(input("Kunci: "))
    except(KeyboardInterrupt):
        back_to_menu()
    ciphertext = ""
    key = generateKey(plaintext, kunci)
    for i in range(len(plaintext)):
        if(plaintext[i].isspace()):
            ciphertext += " "
        else:
            if(plaintext[i].isupper() and key[i].isupper()):
                x = (ord(plaintext[i]) + ord(key[i])) % 26
                x += ord('A')
            elif(plaintext[i].isupper() and key[i].islower()):
                x = (ord(plaintext[i]) + (ord(key[i]) - 32)) % 26
                x += ord('A')
            elif(plaintext[i].islower() and key[i].isupper()):
                x = ((ord(plaintext[i]) - 32) + ord(key[i])) % 26
                x += ord('a')
            else:
                x = ((ord(plaintext[i]) - 32) + (ord(key[i]) - 32)) % 26
                x += ord('a')
            ciphertext += chr(x)
    print("Cipherteks: " + ciphertext)
    create_history(3, 0, kunci, plaintext, ciphertext)
    back_to_menu()

def VigènereCipherDecrypt():
    clear_screen()
    print("=====================================")
    print("|     Vigènere Cipher - Dekripsi    |")
    print("=====================================")
    show_history()
    try:
        ciphertext = str(input("Cipherteks: "))
        kunci = str(input("Kunci: "))
    except(KeyboardInterrupt):
        back_to_menu()
    plaintext = ""
    key = generateKey(ciphertext, kunci)
    for i in range(len(ciphertext)):
        if(ciphertext[i].isspace()):
            plaintext += " "
        else:
            if(ciphertext[i].isupper() and key[i].isupper()):
                x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
            elif(ciphertext[i].isupper() and key[i].islower()):
                x = (ord(ciphertext[i]) - (ord(key[i]) - 32) + 26) % 26
                x += ord('A')
            elif(ciphertext[i].islower() and key[i].isupper()):
                x = ((ord(ciphertext[i]) - 32) - ord(key[i]) + 26) % 26
                x += ord('a')
            else:
                x = ((ord(ciphertext[i]) - 32) - (ord(key[i]) - 32) + 26) % 26
                x += ord('a')
            plaintext += chr(x)
    print("Plainteks: " + plaintext)
    create_history(4, 0, kunci, plaintext, ciphertext)
    back_to_menu()

def create_history(tipe, s, kunci, plaintext, ciphertext):
    file_history_in = open(txt_filename_history, "w")
    if(tipe == 1):
        file_history_in.write("Casesar Cipher (Enkripsi)\nShift: %d\nPlainteks: %s\nCipherteks: %s" % (s, plaintext, ciphertext))
    elif(tipe == 2):
        file_history_in.write("Casesar Cipher (Dekripsi)\nShift: %d\nCipherteks: %s\nPlainteks: %s" % (s, ciphertext, plaintext))
    elif(tipe == 3):
        file_history_in.write("Vigènere Cipher (Enkripsi)\nKunci: %s\nPlainteks: %s\nCipherteks: %s" % (kunci, plaintext, ciphertext))
    elif(tipe == 4):
        file_history_in.write("Vigènere Cipher (Dekripsi)\nKunci: %s\nCipherteks: %s\nPlainteks: %s" % (kunci, ciphertext, plaintext))
    file_history_in.close()

def show_history():
    file_history_in = open(txt_filename_history, "r")
    history = file_history_in.read()
    if(len(history) > 0):
        print("Riwayat sebelumnya: " + history)
        print("=====================================")
    file_history_in.close()

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
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

if __name__ == "__main__":
    show_menu()
