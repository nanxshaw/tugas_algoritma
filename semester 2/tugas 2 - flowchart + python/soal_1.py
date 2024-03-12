# Nama : Nanang Tri Nur Wicaksono
# NIM : 231011700253

# inputan data
seconds = int(input("Masukkan angka per detik: "))

# eksekusi data
minute = seconds // 60
hours = minute // 60
minutes = minute % 60

# tampilkan data
print(f"{seconds} detik : {hours} jam {minutes} menit.")
