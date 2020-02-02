# a = 5
# b = 3
# c = 4.0

# #penjumlahan
# print("penjumlahan a + b =", a + b)

# #pengurangan
# print("pengurangan a - b =", a - b)

# #perkalian
# print("perkalian a * b =", a * b)

# #pembagian
# print("pembagian a / b =", a / b)

#--------------------------------------------------------------------------------

# text1 = 'jalan - jalan di hari minggu'
# text2 = 'jalan - jalan di hari jum\'at'
# text3 = "jalan - jalan di hari jum'at"
# text4 = 'mahmuy berkata, "kemarin kemana bro?"'
# text5 = "hobloh menjawab, \"jalan - jalan bro\""
# text6 = 'mahmuy: "kemarin kemana bro?"\nhobloh: "jalan - jalan bro"'
# text7 = """
# mahmuy: "kemarin kemana bro?"
# hobloh: "jalan - jalan bro"
# mahmuy: "jalan - jalan kemana bro?"
# hobloh: "ke mang uing bro!!"
# """
# text8 = 'C:\nyoto'
# print("text1 = ",text1)
# print("text2 = ",text2)
# print("text3 = ",text3)
# print("text4 = ",text4)
# print("text5 = ",text5)
# print("text6 = ",text6)
# print("text7 = ",text7)
# print("text8 = ",text8)

# text = "kue pukis"
# a = text[2:]
# print('e'+a+' nanas')

#----------------------------------------------------------------
Data = [1,4,9,16,25,30,64]
#mengakses list
Subdata1 = Data[3]
print("Subdata1 = ",Subdata1)
Subdata2 = Data[-3]
print("Subdata2 = ",Subdata2)
#memotong list
Subdata3 = Data[2:4]
print("Subdata3 = ",Subdata3)
Subdata4 = Data[2:]
print("Subdata4 = ",Subdata4)
Subdata5 = Data[:2]
print("Subdata5 = ",Subdata5)
Subdata6 = Data[-2:]
print("Subdata6 = ",Subdata6)
Subdata7 = Data[:-2]
print("Subdata7 = ",Subdata7)
#menambah list
Data2 = [100, 200, 300, 400, 500, 600, 700, 800]
Data3 = Data + Data2
print("Data3 = ", Data3)
#merubah content dari list
print("Data = ", Data)
Data[4] = 87
print("Data[4] = ", Data)
#mengcopy list ke variabel baru
a = Data[:]
a[5] = 87
print("a[5] = ",a[5])
#merubah content list dengan menggunakan metoda slicing
Data[3:5] = [11,12]
#list dalam list
x = [Data,Data2]
print("x = ",x)
#mengakses list dalam multidimensional list
y = x[0][3]
print("y = ",y)
#methods untuk list
Data.append(30)
#function yang bisa digunakan kepada list
panjang_list = len(Data)
print(Data)
print("panjang_list = ", panjang_list)
