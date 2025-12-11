# Contoh dictionary dasar

person = {
    "nama": "Budi",
    "umur": 20,
    "kota": "Jakarta"
}

print("Nama:", person["nama"])
print("Daftar key:", list(person.keys()))
print("Daftar value:", list(person.values()))

# Menambah data
person["pekerjaan"] = "Mahasiswa"

# Mengubah data
person["umur"] = 21

# Menghapus data
del person["kota"]

print("Data setelah update:", person)

