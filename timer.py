import time

def countdown(seconds):

    while seconds>0:
        min= int(seconds/60)
        sec = int(seconds%60)

        timer = f"{min}:{sec}"
        print(timer)

seconds = input("Enter time in seconds:")

countdown(int(seconds))