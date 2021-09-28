class A:
    def __init__(self,x):
        self.x=x
    
    @staticmethod
    def func(a,b):

        print(a+b)
        
A.func(2,3)

op=A(0)
op.func(5,3)
print('--------')
class D:
    def __init__(self,x):
        self.x=x
    @classmethod
    def test(cls,s):
        print(s+2)
        return cls(s)


ob=D(50)
ob.test(5)
D.test(2)
print(ob.test(50).x)


date=('2021-10-1')
yr,b,c=list( map(int,date.split('-')))
print(yr,b,c)
print('--------------')

class Person:
    a=50
    def __init__(self,x,y):
        self.x=x
        self.y=y
 
    def add(self):
        return self.x+self.y

    @classmethod
    def z(cls,s):
        return (cls.a*s)
    @staticmethod
    def v(c,m):
        return (c-m)
    @property
    def me(self):
        return(self.x,self.y+1)

    @me.setter
    def me(self,t):
        self.x,self.y=t



op=Person(10,5)
print(op.add())
print(op.z(5))
print(op.v(10,5))
print(op.me)
op.me=(5,6)
print(op.me)