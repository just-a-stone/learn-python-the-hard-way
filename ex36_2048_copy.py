#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange, choice
from collections import defaultdict
import exit

# 定义动作
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'RESTART', 'EXIT']
keybord_codes = [ord[letter] for letter in 'wsadrqWSADRQ']
action_dict = dict(zip(keybord_codes, actions * 2))

# 定义循环，等待用户动作


# 定义动作对应实现，接收动作指令
class GameActions(object):
    """docstring for GameActions."""
    def __init__(self, height=4, wedth=4, win=2048):
        super(GameActions, self).__init__()
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.topScore = 0
        self.reset()

    def reset(self):
        if self.score > self.topScore:
            self.topScore = self.score
        self.score = 0
        self.dields = [[0 for i in range(self.width) for j in range(self.height)]]
        self.spawn()
        self.spawn()

    def exit(self):
        exit(0)
        pass

    # 行列转换
    def transpose(fields):
        return [list[row] for row in zip(*fields)]
    # 行反转
    def invert(fields):
        return [row[::-1] for row in fields]

    def move(self, direction):

        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                for index,value in enumerate(row):
                    if index + 1 < len(row) && value == row[index + 1]:
                        row[index] = value * 2
                        row[index + 1] = 0
            return row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['LEFT'] = lambda fields: [move_row_left[row] for row in fields]
        moves['RIGHT'] = lambda fields: invert(moves['LEFT'](invert(fields))
        moves['UP'] = lambda fields: transpose(moves['LEFT'](transpose(fields)))
        moves['DOWN'] = lambda fields: transpose[moves['RIGHT'](transpose(fields))]

        if direction in moves:
            self.fields = moves[direction](self.fields)
            self.spawn()
            return True
        else:
            return False

    def is_win(self):
        return any(any(i > self.win_value for i in row) for row in self.fields)

    def is_gameover(self):
        def row_mergeable(row):
            for index, value in enumerate(row):
                if index + 1 < len(row) and value == row[index + 1]:
                    return False
            return True

        flag = False
        for row in self.fields:
            flag = row_mergeable(row)
        if flag:
            for row in transpose(self.fields):
                flag = row_mergeable(row)

        return flag

    def spawn():
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.dields[i][j] == 0])
        self.dields[i][j] = mew_element
        pass


    # 处理用户输入，转义为对应指令
    def get_uer_command():
        while True:
            command = raw_input("> ")
            if command not in action_dict:
                print "wrong command. please input again."
                continue
            else:
                return action_dict[command]

# 指令实现


# 展示棋盘
