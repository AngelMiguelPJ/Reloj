import time
import os, sys
print(time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)

hour = t[3]
min = t[4]
sec = t[5]
print(t[3],":", t[4],":", t[5])

#"for x in range(1,61):
  #  print(x)

#for x in range(1,61):
   # print(x)
   # time.sleep(1)

while sec<60:
    os.system("cls")
    print(hour,":",min,":",sec)
    time.sleep(1)
    sec=sec+1
    while sec>59:
        min=min+1
        sec=0
        while min>59:
            hour=hour+1
            min=0
            if hour>23:
                hour=0