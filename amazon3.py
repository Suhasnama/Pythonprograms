#py-3.x

#         c r
# 1 + 0 = 0 1
# 0 + 1 = 0 1
# 0 + 0 = 0 0
# 1 + 1 = 1 1
# 



def additon(x ,y):
    if (x,y) == (0,1) or (1,0):
        return 0,1
    elif (x,y) == (1,1):
        return 1,1
    elif (x,y) == (0,0):
        return 0,0

def main():
    data = [int(x) for x in input("Enter two binary numbers (delim : space)").split()]

    x = data[0]
    y = data[1]
    c = 0
    val = []
#   10101
#   10011
#       1
    for i,j in x,y:
        c , v = additon(i+c,j)
        val.append(v)




