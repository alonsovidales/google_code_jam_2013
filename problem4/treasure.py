#!/usr/bin/env python

import fileinput, itertools, multiprocessing, time, copy

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class Treasure:
    __debug = False

    def __checkByDep(self, inKeys, inChests, inCurrentChests = []):
        if self.__debug:
            print "Keys: %s" % (inKeys)
            print "Chets %s" % (inChests)
            print "Curent Chets: %s" % (inCurrentChests)
            print "--"
        if len(inChests.keys()) == 0:
            return inCurrentChests

        for keyPos in xrange(0, len(inKeys)):
            if inKeys[keyPos] in inChests:
                for chestPos in xrange(0, len(inChests[inKeys[keyPos]])):
                    keys = inKeys + inChests[inKeys[keyPos]][chestPos][1]
                    keys.pop(keyPos)
                    newChests = copy.deepcopy(inChests)
                    newChests[inKeys[keyPos]].pop(chestPos)
                    if len(newChests[inKeys[keyPos]]) == 0:
                        del newChests[inKeys[keyPos]]
                    newCurrentChests = inCurrentChests[:]
                    newCurrentChests.append(inChests[inKeys[keyPos]][chestPos][0])
                    combination = self.__checkByDep(keys, newChests, newCurrentChests)
                    if combination != False:
                        return combination

        return False

    def __checkIfPossible(self):
        for key, necessary in self.__totalNecessaryKeys.items():
            if necessary > self.__possibleKeys[key]:
                return False

        return True

    def __checkPermutation(self, keys, chests):
        if self.__debug:
            print "Perm"
            print keys
            print chests
        for chest in chests:
            if self.__chests[chest]['key'] not in keys:
                return False

            for keysInChest in self.__chests[chest]['keys']:
                if keysInChest in keys:
                    keys[keysInChest] += 1
                else:
                    keys[keysInChest] = 1

        return True

    def resolve(self):
        if not self.__checkIfPossible():
            return "IMPOSSIBLE"

        initialKeys = {}
        for key in self.__keys:
            if key in initialKeys:
                initialKeys[key] += 1
            else:
                initialKeys[key] = 1
        
        for permutation in itertools.permutations(self.__chestsByKeys.keys(), len(self.__chestsByKeys.keys())):
            if self.__checkPermutation(copy.deepcopy(initialKeys), permutation):
                return ' '.join(map(str, permutation))

        exit()

        keys = self.__checkByDep(self.__keys, self.__chestsByKeys)

        if keys == False:
            return "IMPOSSIBLE"

        return ' '.join(map(str, keys))

    def __init__(self, keys, chests):
        self.__keys = keys
        self.__chestsByKeys = {}
        self.__totalNecessaryKeys = {}
        self.__possibleKeys = {}
        self.__chests = []

        for key in keys:
            if key in self.__possibleKeys:
                self.__possibleKeys[key] += 1
            else:
                self.__possibleKeys[key] = 1
        
        for chestPos in xrange(0, len(chests)):
            self.__chests.append({
                'key': chests[chestPos][0],
                'keys': chests[chestPos][2:2 + chests[chestPos][1]]
            })

            keysInChest = chests[chestPos][2:2 + chests[chestPos][1]]
            for key in keysInChest:
                if key in self.__possibleKeys:
                    self.__possibleKeys[key] += 1
                else:
                    self.__possibleKeys[key] = 1
                
            if chests[chestPos][0] in self.__chestsByKeys:
                self.__chestsByKeys[chests[chestPos][0]].append((chestPos + 1, keysInChest))
                self.__totalNecessaryKeys[chests[chestPos][0]] += 1
            else:
                self.__chestsByKeys[chests[chestPos][0]] = [(chestPos + 1, chests[chestPos][2:2 + chests[chestPos][1]])]
                self.__totalNecessaryKeys[chests[chestPos][0]] = 1

        if self.__debug:
            print "Keys: %s" % (self.__keys)
            print "Chests: %s" % (self.__chests)
            print "Chests By Key: %s" % (self.__chestsByKeys)
            print "Necessary keys: %s" % (self.__totalNecessaryKeys)
            print "Keys in chests: %s" % (self.__possibleKeys)
            print "--"

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    linePos = 1
    for case in xrange(1, int(lines[0]) + 1):
        info = map(int, lines[linePos].split())
        keys = map(int, lines[linePos + 1].split())
        chests = [map(int, lines[linePos + 2 + chest].split()) for chest in xrange(0, info[1])]
        print "Case #%s: %s" % (case, Treasure(keys, chests).resolve())
        linePos = linePos + info[1] + 2
