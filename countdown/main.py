import time
def  countdown(t):
    while t:
        mins , secs = divmod(t, 60)
        timer = '{:02}:{:02}'.format(mins,secs)
        print(timer,end = '\r')
        time.sleep(1)
        t-= 1

    print('Timer Completed!')
t = input('Enter The time in seconds')
countdown(int(t))