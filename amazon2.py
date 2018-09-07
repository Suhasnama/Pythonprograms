data = [ int(x) for x in input("Enter elements of array (delim : space)\n").split()]

print(data)
for j in range(0 ,len(data)-1):
    for i in range(j,len(data)-1):
        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp

print(data)