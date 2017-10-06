class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.speed = speed
		self.fuel = fuel
		self.mileage = 0
		self.price = price
		if price > 10000:
			self.tax = .15
		else:
			self.tax = .12
		self.display_all()

	def display_all(self):
		print "Price" + str(self.price)
		print "Speed" + str(self.speed)
		print "Fuel" + self.fuel
		print "Milage" + str(self.milage) + 'MPG'
		print "Tax" + str(slef.tax)

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(10000, 5, 'Not Full', 105)
car3 = Car(2000, 75, 'Kind Of Full', 95)
car4 = Car(6000, 55, 'Full', 15)
car5 = Car(4000, 22, 'E', 15)
car6 = Car(80000, 100, '3/4', 15)