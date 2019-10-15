a = [10,1,24,5,45,65,565,78]
b = [100,455,758,9,22,211,15,2]
c = 0
for i in a:
    for j in b:
        if(i == j):
            c+=1
            print(i)

if(c == 0):
    print("no same element")

    
   
        


# #ans = a + b
# A = set(a)
# B = set(b)
# if (A & b):
#     print(A & B)
# else:
#     print("no same element")


# #print(sorted(ans))