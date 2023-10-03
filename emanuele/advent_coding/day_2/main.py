'''
first column (oponent): A for Rock, B for Paper, and C for Scissors
second column (me): X for Rock, Y for Paper, and Z for Scissors

total score = the sum of your scores for each round
score for a single round = sum of:
- the score for the shape you selected: 1 for Rock, 2 for Paper, and 3 for Scissors
- the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won
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
    shape_score = 0
    match_score = 0
    moves_set, own_moves_list = read_to_list(file)
    '''for el in own_moves_list:
        shape_score = shape_score + shape_score_dict[el]'''
    print(moves_set)
    moves_set = [('B', 'Z'), ('A', 'X'), ('B', 'Z'), ('A', 'A')]
    print(moves_set)
    for el in moves_set:
        print(f"el is {el}")
        print(el[0])
        print(el[1])
        if el in win_options:
            match_score = match_score + 6
        elif el[0] == el[1]:
            print(f"el is {el}")
            match_score = match_score + 3
    total_score = shape_score + match_score
    return total_score


if __name__ == '__main__':
    file = "input.txt"
    read_to_list(file)
    total_score = final_result(file)
    #part 1
    print("PART 1\n")
    print(f"Total score would be {total_score}")

    ''''#part 2
    print("PART 2\n")

    print(f"")'''

