#base class
class Cars:
	def __init__(self,price,fuel,company,gear):
		self.price=price
		self.fuel=fuel
		self.company=company
		self.gear=gear

	def GetPrice(self):
		return self.price

	def GetFuel(self):
		return self.fuel

	def GetManufacturer(self):
		return self.company

	def GetGear(self):
		return self.gear

	def GetCarType(self):
		pass

#child class
class SportsCar(Cars):
	def __init__(self,price,fuel,company,gear,seats,maxspeed):
		self.price=price
		self.fuel=fuel
		self.company=company
		self.gear=gear
		self.seats=seats
		self.maxspeed=maxspeed 	

	def NumberOfSeats(self):
		return self.seats

	def MaxSpeedInMph(self):
		return self.maxspeed

	def GetCarType(self):
		return 'SportsCar'

#child class
class Saloon(Cars):
	def __init__(self,price,fuel,company,gear,seats,milege):
		self.price=price
		self.fuel=fuel
		self.company=company
		self.gear=gear
		self.seats=seats
		self.milege=milege 	

	def NumberOfSeats(self):
		return self.seats

	def MilegePerGallon(self):
		return self.milege

	def GetCarType(self):
		return 'Saloon'


try:
	#print(Cars)
	#print(Saloon)
	#print(Saloon)
	mustang = SportsCar('$37K','gas','Ford','Auto','4',150)
	prius	= Saloon('$24K','hybrid','Toyota','Auto','4-6',40)
	mx5 	= SportsCar('$26K','gas','Mazda','Auto','2',180)
	accord	= Saloon('$21K','gas','Honda','Auto','4',28)

	#print(mustang)
	#print(prius)
	#print(mx5)
	#print(accord)
	for v in [mustang,prius,mx5,accord]:
		print(v)
		print(v.GetManufacturer(),v.GetCarType())
except Exception as e:
	print(e)