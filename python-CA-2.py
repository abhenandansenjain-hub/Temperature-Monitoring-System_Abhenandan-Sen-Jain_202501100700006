import random
import time
max=int(input("Enter maximum temperature in Celcius : "))
min=int(input("Enter minimum temperature in Celcius : "))
timt=int(input("Enter runtime : "))
mean=0
for i in range(timt//2):
  a=random.randint(min,max);
  print("READING",i," : The temperature is :",float(a),"C")
  mean=mean+a
  time.sleep(2)
print("Experimental value obtained :",mean/(timt//2),"C");
