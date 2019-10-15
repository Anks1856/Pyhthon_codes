a = {'b':10,'a':20,'r':30,'d':40,1:50,3:80,10:100,3:30, 40:4}
b = {}
print(a['a'])
a['b'] = 40
for i in sorted(a) :
    print(i,a[i])

# print(sorted(a.items()))
#print(a)