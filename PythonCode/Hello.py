from math import sqrt
def quadratic(a,b,c):
	deta = sqrt(b*b-4*a*c)
	m = ((0-b)+deta)/2*a
	n = ((0-b)-deta)/2*a
	return m,n 
	
q = quadratic(1,2,-3)
print(q)