#!/usr/bin/env python

import math

def vecMag(r):
	return math.sqrt(vecDot(r,r)) 

def vecSquare(r):
	#(x, y, z) = r
	#return x*x + y*y + z*z
	return vecDot(r,r)

def vecDot(x,y):
	return x[0] * y[0] + x[1] * y[1] + x[2] * y[2]

def fgIterate8(r0, v0, mu, dt, k = 0.01720209895):

	"""Iterate an orbit with 8th order F and G series.

	This function implements ...

	mu = reduced mass = 1.00000016 
	dt = iteration step time = 2 
	r0 = tuple of x, y, z =  (0.1693419,-0.3559908,-0.2077172)
	v0 = tuple of v_x, v_y, v_z = (1.1837591,0.6697770,0.2349312)
	"""


	# modified step 
	tau = k * dt

	R = vecMag(r0)
	u = mu / (R*R*R)
	z = vecDot(r0, v0) / (R*R)
	q = vecSquare(v0) / (R*R) - u

	f2 = -1 * u / 2
	f3 = u * z / 2

	f4 = (u / 24)* (3 * q - 15 * z * z + u)

	f5 = (u * z / 8) * ( 7 * z * z - 3 * q - u)

	f6 = (u / 720) * (z * z * (630 * q + 210 * u - 945 * z * z) - u * (24 * q + u) - 45 * q * q)

	f7 = (u * z / 5040) * (z * z * (10395 * z * z - 3150 * u - 9450 * q) + u * (882 * q + 63 * u) + 1575 * q * q)

	f8 = (u / 40320) * (z * z * (z * z * (51975 * u + 155925 * q - 135135 * z * z) - u * (24570 * q + 2205 * u) -
				42525 * q * q) + q * q * (1107 * u + 1575 * q) + u * u * (117 * q + u))

	g3 = -1 * u / 6
	g4 = u * z / 4
	g5 = (u / 120) * (9 * q - 45 * z * z + u)
	g6 = (u * z / 360) * (210 * z * z - 90 * q - 15 * u)
	g7 = (u / 5040) * (z * z * (3150 * q + 630 * u - 4725 * z * z) - q * (54 * u + 225 * q) - u * u)
	g8 = (u * z / 40320) * (z * z * (62370 * z * z - 56700 * q - 12600 * u) + q * (3024 * u + 9450 * q) + 126 * u * u)

	# now the actual f and g series get calculated
	f = 1 + tau * tau * (f2 + tau * (f3 + tau * (f4 + tau * (f5 + tau * (f6 + tau * (f7 + tau * (f8)))))))
	g = tau * ( 1 + tau * tau * (g3 + tau * ( g4 + tau * (g5 + tau * (g6 + tau * (g7 + tau * (g8)))))))

	# and their derivatives
	df = tau * (2 * f2 + tau * (3 * f3 + tau * (4 * f4 + tau * (5 * f5 + tau * ( 6 * f6 + tau * (7 * f7 + tau * (8 * f8)))))))
	dg = 1 + tau * tau * (3 * g3 + tau * (4 * g4 + tau * (5 * g5 + tau * (6 * g6 + tau * (7 * g7 + tau * (8 * g8))))))

	# and now we update the position, and velocity
	r = ( f * r0[0] + g * v0[0], f * r0[1] + g * v0[1],  f * r0[2] + g * v0[2] )
	v = ( df * r0[0] + dg * v0[0], df * r0[1] + dg * v0[1],  df * r0[2] + dg * v0[2] )

	return (r,v)


print(vecMag( (3, 4, 12)))
print(vecDot( (1.0,3.0,-5.0), (4.0,-2.0,-1.0) ))
k = 0.01720209895
mu = 1.000000166
dt = 2.0
r = (0.1693419,-0.3559908,-0.2077172)
v = (1.1837591,0.6697770,0.2349312)

print("{0}     {1:+.7f}    {2:+.7f}    {3:+.7f}    {4:.7f}".format(6280.5,r[0],r[1],r[2],vecMag(r)))

for i in xrange(1,51):

	(r,v)  = fgIterate8(r, v, mu, dt)

	date = 6280.5 + dt * i
	rmag = vecMag(r)
	print("{0}     {1:+.7f}    {2:+.7f}    {3:+.7f}    {4:.7f}".format(date,r[0],r[1],r[2],rmag))

print("{0:+.7f} {1:+.7f} {2:+.7f}".format(v[0], v[1], v[2]))	

#def fgIterate8(r0, v0, mu, dt, k = 0.01720209895):
