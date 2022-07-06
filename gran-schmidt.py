
def gs_cofficient(v1, v2):
    n = 0
    for i in range (len(v1)):
        n += (v1[i]*v2[i])
    d = 0
    for i in range (len(v1)):
        d += (v1[i]*v1[i])
    return (n/d)

def multiply(cofficient, v):
        projvec = []
        for i in v:
            projvec.append(i*cofficient)
        return(projvec)

def proj(v1, v2):
    return multiply(gs_cofficient(v1, v2) , v1)

def gs(X):
    Y = []
    for i in range(len(X)):
        temp_vec = X[i]
        for inY in Y :
            proj_vec = proj(inY, X[i])
            #print "i =", i, ", projection vector =", proj_vec
            for i in range (len(temp_vec)):
                temp_vec[i] -= proj_vec[i]
            #print "i =", i, ", temporary vector =", temp_vec
        Y.append(temp_vec)
    return Y

print("Number of Wishes")
t = int(input())
for _ in range (t):
    print("Enter number of vectors")
    n = int(input())
    a = []
    print("Enter size of vectors")
    k = int(input())
    key = 0
    for _ in range (n):
        l = [float(i) for i in input().split()]
        if len(l) != k:
            print("Wrong size of Array")
            key = 1
            break
        a.append(l)
    print(a)
    if key == 0:
        print(gs(a))
    else:
        print("You wasted a Wish")