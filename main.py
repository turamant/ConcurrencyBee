from threading import Thread
import time

def countdown(n):
    while n > 0:
        print("Time-minus", n)
        n -= 1
        time.sleep(1)
        print("Time-plus", n)



if __name__ == '__main__':
    t = Thread(target=countdown, args=(10,))
    #t1 = Thread(target=countdown, args=(7,))
    t.start()
    #t1.start()
    if t.is_alive():
        print('still running')
    else:
        print("Finished")
    print("Major thread main finished")

