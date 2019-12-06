from numpy import loadtxt
import re

# Transforms the input into an array of integers
def to_ints_array(input, delimiter=' '):
    array = loadtxt(input, delimiter=delimiter)
    return list(map(int, array))

# Transforms the input (separated by comma) into an array of strings
def to_strings_array(input):
    data=[]
    with open(input) as file:
        for line in file.readlines():
            data.append(line.split(','))
    return data

# Restore a intcode computer with a 1202 Error or change the 1 and 2 addresses
def restore(intcode, noun=12, verb=2):
    intcode[1] = noun
    intcode[2] = verb
    return intcode

# Run programs from intcode computers after restoring
def run(intcode):
    pc = 0
    opcode = intcode[pc]
    while (opcode != 99):
        if (opcode == 1):
            intcode[intcode[pc+3]] = intcode[intcode[pc+1]] + intcode[intcode[pc+2]]
        elif (opcode == 2):
            intcode[intcode[pc+3]] = intcode[intcode[pc+1]] * intcode[intcode[pc+2]]
        else:
            print('Something went wrong.')
            break
        pc += 4
        opcode = intcode[pc]
    return intcode

def abs_difference_2D(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

# Return a list of tuples from a list of directions in strings (taxonomy)
def strings_to_lines(x):
    tuples_list = []
    prev = (0, 0)
    current = (0,0)
    for coordinate in x:
        direction = re.split('\d', coordinate)[0]
        length = int(re.split('\D', coordinate)[1])
        if direction == 'R':
            current = (length + current[0], prev[1])
        elif direction == 'L':
            current = (-length + current[0], prev[1])
        elif direction == 'U':
            current = (prev[0], length + current[1])
        elif direction == 'D':
            current = (prev[0], -length + current[1])
        else:
            print("Direction invalid.")
        tuples_list.append([prev, current])
        prev = current
    return tuples_list

# Find determinant of two tuples
def det(a, b):
    return a[0] * b[1] - a[1] * b[0]