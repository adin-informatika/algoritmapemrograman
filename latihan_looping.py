# For loops
#for i in range(1,10): 
     #print(i)
list_dosen =("Dosen1","Dosen2","Dosen3","Dosen4")
list_jadwal =("Senin","Selasa","Rabu","Kamis","Jumat")

for i in (list_dosen):
    for k in (list_jadwal):
        print(i," - ",k)
# Fibonanci 
n=10
fib = [0,1]

for i in range(n-2):
    fib_lanjut = fib[i+1] + fib[i]
    print(fib[i+1]," + ",fib[1]," = ",fib_lanjut)
    fib.append(fib_lanjut)
print(fib)
