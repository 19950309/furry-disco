class Car():
    def __init__(self, make, model, year):
        self.make =make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+ ' '+ self.make + ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print('this car has '+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer')

    def increment_odometer(self, miles):
        self.odometer_reading+=miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model, year)
        self.battery_size = Battery()

    def read_odometer(self):
        print("this car doesn't need gas")
class Battery:
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size


    def describe_battery(self):
        print('This car has a ' + str(self.battery_size))
my_tesla = ElectricCar('TESLA','model_s',2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()

class a:
    def hi(self):
        print('a.hello')

class b(a):
    def hi(self):
        print('b hello')

class c(a):
    def hi(self):
        print('c hello')

class d(b,c):
    pass

if __name__ == '__main__':
    d = d()
    d.hi()