class Student:
  count = 0
  number = 50

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sayhello(self):
    print(str(Student.number) + ' is ' + self.name)

#a= Student('bob', 54)
#a.sayhello()
  @staticmethod
  def add(a,b):
    print(Student.number)
    print('{0} + {1} = {2}'.format(a,b,(a+b)))

#Student.add(2,3)

class Employee:
  def __init__(self,name,age):
    self.__name = name
    self.__age = age

  def __work(self):
    print('hard work')
e = Employee('BOB', 18)
e._Employee__work()

print(e._Employee__name)
