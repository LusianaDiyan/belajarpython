thislist = ["satu", "tiga", "lima"]
satu = input("sisipkan angka huruf1 = ")
dua = input("sisipkan angka huruf2 = ")

print(thislist)
thislist.insert(1,satu)
thislist.insert(3,dua)
print("daftar update list : ")
print(thislist)
del thislist[2]
print("daftar final list : ")
print(thislist)
