print("*****************************practice day-5*************************")
'''x=10  #globalvariable
def f1():
    a=20    #local variable
    b=30
    print(a+b)
f1()
def f1():
    x=30
    global x
    print(x)
f1()
def f1(a,b):
    print(a+b)
f1(8,7)
def f1():
    x=20
    global x
    print(x)
f1()
print(x)
a=10
def f1():
    print('f1',a)
def g():
    a=20
    print('g',a)
def h():
    a=30
    global a
    print('h',a)
print('glo',a)
f1()
print('glo',a)
g()
print('glo',a)
h()
print('glo',a)'''
def f1():
    a=10
    def f2():
        print('hello')
        nonlocal a
        a=40
        print(a)
    f2()
f1()
    
