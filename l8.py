d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {5:50,6:60}
d1[8] = 80 
ans = {}

ans.update(d1)
ans.update(d2)
ans.update(d3)

print(ans) 