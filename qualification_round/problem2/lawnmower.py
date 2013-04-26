#!/usr/bin/env python

import fileinput, itertools, multiprocessing, time

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Lawnmower:
    __debug = False

    def resolve(self):
        for row in xrange(0, self.__problemInfo[0]):
            for col in xrange(0, self.__problemInfo[1]):
                if self.__lawn[row][col] < self.__maxHeights['rowsHeight'][row] and self.__lawn[row][col] < self.__maxHeights['colsHeight'][col]:
                    return "NO"

        return "YES"

    def __init__(self, inProblem, inInfo, inLawn):
        self.__lawn = [map(int, row.split()) for row in inLawn]
        self.__problemInfo = inInfo

        self.__maxHeights = {
            'rowsHeight': [max(row) for row in self.__lawn],
            'colsHeight': []
        }

        for col in xrange(0, inInfo[1]):
            maxHeight = 0
            for row in xrange(0, inInfo[0]):
                if self.__lawn[row][col] > maxHeight:
                    maxHeight = self.__lawn[row][col]

            self.__maxHeights['colsHeight'].append(maxHeight)

        if self.__debug:
            print "Problem: %s" % (self.__problemInfo)
            print "Lawn: %s" % (self.__lawn)
            print "Maxs: %s" % (self.__maxHeights)

        print "Case #%s: %s" % (inProblem, self.resolve())

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]
    cpus = multiprocessing.cpu_count()

    line = 1
    for problem in xrange(1, int(lines[0]) + 1):
        problemInfo = map(int, lines[line].split())
        Lawnmower(problem, problemInfo, lines[line + 1:line + problemInfo[0] + 1])
        line += problemInfo[0] + 1

    """
        p = multiprocessing.Process(target = Lawnmower, args = (problem, problemInfo, lines[line + 1:line + problemInfo[0] + 1]))
        p.start()

        while len(multiprocessing.active_children()) >= cpus:
            time.sleep(0.1)
    """
