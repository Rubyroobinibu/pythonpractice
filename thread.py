import threading
import time
def cubes():
    for i in range(1,10):
        print(i**3,end=' ')
        time.sleep(2)
        print()
        
def sq():
    for i in range(1,10):
        print(i**2,end=' ')
        time.sleep(4)
        print()
        
if __name__ == '__main__':
    #creating threads
    t1=threading.Thread(target=cubes, args=())
    t2=threading.Thread(target=sq, args=())
    #start the threads
    t1.start()
    t2.start()
    print(t1.is_alive())
    
#     print("thread count: {}".format(threading.activeCount()))
#     t1.setname("thread 1")
#     t1.getname()
    
    #join -- t1 t2 combinely runs only aftr that main for loop gets exec
    t1.join()
    t2.join()
    

    for i in range(1,10):
        print(i,end=' ')
    print(t1.is_alive())
        