from math import *
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n * multiplier) / multiplier
suma=0
with open('input.txt') as file:
   for line in file:
        mass=int(line)
        fuel=round_down((mass/3))-2
        suma+=fuel
print(suma)
       
