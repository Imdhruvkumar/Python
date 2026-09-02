class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"{self.__brand}{self.model}"

    def fuel_type(self):
        return "petrol or diesal"

    @staticmethod
    def general_descrption():
        return "car is goos with black color"



class Electric_car(Car):
    def __init__(self,brand,model,b_size):
        super().__init__(brand,model)
        self.b_size = b_size

    def fuel_type(self):
        return "charge"




my_car = Car("toyoto","corola")
new_car = Electric_car("tesla","model","86ksd")

# print(new_car.__brand)
# print(new_car.model)
# print(new_car.b_size)
# print(new_car.fuel_type())
# print(new_car.get_brand())


# print(my_car.brand)
# print(my_car.model)
# print(my_car.fuel_type())
# print(my_car.total_car) 
# print(Car.total_car)
# print(my_car.general_descrption())
# print(Car.general_descrption())


# my_new_car = Car("fararri","cruse")
# print(my_new_car.brand)
# print(my_new_car.model)