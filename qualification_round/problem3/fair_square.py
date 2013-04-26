#!/usr/bin/env python

import fileinput, itertools, multiprocessing, math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class FairSquare:
    __debug = False

    # First of all I used this method to create a list of candidates
    def createFairNums(self, inMin, inMax):
        sqrMin = int(math.ceil(math.sqrt(inMin)))
        sqrMax = int(math.floor(math.sqrt(inMax)))

        total = 0
        number = sqrMin
        while number <= sqrMax:
            if self.__checkPalindrome(number) and self.__checkPalindrome(number ** 2):
                print number

            number += 1

    def __checkPalindrome(self, inNum):
        n = inNum;
        rev = 0;
        while (n > 0):
            dig = n % 10
            rev = rev * 10 + dig
            n /= 10

        return inNum == rev

    def resolve(self, inMin, inMax):
        sqrMin = int(math.ceil(math.sqrt(inMin)))
        sqrMax = int(math.floor(math.sqrt(inMax)))

        total = 0
        for number in xrange(sqrMin, sqrMax + 1):
            if self.__checkPalindrome(number) and self.__checkPalindrome(number ** 2):
                print number
                total += 1

        return total

    def __init__(self):
        self.__solutions = []

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    fairSquare = FairSquare()

    # Uncomment in order to create the list of candidates
    #fairSquare.createFairNums(1, 10 ** 100)

    case = 1
    for problem in lines[1:]:
        problemInfo = map(int, problem.split())
        print "Case #%d: %d" % (case, fairSquare.resolve(problemInfo[0], problemInfo[1]))

        case += 1
