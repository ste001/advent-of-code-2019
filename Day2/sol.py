from numpy import loadtxt

# Export to utility.py
def to_ints_array(input, delimiter=' '):
    array = loadtxt(input, delimiter=delimiter)
    return list(map(int, array))

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

intcode = to_ints_array('./input.txt', ',')
og_intcode = intcode[:]

# Part 1
intcode = restore(intcode)
intcode = run(intcode)
print('Position 0 is: ' + str(intcode[0]))

# Part 2
solutions = []
for i in range(0, 100):
    for j in range (0, 100):
        intcode = og_intcode[:]
        intcode = restore(intcode, i, j)
        intcode = run(intcode)
        if (intcode[0] == 19690720):
            solutions.append(i)
            solutions.append(j)
            break
print('The output is provided by: ' + str(100*solutions[0]+solutions[1]))
