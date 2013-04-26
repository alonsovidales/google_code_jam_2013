#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Problem:
    __debug = False

    def resolve(self):
        return ''

    def __init__(self, ...):
        if self.__debug:
            print "Position: %s" % (self.__groups) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    print "%s" % (Problem(...).resolve())
