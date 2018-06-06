import webbrowser
import time

times = 5
print "Start working on: " + time.ctime()
while times > 0:
    print "It's time for work!"
    time.sleep(25 * 60)
    print "Now, It's time to take a break!"
    webbrowser.open("https://www.youtube.com/watch?v=1g5wM-YSNHo")
    time.sleep(5 * 60)
    times -= 1

