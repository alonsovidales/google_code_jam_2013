#!/usr/bin/env python

import multiprocessing, math

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

    def __init__(self, inFrom, inTo):
        sqrMin = int(math.ceil(math.sqrt(inFrom)))
        sqrMax = math.floor(math.sqrt(inTo))

        toLeftCheck = math.sqrt(sqrMax)

        num = sqrMin
        while num <= toLeftCheck:
            revStrPatern = '%0' + str(len(str(num))) + 'd'

            toTest = long("%d%s" % (num, revStrPatern % (self.__reverseNumber(num))))

            palindNum = toTest ** 2
            if palindNum == self.__reverseNumber(palindNum):
                print toTest

            for count in xrange(0, 10):
                toTest = long("%d%d%s" % (num, count, (revStrPatern % (self.__reverseNumber(num)))))
                palindNum = toTest ** 2
                if palindNum == self.__reverseNumber(palindNum):
                    print toTest

            num += 1

        print "From: %s to %s" % (sqrMin, sqrMax)

# Calculate all the possible values
FairSquareMiner(1, 10 ** 100)
