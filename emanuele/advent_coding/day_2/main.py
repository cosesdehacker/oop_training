'''
the second column says how the round needs to end:
- X means you need to lose
- Y means you need to end the round in a draw
- Z means you need to win
'''


def read_to_list(file):
    input_data = open(file, "r").read()
    input_data_list = input_data.split("\n")
    opponent_moves_list = []
    own_moves_list = []
    i = 0
    while i < len(input_data_list)-1:
        el = input_data_list[i]
        opponent_moves_list.append(el[0])
        own_moves_list.append(el[2])
        i = i+1
    moves_set = list(zip(opponent_moves_list, own_moves_list))
    return moves_set, own_moves_list


def final_result(file):
    shape_score_dict = {'X': 1, 'Y': 2, 'Z': 3}
    win_options = {('C', 'X'), ('A', 'Y'), ('B', 'Z')}
    draw_options = {('A', 'X'), ('B', 'Y'), ('C', 'Z')}
    shape_score = 0
    match_score = 0
    moves_set, own_moves_list = read_to_list(file)
    for el in own_moves_list:
        shape_score = shape_score + shape_score_dict[el]
    for el in moves_set:
        if el in win_options:
            match_score = match_score + 6
        elif el in draw_options:
            match_score = match_score + 3
    total_score = shape_score + match_score
    print(dict(moves_set))
    return total_score

def get_startegic_moves(file):
    #strategy_dict = {'X': "lose", 'Y': "draw", 'Z': "win"}
    win_options = {'C': 'A', 'A': 'B', 'B': 'C'}
    lose_options = {'A': 'B', 'B': 'C', 'C': 'A'}
    moves_set, own_moves_list = read_to_list(file)
    print(moves_set)
    for el in moves_set:
        print(f"here el is {el}")
        opponent_move = el[0]
        print(f"here opponent_move is {opponent_move}")
        print(f"here el[1] is {el[1]}")
        if el[1] == 'X':
            print("first if")
            #el[1] = lose_options[opponent_move]
        elif el[1] == 'Z':
            print("second if")
            #el[1] = win_options[opponent_move]
        else:
            print("third if")
            #el[1] = el[0]
    return moves_set


if __name__ == '__main__':
    file = "input.txt"
    read_to_list(file)
    total_score = final_result(file)

    #part 1
    print("PART 1\n")
    print(f"Total score would be {total_score}")

    #part 2
    print("PART 2\n")
    get_startegic_moves(file)

