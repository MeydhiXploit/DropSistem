import os

# Meminta input dari user untuk direktori tempat file-file akan disimpan
direktori = input("Masukkan direktori tempat file-file akan disimpan: ")

# Membuat direktori jika belum ada
if not os.path.exists(direktori):
    print(f"Direktori {direktori} tidak ditemukan.")
else:
    # Membuat file kosong dengan nama yang berbeda-beda hingga 100 kali
    i = 1
    while True:
        nama_file = f"{direktori}/file_{i}.txt"
        if not os.path.exists(nama_file):
            with open(nama_file, "w"):
                pass
            i += 1

            
