# opening the file in read mode
def read_to_list(file):
    input_data = open(file, "r").read()
    input_data_list = input_data.split("\n")

    i = 0
    output_lists_list = []
    output_list = []
    while i < len(input_data_list):
        el = input_data_list[i]
        if el != '':
            output_list.append(el)
            if i == len(input_data_list)-1:
                output_lists_list.append(output_list)
                output_list = []
        else:
            output_lists_list.append(output_list)
            output_list = []
        i = i+1
    structured_input = output_lists_list
    return structured_input


def sum_values_in_list(file):
    structured_input = read_to_list(file)
    total_calories_by_elf = []
    for el in structured_input:
        i = 0
        total_calories = 0
        while i < len(el):
            total_calories = total_calories + int(el[i])
            i = i+1
        total_calories_by_elf.append(total_calories)
    return total_calories_by_elf


def get_most_caloric_elf(file):
    total_calories_by_elf = sum_values_in_list(file)
    max_calories = max(total_calories_by_elf)
    most_caloric_elf = total_calories_by_elf.index(max_calories)+1
    return most_caloric_elf, max_calories

def get_top_three_calories(file):
    total_calories_by_elf = sum_values_in_list(file)
    total_calories_by_elf.sort()
    top_three_calories = 0
    i = 0
    while i in range(0, 3):
        top_three_calories += total_calories_by_elf[i]
        i = i+1
    return top_three_calories


if __name__ == '__main__':
    file = "input.txt"
    #part 1
    print("PART 1\n")
    most_caloric_elf, max_calories = get_most_caloric_elf(file)
    print(f"Most caloric elf is elf number {most_caloric_elf}, with a total of {max_calories}.")
    print("Bon appetit!\n")
    #part 2
    print("PART 2\n")
    top_three_calories = get_top_three_calories(file)
    print(f"Three most caloric elfs carry a total of {top_three_calories} calories <3")

