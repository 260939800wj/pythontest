# -*- coding: cp936 -*-
'''
#1���򵥵�װ����
def play():
    print ("hello world!")

def outer(func):
    print "****************"
    func()

outer(play)


'''
'''
#2�����غ�����װ����

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



#3����������װ����

def sum(a,b):
    print "�������ǣ�"
    return a + b

def outer(func):
    def inner(*args,**kwargs):
        print "�����%d+%d�ĺ���:"
        return func(*args,**kwargs)
    return inner
a = outer(sum)
print a(1,3)



#4��@װ����

def outer(func):
    def inner(*args,**kwargs):
        print "�����%d+%d�ĺ���:"
        return func(*args,**kwargs)
    return inner
    
@outer
def sum(a,b):
    print "�������ǣ�"
    return a + b

p = sum(1,8)
print p

#funA ��Ϊװ��������
def funA(fn):
    print("C����������")
    fn() # ִ�д����fn����
    print("http://c.biancheng.net")
    #return "װ���������ķ���ֵ"
@funA
def funB():
    print("ѧϰ Python")

#print(funA)
print(funB)
'''
#5��@װ�������в���

def outer(func):
    def inner(*args,**kwargs):
        print "�����%d+%d�ĺ���:"
        return func(*args,**kwargs)
    return inner

@outer #a = outer(sum)(1,5)
def sum(a,b):
    print "�������ǣ�"
    return a + b

sum(1,5)

