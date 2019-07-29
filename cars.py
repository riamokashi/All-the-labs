from google.appengine.ext import ndb


class Car(ndb.Model):
    carMake = ndb.StringProperty(required=True)
    carModel = ndb.StringProperty(required=True)

    def printCarInfo(self):
        print(self.carMake + " " + self.carModel)

car1 = Car(carMake="ford", carModel="mustang")
car2 = Car(carMake="audi", carModel="r8")
car1.printCarInfo()
car2.printCarInfo()

all_cars = Car.query().fetch()
print(all_cars)
print(all_cars[0])
print(all_cars[0].carMake)
