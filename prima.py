def isPrima(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
    
def bilanganPrima(awal, akhir):
    hold    =[]
    for k in range(awal, akhir+1):
        if isPrima(k):
            hold.append(k)
    return hold
    
print(bilanganPrima(1,100))