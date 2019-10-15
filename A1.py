a  = {
    'id1':
    { 'name':['anks'],
      'age':19
    },
    'id2':{
        'name':['ankur'],
        'age':19
    },
    'id3':{
        'name':['anks'],
        'age':29
    }
}
b = {}
print(len(b))
if (len(b)== 0):
    print("this is empty dictnary!") 

for i,j in a.items():
    if j not in b.values():
        b[i] = j
    
        
print(b)
