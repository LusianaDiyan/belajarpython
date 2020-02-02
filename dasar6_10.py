# nilai = 100

# if nilai == 75:
# 	print("nilai anda: ", nilai)

# if nilai is 60:
# 	print("nilai anda: ", nilai)

# if nilai is not 60:
# 	print("nilai anda bukan 60 ")
# print("=======================================")
# if 80 <= nilai <= 100:
# 	print("nilai anda adalah A")
# elif 70 <= nilai < 80:
# 	print("nilai anda adalah B")
# elif 60 <= nilai < 70:
# 	print("nilai anda adalah C")
# elif 50 <= nilai < 60:
# 	print("nilai anda adalah T, lakukan perbaikan")
# else:
# 	print("maaf anda tidak lulus mata kuliah ini")

#====================================================================
#list sebagai iterable
# gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
# print("==list sebagai iterable==")
# for g in gorengan:
# 	print(g)
# 	print(len(g))

# #string sebagai iterable
# bakwan = 'bakwan'
# print("==string sebagai iterable==")
# for i in bakwan:
# 	print(i)

# #for di dalam for
# buah = ['semangka', 'jeruk', 'apel', 'anggur']
# sayur = ['kangkung', 'wortel', 'tomat', 'kentang']
# daftar_belanja = [gorengan,buah,sayur]
# print("==for di dalam for==")
# for subDaftarBelanja in daftar_belanja:
# 	print("Daftar Belanja = ",subDaftarBelanja)
# 	for komponen in daftar_belanja:
# 		print("komponen = ", komponen)

#====================================================================
# number = 50;

# for i in range(0,40):
# 	print(i)

# 	if i is number:
# 		print('angka ditemukan', i)
# 		break
# else:
# 	print('angka tidak ditemukan')
# print("space di luar for")

#================================================================
# for i in range(1,10):
# 	if i is 6:
# 		print("nilai i adalah", 6)
# 		pass
# 		print("cek bro 1")
# 	print('nilai saat ini adalah',1)
# else:
# 	print('akhir dari loop')
# print('print diluar loop')

#================================================================
# angka = 0

# while angka < 10:
# 	if angka is 5:
# 		# print('checkpoint 1')
# 		angka += 1
# 		continue
# 		# print('checkpoint 2')
# 	print('nilai angka adalah:', angka)
# 	angka = angka + 1
# else:
# 	print('nilai angka diakhir while adalah', angka)
# print('di luar while')

#================================================================
# def suaraayam():
# 	print("kukuruyuk!!!!")

# def hargaayam():
# 	suaraayam()
# 	print('harga ayam per 1 kg adalah Rp. 20.000')

# def hargatotalayam(kg):
# 	suaraayam()
# 	harga = 20000
# 	hargaTotal = kg+harga
# 	print('harga',kg,'kg ayam adalah',hargaTotal)

# hargaayam()
# hargatotalayam(2)
# hargatotalayam(0.5)
# hargatotalayam(1)
# hargatotalayam(9)

#================================================================
# def siswa(nama):
# 	print('siswa ini bernama: ', nama)

# siswa('mario')

# def guru(nama, pelajaran):
# 	print('guru ini bernama: ', nama)
# 	print('mengajar', pelajaran)

# guru(nama='popong', pelajaran='seni rupa')
# guru(pelajaran='olahraga',nama='endang')
# guru('olahraga','raihan')

# def penjagaSekolah(nama, shift='siang', galak='tidak'):
# 	print('penjaga sekolah ini bernama:', nama)
# 	print('shiftnya:', shift)
# 	print('galak?', galak)

# penjagaSekolah('Entis')
# penjagaSekolah('Maman', shift='malam')
# penjagaSekolah('Asep', galak='Sangat')
# penjagaSekolah(shift='malam', galak='iya')

#================================================================
# def kuadrat(argumen):
# 	total = argumen**2
# 	print('nilai kuadrat dari', argumen, 'adalah', total)
# 	return total

# a = kuadrat(4)
# print(a)
# print('+'*100)

# def tambah(argumen1, argumen2):
# 	total = argumen1 + argumen2
# 	print(argumen1, '+', argumen2, '=',total)
# 	return total

# def kali(argumen1, argumen2):
# 	total = argumen1 * argumen2
# 	print(argumen1, 'x', argumen2, '=', total)
# 	return total

# b = kali(3,tambah(3,4))
# print(b)

#================================================================
# def jumlah(a,b):
# 	c = a + b
# 	return c

# hasil = jumlah(4,5)
# kali = lambda x,y: x*y
# hasil = kali(3,4)
# print(hasil)

#================================================================
namaKucing = 'cassandra'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
	global namaKucing
	namaKucing = namaBaru
	print('saya rubah nama kucing menjadi', namaKucing)

def kasihMakanKucing(makanan,nama):
	global namaKucing, makananKucing
	namaKucing = nama
	makananKucing = makanan

rubahNamaKucing('ketie')
kasihMakanKucing('universal', 'alex')

print('nama kucing saya menjadi', namaKucing, 'dan makanan', makananKucing)
