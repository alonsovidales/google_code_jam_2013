#!/usr/bin/env python

import fileinput, itertools, multiprocessing, time, copy

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Treasure:
    __debug = True

    def resolve(self):
        return "IMPOSSIBLE"

    def __init__(self, info, keys, chests):
        self.__chestsGraph = [None] * info[1]

        chestByKey = {}
        for chestPos in xrange(0, info[1]):
            if chests[chestPos][0] in chestByKey:
                chestByKey[chests[chestPos][0]].append(chestPos)
            else:
                chestByKey[chests[chestPos][0]] = [chestPos]

        for chestPos in xrange(0, info[1]):
            print "ChestPos: %s" % (chestPos)
            for keyInChest in chests[chestPos][2:]:
                if keyInChest in chestByKey:
                    print chestByKey[keyInChest]
                    chestsToOpen = chestByKey[keyInChest][:]
                    try:
                        chestsToOpen.remove(chestPos)
                    except:
                        pass
                    if self.__chestsGraph[chestPos] == None:
                        self.__chestsGraph[chestPos] = chestsToOpen
                    else:
                        self.__chestsGraph[chestPos] += chestsToOpen

        self.__possibleChests = []
        for key in keys:
            if key in chestByKey:
                self.__possibleChests

        if self.__debug:
            print "Info: %s" % (info)
            print "Chests keys: %s" % (chestByKey)
            print "Keys: %s" % (keys)
            print "Chests: %s" % (chests)
            print "Chests graph: %s" % (self.__chestsGraph)
            print "--"

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    linePos = 1
    for case in xrange(1, int(lines[0]) + 1):
        info = map(int, lines[linePos].split())
        keys = map(int, lines[linePos + 1].split())
        chests = [map(int, lines[linePos + 2 + chest].split()) for chest in xrange(0, info[1])]
        print "Case #%s: %s" % (case, Treasure(info, keys, chests).resolve())
        linePos = linePos + info[1] + 2
