#!/usr/bin/env python

import fileinput, itertools, multiprocessing, time

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-04-12"

class TickTack:
    __debug = False

    def __checkComplete(self):
        for row in self.__board:
            for col in row:
                if col == '.':
                    return False

        return True

    def __checkDiag(self):
        first = self.__board[0][0]
        if first == 'T':
            first = self.__board[1][1]

        if first != '.':
            possible = True
            for pos in xrange(0, 4):
                if self.__board[pos][pos] != first and self.__board[pos][pos] != 'T':
                    possible = False
                    break

            if possible:
                return first

        first = self.__board[0][3]
        if first == 'T':
            first = self.__board[1][3]

        if first != '.':
            possible = True
            for pos in xrange(1, 4):
                if self.__board[pos][3 - pos] != first and self.__board[pos][3 - pos] != 'T':
                    possible = False
                    break

            if possible:
                return first

        return False

    def __checkVert(self):
        for colPos in xrange(0, 4):
            first = self.__board[0][colPos]

            if first == 'T':
                first = self.__board[1][colPos]

            if first == '.':
                possible = False
                continue

            possible = True
            for rowPos in xrange(1, 4):
                if self.__board[rowPos][colPos] != first and self.__board[rowPos][colPos] != 'T':
                    possible = False
                    break

            if possible:
                return first

        return False

    def __checkHoriz(self):
        for row in self.__board:
            first = row[0]
            if first == 'T':
                first = row[1]

            if first == '.':
                possible = False
                continue

            possible = True
            for colPos in xrange(1, 4):
                if row[colPos] != first and row[colPos] != 'T':
                    possible = False
                    break

            if possible:
                return first
        return False

    def resolve(self):
        winner = self.__checkHoriz()
        if winner == False:
            winner = self.__checkVert()
            if winner == False:
                winner = self.__checkDiag()

        if winner == False:
            if self.__checkComplete():
                return "Draw"
            else:
                return "Game has not completed"

        if winner == 'X':
            return "X won"

        return "O won"

    def __init__(self, inGame, inLines):
        self.__board = [list(line) for line in inLines]

        if self.__debug:
            print "Board: %s" % (self.__board)

        print "Case #%s: %s" % (inGame, self.resolve())

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]
    cpus = multiprocessing.cpu_count()

    for game in xrange(0, int(lines[0])):
        TickTack(game + 1, [
            lines[game * 5 + 1],
            lines[game * 5 + 2],
            lines[game * 5 + 3],
            lines[game * 5 + 4],
        ])
