import time

def pomodoro(): 
  print("Pomodoro starts now!")
  for i in range(4):
    t = 25*60
    while t: 
      mins = t // 60 
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(timer, end="\r") 
      t -= 1 
    print("stop")

    t = 5*60 
    while t: 
      mins = t // 60 
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(timer, end="\r") 
      time.sleep(1)
      t -= 1 
    print("start")

pomodoro()