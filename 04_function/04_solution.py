import math

def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumfrence = 2 *  math.pi * radius
    return area,circumfrence

a,c = circle_stats(2)

print(math.floor(a)  ,  math.floor(c))