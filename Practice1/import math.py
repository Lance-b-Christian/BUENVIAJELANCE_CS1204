import math

n = float(input("Diameter of the sphere: ")) 
r = n/2 
surface_area = (4 * math.pi * (r ** 2)) 
print (f"Surface Area is {surface_area:.4f}") 

volume = ((4/3) *math.pi * (r**3) )
print (f"Volume is {volume:.4f}")
