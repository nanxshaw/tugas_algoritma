# Nama : Nanang Tri Nur Wicaksono
# NIM : 231011700253

# inputan data
usd = float(input("Masukkan US Dollar : "))
kurs = float(input("Masukkan kurs : "))

# eksekusi data
rupiah = usd * kurs
amount = "{:,.2f}".format(rupiah) 

# tampilkan data
print(f"${usd} adalah Rp. {amount}.")
