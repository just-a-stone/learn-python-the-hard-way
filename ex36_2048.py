#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import curses
from random import randrange, choice

class Game2048(object):
    """docstring for Game2048."""
    def __init__(self, width=4, height=4, win=2048):
        super(Game2048, self).__init__()
        self.width = width
        self.height = height
        self.win_value = win
        self.reset()

    def reset(self):
        self.chessboard = [[0 for i in range(self.width)] for j in range(self.height)]
        self.max_score = 0
        self.add_new()

    def add_new(self):
        new_chessman = 2 if randrange(100) < 89 else 4
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.chessboard[i][j] == 0])
        self.chessboard[i][j] = new_chessman

    def transpose(chessboard):
        return [list(i) for i in zip(*chessboard)]

    def invert(chessboard):
        return [row[::-1] for row in chessboard]

    def move(self, action):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i > 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                for index, value in enumerate(row):
                    if index + 1 < len(row) and value == row[index + 1]:
                        row[index] = value * 2
                        row[index + 1] = 0
                        if row[index] > self.max_score:
                            self.max_score = row[index]
                        continue
                return row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['LEFT'] = lambda chessboard: [move_row_left(row) for row in chessboard]
        moves['RIGHT'] = lambda chessboard: [invert(moves['LEFT'](invert(row))) for row in chessboard]
        moves['UP'] = lambda chessboard: [transpose(moves['LEFT'](transpose(row))) for row in chessboard]
        moves['DOWN'] = lambda chessboard: [transpose(moves['RIGHT'](transpose(row))) for row in chessboard]

        action = action.upper()
        if action in moves:
            self.chessboard = moves[action](self.chessboard)
        else:
            print 'error action.'

    def is_win(self):
        return self.max_score >= self.win_value

    def is_gameover(self):
        def moveable():
            return any((i == 0 for i in row) for row in self.chessboard)

        def mergeable():
            for row in self.chessboard:
                for index, value in enumerate(row):
                    if value == row[index + 1]:
                        return True

            for row in transpose(self.chessboard):
                for index, value in enumerate(row):
                    if value == row[index + 1]:
                        return True

            return False

        return not (moveable()) or not (mergeable())


    def draw(self):
        def show(string):
            print string
            # screen.addstr(string + '\n')

        def start():
            tips = "please input the key follows!"
            operation = "[w]:up [a]:left [s]:down [d]:right"
            helps = "[q]:exit [r]:restart"
            begin = "now, let's begin!"

            show(tips)
            show(operation)
            show(helps)
            show(begin)

        def show_chessboard():
            line = '+------' * self.width + '+'
            for row in self.chessboard:
                rowout = ''
                for x in row:
                    rowout += str(x).center(6)
                show(rowout)

        show_chessboard()
