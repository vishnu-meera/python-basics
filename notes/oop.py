import math

class Complex:
	'this class simulates complex numbers'
	def __init__(this,real=0,imaginary=0):
		if(type(real) not in (int,float) or type(imaginary) not in (int,float)):
			raise Exception('Args should be numbers')
		this.SetImag(imaginary)
		this.SetReal(real)
	
	def SetReal(this,val):
		if(type(val) not in (int,float)):
			raise Exception('Args should be numbers')
		this.__real = val
	
	def SetImag(this,val):
		if(type(val) not in (int,float)):
			raise Exception('Args should be numbers')
		this.__imaginary = val
	
	def GetReal(this):
		return this.__real
	
	def GetImag(this):
		return this.__imaginary

	def __str__(this):
		return str(this.GetReal()) + '+' + str(this.GetImag()) + 'i'

	def __add__(this,other):
		return Complex(this.GetReal()+other.GetReal(),this.GetImag()+other.GetImag())

	def __mul__(this,other):
		if(type(other) in (int,float)):
			a,b,c,d = this.GetReal(),this.GetImag(),other,0
		else:
			a,b,c,d = this.GetReal(),this.GetImag(),other.GetReal(),other.GetImag()
		r = a*c - b*d
		i = a*d + b*c
		return Complex(r,i)


	def __truediv__(this,other):
		if(type(other) in (int,float)):
			a,b,c,d = this.GetReal(),this.GetImag(),other,0
		else:
			a,b,c,d = this.GetReal(),this.GetImag(),other.GetReal(),other.GetImag()
		r = a*c - b*d
		i = a*d + b*c
		conjugate = c*c + d*d
		return Complex(r/conjugate,i/conjugate)

try:
	c = Complex(1,3)
	#print(c)
	#print(c.__real)
	#print(c.__imaginary)
	d=Complex()
	#print(d)
	d.SetImag(2)
	d.SetReal(2)
	print(d.GetImag())
	print(d.GetReal())	
	#print(d.__real) ->will say no such value
	#print(d.__imaginary)
	print(c+d)
	print(c*d)
	print(c*2)
	print(c/d)
	#print (Complex)
except Exception as e:
	print(e)

