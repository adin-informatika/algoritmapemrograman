# MEMBUKA FILE DATA
data = open("data_iris.txt","r")
print("Nama File",data.name)

# MEMBACA FILE DATA
file_konten = data.read(100)
print("Isi Data :",file_konten[17:39])

# MENUTUPP FILE DATA
data.close()
