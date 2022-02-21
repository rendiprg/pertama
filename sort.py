def removeDuplicate(arr):
    hold=[]
    m   =0
    for k in range(len(arr)):
        if arr[k]!=m :
            hold.append(arr[k])
        m = arr[k]
    return hold

def sortir(data):
    for k in range(len(data)):
        for m in range(len(data)-1):
            if(data[m]>data[m+1]):
                data[m+1], data[m]  = data[m], data[m+1]
    return data

data =[5,4,7,3,3,2,1,6,5]
rst = sortir(data)
print(rst)
print("\n")
print(removeDuplicate(rst))