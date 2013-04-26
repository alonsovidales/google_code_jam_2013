#!/usr/bin/env python

import multiprocessing, math, fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class FairSquareMiner:
    """
    Use this class to create a file with all the possible inputs out of
    the contest necessary time
    """
    __debug = False

    def __reverseNumber(self, n):
        rev = 0;
        while (n > 0):
            dig = n % 10
            rev = rev * 10 + dig
            n /= 10

        return rev

    def __init__(self, inCase, inFrom, inTo):
        sqrMin = int(math.ceil(math.sqrt(inFrom)))
        sqrMax = math.floor(math.sqrt(inTo))

        toLeftCheck = math.sqrt(sqrMax)

        num = sqrMin
        total = 0
        while num <= toLeftCheck:
            revStrPatern = '%0' + str(len(str(num))) + 'd'

            toTest = long("%d%s" % (num, revStrPatern % (self.__reverseNumber(num))))

            palindNum = toTest ** 2
            if palindNum == self.__reverseNumber(palindNum):
                total += 1

            for count in xrange(0, 10):
                toTest = long("%d%d%s" % (num, count, (revStrPatern % (self.__reverseNumber(num)))))
                palindNum = toTest ** 2
                if palindNum == self.__reverseNumber(palindNum):
                    total += 1

            num += 1

        print "Case #%d: %d" % (inCase, total)

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    case = 1
    for problem in lines[1:]:
        problemInfo = map(int, problem.split())

        FairSquareMiner(case, problemInfo[0], problemInfo[1])
        case += 1
