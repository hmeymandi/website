from datetime import *

time2=time(10,5)
time3=time(12,10)
time1=date.today()
time= datetime.combine(time1, time3) - datetime.combine(time1, time2)

print(time)