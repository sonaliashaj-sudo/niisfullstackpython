class Mycomplex:
	def _init_(self,r,i):
		self.__r=r
		self.__i=i
	def show(self):
		print(self._r,"+",self._i,"i")
	def _add_(self,c2):
		c3=Mycomplex(0,0)
		c3._r=self.r+c2._r
		c3._i=self.i+c2._i
		return c3
c1=Mycomplex(2,3)
c2=Mycomplex(3,4)
c3=c1+c2  #c1.add(c2)
c1.show()
c2.show()
c3.show()