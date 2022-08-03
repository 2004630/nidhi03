print("*************PRACTICE DAY-16*************")
print("***********MULTI-THREADING***************")
print("****procedural way of multi-threading for one function******")
from threading import*
def f1(n):
    for x in range(n):
        print(current_thread().name,x)
t1=Thread(target=f1,args=[5],name='thread1')     #creating a thread of f1
t1.start()
print(current_thread().name)     #by default mainthread
print("********procedural approach for two functions*********")
from threading import*
def f1(n):
    for x in range(n):
        print(current_thread().name,x)
def f2():
    for x in range(6,10):
        print(current_thread().name,x)
t1=Thread(target=f1,args=[5],name='thread1')     #creating a thread of f1
t1.start()
t2=Thread(target=f2,name='thread2')              #creating a thread of f2
t2.start()
print(current_thread().name)
print("**********using sleep function in multi-threading*********")
from threading import*
import time
def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start=time.time()
def f2():
    for x in range(6,10):
        time.sleep(3)
        print(current_thread().name,x)
end=time.time()
t1=Thread(target=f1,args=[5],name='thread1')     #creating a thread of f1
t1.start()
t1.join()       #join() blocks the another process until the called function terminates
t2=Thread(target=f2,name='thread2')              #creating a thread of f2
t2.start()
t2.join()
print(current_thread().name)
print("time taken:",end-start)
print("********class approach of multi-threading with extending the class thread************")
from threading import*
class A(Thread):
    def run(self):     #inbuilt run function of class thread
        for x in range(5):
            print(x)
ob=A()
t1=Thread(target=ob.run)
t1.start()             #no need to call run function becoz it is not callable
print("********class approach of multi-threading without extending the class thread************")
from threading import*
class A():
    def run(self):
        for x in range(5):
            print(x)
ob=A()
t1=Thread(target=ob.run)
t1.start()
print("**********using daemon thread***********")
from threading import*
import time
def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start=time.time()
def f2():
    for x in range(6,10):
        time.sleep(3)
        print(current_thread().name,x)
end=time.time()
def f3():
     while True:
         print('hello')
t1=Thread(target=f1,args=[5],name='thread1')     #creating a thread of f1
t1.start()
t1.join()       #join() blocks the another process until the called function terminates
t2=Thread(target=f2,name='thread2')              #creating a thread of f2
t2.start()
t2.join()
t3=Thread(target=f3,name='thread3',daemon=True)
t3.start()
print(t3.isDaemon())
print(current_thread().name)
print("time taken:",end-start)


