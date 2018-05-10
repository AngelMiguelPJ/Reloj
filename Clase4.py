import time

print (time.localtime(),"\n")


for x in range(1,61):
  t = time.localtime()
  hour = t[3]
  min = t[4]
  sec = t[5]
  print("La hora es ", hour,":" , min,":" , sec)
  time.sleep(1)




