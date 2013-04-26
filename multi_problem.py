#!/usr/bin/env python

import fileinput, itertools, multiprocessing, time, os

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Problem:
    __debug = False

    def resolve(self):
        return 'solution'

    def __init__(self, mainProcessPid, inLinePos, inParams):

        #if self.__debug:
        #    print "Screen: %s" % (self.__screen)

        f = open("/tmp/out_%s_%s" % (mainProcessPid, inLinePos), 'w')
        f.write("Case #%s: %s\n" % (inLinePos, self.resolve()))
        f.close()

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]
    cpus = multiprocessing.cpu_count()

    for linePos in xrange(1, int(lines[0]) + 1):
        #info = map(int, lines[linePos].split())
        p = multiprocessing.Process(target = Problem, args = (os.getpid(), linePos, "EIN???", ))
        p.start()

        while len(multiprocessing.active_children()) >= cpus:
            time.sleep(0.1)

    # Wait until all the process has finished
    while len(multiprocessing.active_children()) > 0:
        time.sleep(0.1)

    os.system("cat /tmp/out_%s_*" % (os.getpid()))
