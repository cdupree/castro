 #!/usr/bin/env python3

import math

# decorator to convert functions which take radians into functions which accept
# degrees instead.
def convert_degrees(function):
    def new_function(angle):
        return function(math.radians(angle))
    return new_function

# decorator to convert functions which return radians into functions which 
# return degrees. The option 2nd argument of the function is used in
# atan2(y,x) which returns the angle corresponding to tan(y,x) within
# the proper coordinate based on the signs and values of x, and y.
def convert_radians(function):
    def new_function(measurement, measurement2=None):
        if measurement2 == None:
            return math.degrees(function(measurement))
        else:
            return math.degrees(function(measurement,measurement2))
    return new_function
        
@convert_degrees
def SN(angle):
    return math.sin(angle)

@convert_degrees
def CS(angle):
    return math.cos(angle)

@convert_degrees
def TN(angle):
    return math.tan(angle)

@convert_radians
def ASN(measurement):
    return math.asin(measurement)

@convert_radians
def ACS(measurement):
    return math.acos(measurement)

@convert_radians
def ATN(measurement):
    return math.atan(measurement)

@convert_radians
def ATN2(measurement, measurement2):
    return math.atan2(measurement, measurement2)

def CUBR(x):
    if x == 0.0:
        return x
    else:
        return math.exp(math.log(x)/3.0)
