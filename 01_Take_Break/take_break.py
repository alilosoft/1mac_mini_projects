import webbrowser
import time

times = 5
print "Start working on: " + time.ctime()
while times > 0:
    webbrowser.open("https://classroom.udacity.com/courses/ud004-track-1mac")
    time.sleep(25 * 60)
    print "Time for break!"
    webbrowser.open("https://www.youtube.com/watch?v=1g5wM-YSNHo")
    time.sleep(5 * 60)
    times -= 1

