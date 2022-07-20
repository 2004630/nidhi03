print("*****************************practice day-5*************************")
x=10  #globalvariable
def f1():
    a=20    #local variable
    b=30
    print(a+b)
f1()
print("************")
def f1():
    x=30
    global x
    print(x)
f1()
print("************")
def f1(a,b):
    print(a+b)
f1(8,7)
print("************")
def f1():
    x=20
    global x
    print(x)
f1()
print(x)
print("************")
a=10
def f1():
    print('f1',a)
def g():
    a=20
    print('g',a)
def h():
    a=30
    global a          #global keyword for accessing global variables
    print('h',a)
print('glo',a)
f1()
print('glo',a)
g()
print('glo',a)
h()
print('glo',a)
print("************")
def f1():                #outer function
    a=10
    def f2():            #inner function
        print('hello')
        nonlocal a            #nonlocal keyword for accessing outer function variable
        print(a)
    f2()
f1()
print("**************classes and objects*****************")
class demo:
    def disp(self,a,b):
        print(a+b)
ob=demo()
ob.disp(4,5)          #or demo().disp()
print("*******************constructors***********")
class a:
    def __init__(self):
        print("hello")
    def f1(self):
        print("hi")
ob=a()
ob.f1()
print("************")
class a:
    def __init__(self,a,b):
             print(a+b)
    def f1(self):
        print("hi")
ob=a(4,3)
ob.f1()
print("************")
class name:
    def __str__(slf):
        return "hello"
ob=name()
print(ob)
print("************")
class b:
    def __del__(self):
              return "hi"
    def sum(self):
        a=20
        b=30
        print(a+b)
ob=b()
ob.sum()
del ob
class name:
    a=10
    b=20
    def sum(self):
        a=12
        b=34
        print(self.a+self.b)       #self keyword to access class variables
obj1=name()
obj1.sum()
class nidhi:
    name_nid='nidz'
    age_nid=20
    default_age=19
    def default(self):
        print("this is a default method")
n=nidhi()
print("*******getattr()*********")
print(getattr(n,'name',45))
print(getattr(n,'age_nid',40))
print(getattr(n,'age_other',n.default_age))
print("******setattr()********")
n1=nidhi()
setattr(n,'sign','maddy')
print(getattr(n,'sign',45))
#print(getattr(n1,'sign')) becoz n1 has no attribute 'sign'
print(getattr(n,'age_other',n.default_age))
setattr(n,'age_nid',100)
print(getattr(n,'age_nid',45))
setattr(n1,'age_nid',0)
print(getattr(n1,'age_nid',43))
print("****************hasattr()**********)
print(hasattr(n,'name_nid'))
print(hasattr(n,'age_other'))
print("******************delattr()************")
delattr(nidhi,'name_nid')
print(hasattr(n,'name_nid'))
print(dir(n)) #to get list of attributes
print(hasattr(n,'sign'))
print(hasattr(n,'name_nid'))

    



