import sys
sys.path.append('../')
from utility import *

if __name__ == "__main__": 
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
