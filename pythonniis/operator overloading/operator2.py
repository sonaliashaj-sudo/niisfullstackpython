class MyTime:
    def _init_(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def show(self):
        print(self.h,":",self.m,":",self.s)
t1=MyTime(5,40,15)
t2=MyTime(4,45,55)
t3=MyTime(0,0,0)

t3.s=t1.s+t2.s
t3.m=t1.m+t2.m+t3.s//60
t3.s=t3.s%60
t3.h=t1.h+t2.h+t3.m//60
t3.m=t3.m%60
t1.show()
t2.show()
t3.show()