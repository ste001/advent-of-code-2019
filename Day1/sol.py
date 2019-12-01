import math

def input_to_array(input):
    inputArray = []
    f = open(input, 'r')
    with open(input) as f:
        for line in f:
            inputArray.append(line.rstrip('\n'))
    return inputArray

def module_fuel(mass):
    return int(mass) // 3 - 2

def module_fuel_recursive(mass):
    fuel = int(mass)
    total_fuel = 0
    while (fuel // 3 - 2 > 0):
        fuel = fuel // 3 - 2
        total_fuel += fuel
    return total_fuel

masses = input_to_array('./input.txt')
total_fuel = 0
for mass in masses:
    fuel = module_fuel(mass)
    total_fuel += fuel
print('Total fuel is: ' + str(total_fuel))
total_fuel = 0
for mass in masses:
    fuel = module_fuel_recursive(mass)
    total_fuel += fuel
print('Real total fuel is: ' + str(total_fuel))

    