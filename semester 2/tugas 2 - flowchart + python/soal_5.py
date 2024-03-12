# Nama : Nanang Tri Nur Wicaksono
# NIM : 231011700253

# function cek nilai to grade
def konversi_nilai_ke_grade(nilai):
    if nilai < 40:
        return "E"
    elif 41 <= nilai <= 54:
        return "D"
    elif 55 <= nilai <= 64:
        return "C"
    elif 65 <= nilai <= 79:
        return "B"
    else:
        return "A"

# Input nilai
nilai = float(input("Masukkan nilai: "))

# Konversi nilai ke grade
grade = konversi_nilai_ke_grade(nilai)

# Tampilkan data
print(f"Nilai {nilai} adalah {grade}")
