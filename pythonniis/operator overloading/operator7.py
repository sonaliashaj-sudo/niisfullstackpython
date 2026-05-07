class Demo:
	def show(self,a=0,b=0):
		if a!=0 and b!=0:
			print("two argument show",a,b)
		elif a!=0:
		    print("one argument show",0)
		else:
		    print("no argument show")
d=Demo()
d.show()
d.show(10)
d.show(10,20)		         	