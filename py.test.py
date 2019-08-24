import sys
print(sys.executable)
print(sys.version)
print("Hello")

class Employee:
	def __init__(self,first,last):
		self.first = first
		self.last  = last
		@property
		def foo(self):
			return self._foo
		@property
		def fullname(self):
			return '{} {}'.format(self.first,self.last)
        
     emp_1 = Employee('John','Smith')


     print(emp_1.first)
     print(emp_1.last)
     print(emp_1.fullname)
		