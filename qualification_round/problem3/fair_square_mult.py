#!/usr/bin/env python

from multiprocessing import Process, Manager
import fileinput, itertools, multiprocessing, math, time

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class FairSquare:
    __debug = False

    def __checkPalindrome(self, inNum):
        n = inNum;
        rev = 0;
        while (n > 0):
            dig = n % 10
            rev = rev * 10 + dig
            n /= 10

        return inNum == rev

    def __init__(self, inCase, inMin, inMax, result):
        sqrMin = int(math.ceil(math.sqrt(inMin)))
        sqrMax = int(math.floor(math.sqrt(inMax)))

        total = 0
        for number in xrange(sqrMin, sqrMax + 1):
            if self.__checkPalindrome(number) and self.__checkPalindrome(number ** 2):
                total += 1

        result.append("Case #%d: %d" % (inCase, total))

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]
    cpus = multiprocessing.cpu_count()

    result = Manager().list()
    case = 1
    for problem in lines[1:]:
        problemInfo = map(int, problem.split())

        p = multiprocessing.Process(target = FairSquare, args = (case, problemInfo[0], problemInfo[1], result))
        p.start()

        case += 1

        while len(multiprocessing.active_children()) >= cpus:
            time.sleep(0.1)

    print '\n'.join(result)
