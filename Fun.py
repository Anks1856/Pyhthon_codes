import webbrowser
import random
import time

while True:
    sites = random.choice(['youtube.com','facebook.com','pixels.com','gmail.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(2,8)
    time.sleep(seconds)