#this pgm plays a video after every 2 hours from the time when you start runnning the pgm
#usecase - use this while working for long hours - so that it will play your favuorite video
#after

import time
import webbrowser

frequency=int(input("After how many hours you want to take break"))
no_of_breaks=int(input("How many breaks you want take ?"))
print("current time is ",time.ctime()," \nFrom Now onwards your favourtite video will be played after every two hours")
x=0
while (x < no_of_breaks):
    time.sleep(frequency*60*60)
    x=x+1
    webbrowser.open("https://www.youtube.com/watch?v=DQ4mraAx23I")

