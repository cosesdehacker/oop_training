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
    print("This is the real input data:")
    print(input_data_list)
    opponent_moves_list = []
    own_moves_list = []
    for el in input_data_list:
        el.replace(' ', '')
        #print("el1")
        #print(el[1])
        opponent_moves_list.append(el[0])
        own_moves_list.append(el[2])
        moves_dict = dict(zip(opponent_moves_list, own_moves_list))
    print(moves_dict)
    return moves_dict

def test_read_to_list(file):
    print("This is my fake input data, which looks the fucking same:")
    input_data_list = ['B Z', 'A X', 'B Z']
    opponent_moves_list = []
    own_moves_list = []
    for el in input_data_list:
        el.replace(' ', '')
        #print("el1")
        #print(el[1])
        opponent_moves_list.append(el[0])
        own_moves_list.append(el[2])
        moves_dict = dict(zip(opponent_moves_list, own_moves_list))
    print(moves_dict)
    return moves_dict

def single_round_result(file):
    moves_dict = read_to_list(file)
    shape_score_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    standard_shapes = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    win_options = {'C': 'A', 'A': 'B', 'B': 'C'}
    #0 if you lost, 3 if the round was a draw, and 6 if you won


if __name__ == '__main__':
    file = "input.txt"
    #read_to_list(file)
    test_read_to_list(file)
    #single_round_result(file)
    #part 1
    print("PART 1\n")

    print(f"Total score would be ")

    #part 2
    print("PART 2\n")

    print(f"")

