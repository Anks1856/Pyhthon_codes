
def Mul(x):
    mul = 1
    for i in range(len(x)):
        mul*=i
    print(mul)
   
a = [10,12,3]    
# print (">>>>>>>>>>>>>>>0", len(a))
Mul(a)    

for i in range(len(a)):
    print (">>>>>>>>>>>0", i, a[i])
