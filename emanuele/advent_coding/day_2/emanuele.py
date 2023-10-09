#!/usr/bin/python3

"""
A = rock
B = paper
C = scissor
"""

def translate_part1(strategy):
    strat_dict = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    return strat_dict[strategy]


def translate_part2(p1, strategy):
    win_options = {'A': 'B', 'B': 'C', 'C': 'A'}
    lose_options = {'A': 'C', 'B': 'A', 'C': 'B'}
    if strategy == 'X': # lose
        return lose_options[p1]
    elif strategy == 'Z': # win
        return win_options[p1]
    else: # draw
        return p1


def round_score(p1, p2):
    shape_score_dict = {'A': 1, 'B': 2, 'C': 3}
    game_score_dict = {
        'A': {
            'A': 3,
            'B': 6,
            'C': 0,
        },
        'B': {
            'A': 0,
            'B': 3,
            'C': 6,
        },
        'C': {
            'A': 6,
            'B': 0,
            'C': 3,
        },
    }
    return shape_score_dict[p2] + game_score_dict[p1][p2]


def solve(file="input.txt", part1=True):
    total_score = 0
    with open(file, 'r') as f:
        for line in f:
            p1, strat = line.rstrip().split(' ')
            p2 = translate_part1(strat) if part1 is True else translate_part2(p1, strat)
            total_score += round_score(p1, p2)
    return total_score


if __name__ == '__main__':
    path = "input.txt"
    print(f"Total score for part 1 would be {solve(path, True)}")
    print(f"Total score for part 2 would be {solve(path, False)}")
