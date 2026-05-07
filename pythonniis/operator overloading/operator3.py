class Mycomplex:
	def _init_(self,r,i):
		self.__r=r
		self.__i=i
	def show(self):
		print(self._r,"+",self._i,"i")
c1=Mycomplex(2,3)
c2=Mycomplex(3,4)
c3=Mycomplex(0,0)
#c3=c1+c2  error
#c3._r=c1.r+c2._r error
#c3._i=c1.i+c2._i  error
c1.show()
c2.show()
c3.show()
