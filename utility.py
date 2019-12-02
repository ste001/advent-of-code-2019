from numpy import loadtxt

# Transforms the input into an array of integers
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