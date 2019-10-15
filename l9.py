from l8 import d1
print(d1)
a = {1:10,2:20,3:30,4:40,5:50}


sum = 0
mul = 1  
for i in a.values() :
    sum+=i
    mul*=i
print(sum) 
print(mul)
# print(sum(a.values()))
