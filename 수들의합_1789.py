'''
근의 공식
x = -b +- 루트(b^2-4ac) / 2a

(x**2 -x )/2= n
x**2 - x = 2n


a = 1
b = -1
c = -2n

'''
import math

n = int(input())


a=1
b=-1
c=-2*n

x1 = (-b + (b**2 - 4*a*c)**(1/2) )/ 2*a
x2 = (-b - (b**2 - 4*a*c)**(1/2) )/ 2*a

x1 = math.floor(x1)
print(x1-1)


    

