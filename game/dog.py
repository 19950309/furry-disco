class Dog(object):
      def __init__(self,name,age,dog_type):
        self.name = name
        self.age = age
        self.dog_type = dog_type

      def sayhi(self):
        print('my dog is a %s whose name is %s its %d years old' %(self.dog_type, self.name, self.age))

d = Dog('bob',19, 'jingmao')
d.sayhi()


def hello(mingzi, nianling=6):
  print('my dog whose name is %s its %d years old' %(mingzi,nianling))

hello('jack',4)
