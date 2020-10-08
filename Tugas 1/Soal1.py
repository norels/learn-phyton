nama = input("Siapa namamu: ")
print(type(nama))
print("Namaku "+ nama)

umur = input("Berapa umurmu:")
print(type(umur))
print("Umurku " + umur + " tahun")

tinggi = input("Berapa tinggimu:")
print(type(tinggi))
print("Tinggiku " + tinggi + " cm")

biodata = "Nama saya {} , umur saya {} tahun, dan tinggi saya {} cm.".format(nama, umur, tinggi)

print(biodata)
