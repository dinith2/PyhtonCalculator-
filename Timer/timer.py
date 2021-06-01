import time 

t=int(input("number of second you want to count down to"))

while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end = "/r")