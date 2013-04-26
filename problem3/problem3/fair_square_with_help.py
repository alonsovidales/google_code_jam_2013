#!/usr/bin/env python

import fileinput, math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class FairSquare:
    __debug = False

    def resolve(self, inMin, inMax):
        sqrMin = int(math.ceil(math.sqrt(inMin)))
        sqrMax = int(math.floor(math.sqrt(inMax)))

        total = 0
        for num in self.__fairSqrNum:
            if num > sqrMax:
                return total

            if num >= sqrMin:
                total += 1
                
        return total

    def __init__(self):
        self.__fairSqrNum = []
        for number in open('total', 'r').read().split('\n'):
            if number != '':
                self.__fairSqrNum.append(int(number))

        self.__fairSqrNum = sorted(self.__fairSqrNum)

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    fairSquare = FairSquare()

    case = 1
    for problem in lines[1:]:
        problemInfo = map(int, problem.split())
        print "Case #%d: %d" % (case, fairSquare.resolve(problemInfo[0], problemInfo[1]))

        case += 1
