from math import *
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n * multiplier) / multiplier
def calc_fuel(mass):
    fuel=int((mass//3)-2)
    return fuel
suma=0
with open('input.txt') as file:
   for line in file:
        mass=int(line)
        fuel=int((mass//3)-2)
        suma=suma+fuel;
        while(fuel>=0):
            print(fuel)
            fuel=calc_fuel(fuel)
            suma=suma+fuel
            
print(suma)
