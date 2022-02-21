string =""
bar=1
x=5
while bar<x:
    kol = bar
    while kol > 1:
        string +=" "
        kol -=1 
    kiri =0
    while kiri <= (x-bar):
        string +="*"
        kiri +=1
    kanan = kiri
    while kanan>1:
        string +="*"
        kanan -=1
    if (bar+1) <=x:
        string +="\n"
    bar+=1
bar = x-1
while bar>=0:
    kol = bar
    while kol>0:
        string +=" "
        kol -=1
    kiri=1
    while kiri < (x -(bar-1)):
        string +="*"
        kiri+=1
    kanan = 1
    while kanan < (kiri-1):
        string +="*"
        kanan+=1
    string +="\n"
    bar-=1
print(string)