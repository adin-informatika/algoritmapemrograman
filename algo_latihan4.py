# ALGO LATIHAN 4

# SETTING NILAI VARIABEL
harga_kecap			= 3500
harga_sambal		= 2500
harga_indomie		= 3000
harga_teh			= 2000
harga_kopi			= 1500

# SETTING JUMLAH BARANG
jumlah_kecap		= int(input("Masukan jumlah kecap   : "))
jumlah_sambal		= int(input("Masukan jumlah sambal  : "))
jumlah_indomie		= int(input("Masukan jumlah indomie : "))
jumlah_teh			= int(input("Masukan jumlah teh     : "))
jumlah_kopi			= int(input("Masukan jumlah kopi    : "))

# CETAK HASIL
print("-----------------------------------------------")
print("                WARUNG SEMBAKO")
print("-----------------------------------------------")
print("Nama Barang       Harga     Jumlah     Total")
print("Kecap            ",harga_kecap,"    ",jumlah_kecap,"        ",harga_kecap*jumlah_kecap)
print("Sambal           ",harga_sambal,"    ",jumlah_sambal,"        ",harga_sambal*jumlah_sambal)
print("Indomie          ",harga_indomie,"    ",jumlah_indomie,"        ",harga_indomie*jumlah_indomie)
print("Teh              ",harga_teh,"    ",jumlah_teh,"        ",harga_teh*jumlah_teh)
print("Kopi             ",harga_kopi,"    ",jumlah_kopi,"        ",harga_kopi*jumlah_kopi)
print("-----------------------------------------------")
print("Total Belanja						  ",harga_kecap*jumlah_kecap+harga_sambal*jumlah_sambal+harga_indomie*jumlah_indomie+harga_teh*jumlah_teh+harga_kopi*jumlah_kopi)
print("-----------------------------------------------")
