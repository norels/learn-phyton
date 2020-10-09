teori = int(input("Berapa nilai teori: "))
praktik = int(input("Berapa nilai praktik:"))


if teori >= 70 and praktik >= 70:
    print("Selamat, anda lulus!")
elif teori < 70 and praktik >= 70:
    print("Anda harus mengulang ujian teori")
elif teori >= 70 and praktik < 70:
    print("Anda harus mengulang ujian praktik")
else :
    print("Anda harus mengulang ujian teori dan ujian praktik")

#udah bisa kayaknya hehehe