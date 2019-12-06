import sys
sys.path.append('../')
from utility import *

def check(n):
    return list(n) == sorted(n) and 2 in map(n.count, n)

if __name__ == "__main__":
    with open('./input.txt') as file:
        rangeLower, rangeUpper = file.readline().split('-')
        passwordsCounter = 0
        for number in range(int(rangeLower), int(rangeUpper)):
            duplicateFound = False
            increment = True
            prev = 0
            for num in str(number):
                if int(num) == prev:
                    duplicateFound = True
                if (int(num) < prev):
                    increment = False
                prev = int(num)
            if duplicateFound and increment:
                passwordsCounter += 1
        print('There are',str(passwordsCounter),'passwords in this range.')

    with open('./input.txt') as file:
        rangeLower, rangeUpper = file.readline().split('-')
        passwordCounter = 0
        for n in range(int(rangeLower),int(rangeUpper)):
            if check(str(n)):
                passwordCounter += 1
        print('There are',str(passwordsCounter),'real passwords in this range.')