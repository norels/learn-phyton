inputUser = 0
nama = ["Farhan","Joko"]
nomorTelepon = ["08123456789","08987654321"]
inputNama = str
inputTelepon = str

while (1):
    print("\n\n\n\n\n")
    print("Selamat Datang!\n")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print("Pilih Menu: ")
    inputUser = int(input())
    if (inputUser == 1):
        print("Daftar Kontak:")
        for x in range(len(nama)):
            print("Nama: " + nama[x])
            print("No Telepon: " + nomorTelepon[x])
    elif (inputUser == 2):
        print("Nama: ")
        inputNama = input()
        nama.append(inputNama)
        print("No Telepon: ")
        inputTelepon = input()
        nomorTelepon.append(inputTelepon)
        print("Kontak berhasil ditambahkan")
    elif (inputUser == 3):
        print("Progam selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")

        #testtestest