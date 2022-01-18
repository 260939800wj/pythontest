# -*- coding: cp936 -*-
'''
#1、简单的装饰器
def play():
    print ("hello world!")

def outer(func):
    print "****************"
    func()

outer(play)


'''
'''
#2、返回函数的装饰器

def play():
    print ("hello world!")

def outer(func):
    print 11111
    def inner():
        print "@@@@@@@@@@@@"
        func()
        print "%%%%%%%%%%%%%%%%%%%%%%"
    return inner()
outer(play)



#3、带参数的装饰器

def sum(a,b):
    print "请计算和是："
    return a + b

def outer(func):
    def inner(*args,**kwargs):
        print "请计算%d+%d的和是:"
        return func(*args,**kwargs)
    return inner
a = outer(sum)
print a(1,3)



#4、@装饰器

def outer(func):
    def inner(*args,**kwargs):
        print "请计算%d+%d的和是:"
        return func(*args,**kwargs)
    return inner
    
@outer
def sum(a,b):
    print "请计算和是："
    return a + b

p = sum(1,8)
print p

#funA 作为装饰器函数
def funA(fn):
    print("C语言中文网")
    fn() # 执行传入的fn参数
    print("http://c.biancheng.net")
    #return "装饰器函数的返回值"
@funA
def funB():
    print("学习 Python")

#print(funA)
print(funB)
'''
#5、@装饰器后有参数

def outer(func):
    def inner(*args,**kwargs):
        print "请计算%d+%d的和是:"
        return func(*args,**kwargs)
    return inner

@outer #a = outer(sum)(1,5)
def sum(a,b):
    print "请计算和是："
    return a + b

sum(1,5)

