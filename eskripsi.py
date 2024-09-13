# Fungsi enkripsi menggunakan Caesar Cipher yang diperluas untuk beberapa simbol
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        # Cek jika karakter adalah huruf
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        # Cek jika karakter adalah simbol tertentu, misal ~, #, $, dll.
        elif char in "~#$%^&*()-_+=<>?/":
            result += chr((ord(char) + shift - 32) % 15 + 32)  # Geser pada range simbol
        else:
            result += char
    
    return result

# Fungsi dekripsi menggunakan Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Aplikasi sederhana untuk enkripsi
def run_encryption_app():
    print("Selamat datang di aplikasi Enkripsi Caesar Cipher!")
    nama = input("Masukkan nama Anda: ")
    plaintext = input(f"Halo {nama}, masukkan teks yang ingin dienkripsi: ")
    shift_key = int(input("Masukkan nilai pergeseran (shift key): "))

    # Proses enkripsi
    encrypted_text = encrypt(plaintext, shift_key)
    print(f"\nHasil Enkripsi untuk '{plaintext}' adalah: {encrypted_text}")

    # Proses dekripsi
    decrypt_choice = input("Apakah Anda ingin mendekripsi teks tersebut? (y/n): ")
    if decrypt_choice.lower() == 'y':
        decrypted_text = decrypt(encrypted_text, shift_key)
        print(f"Hasil Dekripsi adalah: {decrypted_text}")
    else:
        print("Terima kasih telah menggunakan aplikasi ini!")

# Jalankan aplikasi
run_encryption_app()
