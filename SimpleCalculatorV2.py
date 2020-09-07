import time
#Ask the user how much time the want
hour=int(input("Enter how many hours you want: "))
min=int(input("Enter how many minutes you want: "))
sec=int(input("Enter how many seconds you want: "))

h=0

m=0
s=0
#Run the timer
for i in range(sec):
    time.sleep(1)
    s+=1
for k in range(min):