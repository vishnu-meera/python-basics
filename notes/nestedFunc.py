
def f(a):
	def g(b):
		def h(c):
			def i(d):
				return a * b * c * d ;
			return i
		return h
	return g

print(f(4)(3)(2)(5))