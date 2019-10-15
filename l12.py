a = [1,2,3,4,5,6]
b = [10,20,30,40,50,60]

ans = {}
for i in a:
    ans[i] = b[i-1]

#ans[i] for i in a = x for x in b
    
print(ans)    
    