from datetime import dateutil.relativedelta

a = datetime.now()
b = a + timedelta(days=10)
c = a - dateutil.relativedelta(months=1)
print(b)
print(c)