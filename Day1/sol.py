from numpy import loadtxt

def module_fuel(mass):
    return int(mass) // 3 - 2

def module_fuel_recursive(mass):
    fuel = int(mass)
    total_fuel = 0
    while (fuel // 3 - 2 > 0):
        fuel = fuel // 3 - 2
        total_fuel += fuel
    return total_fuel

masses = loadtxt('./input.txt')
total_fuel = 0
# Part 1
for mass in masses:
    fuel = module_fuel(mass)
    total_fuel += fuel
print('Total fuel is: ' + str(total_fuel))
# Part 2
total_fuel = 0
for mass in masses:
    fuel = module_fuel_recursive(mass)
    total_fuel += fuel
print('Real total fuel is: ' + str(total_fuel))
