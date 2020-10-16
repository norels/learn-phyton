inputUser = 0
nama = ["Farhan","Joko"]
nomorTelepon = ["08123456789","08987654321"]
inputNama = str
inputTelepon = str

while (inputUser < 1 or inputUser > 3):
    print("Selamat Datang!\n")
    print("--- Menu ---\n")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar\n")
    print("Pilih Menu: ")
    inputUser = int(input())
    if (inputUser == 1):
        print("Daftar Kontak:\n")
        for x in nama and nomorTelepon:
            print("Nama: " + x + "")
            print("No Telepon: " + x + "\n")
    elif (inputUser == 2):
        print("Nama: ")
        inputNama = input()
        nama.append(inputNama)
        print("No Telepon: ")
        inputTelepon = input()
        nomorTelepon.append(inputTelepon)
    elif (inputUser == 3):
        print("Progam selesai, sampai jumpa!\n")
        break