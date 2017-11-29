name = "Curtis"
print("Hello world, my name is " + name + " this is my first github push!")
print(" I am learning computer science. I am excited to see where this journey takes me! Here we go!")


class Student(object):
	def __init__(self, name, age):
		self.age = age
		self.name = name

	

c = Student(name="Curtis", age=20)
print(c.name)
print(c.age)
print(type(c))

s2 = Student(name="Kira", age=14)
print(s2.name)
print(s2.age)