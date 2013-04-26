#!/usr/bin/env python

import fileinput, itertools, multiprocessing, time

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Problem:
    __debug = False

    def resolve(self):
        return ''

    def __init__(self, ....):

        if self.__debug:
            print "Screen: %s" % (self.__screen)

        print "Case #%s: %s" % (inLinePos, self.resolve())

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]
    cpus = multiprocessing.cpu_count()

    for linePos in xrange(1, int(lines[0]) + 1):
        info = map(int, lines[linePos].split())
        p = multiprocessing.Process(target = Problem, args = (....))
        p.start()

        while len(multiprocessing.active_children()) >= cpus:
            time.sleep(0.1)
