a=[
   [0,5,3,4],
   [0,0,0,1],
   [0,1,0,0],
   [0,0,0,0]]
r=4
c=4
zero=0
nonzero=0
print("total element=", r*c)
for i in range (r):
    for j in range(c):
     if (a[i][j]==0):
        zero+=1
    else:
        nonzero+=1
if zero>nonzero:
            print ("sparse matrix")
else:
            print("not sparse matrix.")



