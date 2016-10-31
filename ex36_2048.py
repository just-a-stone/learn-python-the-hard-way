#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
                        continue
                return row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['LEFT'] = lambda chessboard: [move_row_left(row) for row in chessboard]
        moves['RIGHT'] = lambda chessboard: [invert(moves['LEFT'](invert(row))) for row in chessboard]
        moves['UP'] = lambda chessboard: [transpose(moves['LEFT'](transpose(row))) for row in chessboard]
        moves['DOWN'] = lambda chessboard: [transpose(moves['RIGHT'](transpose(row))) for row in chessboard]

        if action in moves:
            self.chessboard = moves[action](self.chessboard)
        else:
            print 'error action.'
