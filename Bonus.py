def factorial(n):
    if n == 1:
        return(1)
    fac = factorial(n-1)
    return n*fac
print(factorial(7))


#
class Car:
    def __init__(self,color):
        print(color)
        #self.color

    def add_wheel(self):
        Car.wheels += 1

car_1= Car('white')
car_2= Car('blue')

print (car_1.color)