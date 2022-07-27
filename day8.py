print("***************practice day-8*************")
class A:
    def __init__(self):
        self._a=14          #private keyword
class B(A):  
    def __init__(self):
        A.__init__(self)
        print(self._a)
obj.B()
class A:
    __a=10               #protected keyword
    def __sum(self):
        print(self.__a)
    def display(self):
        print ('A')
        obj.__sum()
obj=A()
obj.display()
print("************getter and setter classes*************")
class A:
    __songname=""
    def setsongname(self,songname):
        self.__songname=songname
    def getsongname(self):
        return self.__songname
ob=A()
ob.setsongname("hey")
print(ob.getsongname())
print("***********abstract class**********")
from abc import ABC,abstractmethod
class student(ABC):
    @abstractmethod    #decorator
    def m1(self):
        pass
class A(student):
    def m1(self):
        print("hello")
ob=A()
ob.m1()
print("***********exception handling***************")
def fun(a):
	if a < 4:
		b = a/(a-3)
	print("Value of b = ", b)
	
try:
	fun(4)
	fun(5)
except ZeroDivisionError:           #try having more than one except statement
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:         #try with else block
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
try:
	k = 5//0
	print(k)
except ZeroDivisionError:
	print("Can't divide by zero")

finally:       #using finally block
	print('This is always executed')
try: 
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise 



