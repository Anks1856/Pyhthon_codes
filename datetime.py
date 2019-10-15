from datetime import datetime,time

# a = time(11,12,12)
a = datetime.now()
print (">>>>>>>>>>>", a)
b = a.strftime('%Y-%B-%d')
print(b)
