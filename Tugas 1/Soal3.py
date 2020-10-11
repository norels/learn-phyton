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

catetan jawaban versi mas farhan

#nilai_minimum = float(input("Nilai minimun: "))

#nilai_teori = float(input("Nilai teori: "))
#nilai_praktek = float(input("Nilai prakrek: "))

#if nilai_teori >= nilai_minimum and nilai_praktek >= nilai_minimum:
#    print("Lulus")
#elif nilai_teori >= nilai_minimum and nilai_praktek < nilai_minimum:
#    print("Anda mengulang ujian praktek")
#elif nilai_teori < nilai_minimum and nilai_praktek >= nilai_minimum:
#    print("Anda mengulang ujian teori")
#else:
#    print("Anda mengulang ujian teori dan praktek")