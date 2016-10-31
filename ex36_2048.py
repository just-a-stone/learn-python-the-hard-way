#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def transpose(chessboard):
        return [row for list(i) for i in zip(*cheeses)]

    def invert(chessboard):
        return [row[::-1] for row in chessboard]

    def move(self, action):
        pass
