import webbrowser
import time

breaks = 3
count = 1
print(time.ctime())
while breaks>=count:
    print('Please relax and enjoy the song')
    webbrowser.open('https://open.spotify.com/track/6wkGVfvTNqDDgeyGoYyYQ1?si=d9df0fe7f3914cfb')
    time.sleep(4*60)
    count = count + 1

    
