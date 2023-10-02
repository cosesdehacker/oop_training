# opening the file in read mode
def read_to_list(file):
    input_data = open(file, "r").read()
    input_data_list = input_data.split("\n")

    input_data_list = ["2","2","","0","98","","3"]

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
    print("structured_input:")
    print(structured_input)
    return structured_input


def sum_values_in_list(file):
    structured_input = read_to_list(file)
    total_calories_by_elf = []
    print(structured_input)
    for el in structured_input:
        print("el:")
        print(el)
        i = 0
        total_calories = 0
        while i < len(el):
            print("total_calories1:")
            print(total_calories)
            total_calories = total_calories + int(el[i])
            print("iterator:")
            print(i)
            print("total_calories2:")
            print(total_calories)
            i = i+1
        total_calories_by_elf.append(total_calories)
    print("total calories by elf:")
    print(total_calories_by_elf)
    return total_calories_by_elf


def get_most_caloric_elf(file):
    total_calories_by_elf = sum_values_in_list(file)
    max_calories = max(total_calories_by_elf)
    print("max_calories:")
    print(max_calories)
    most_caloric_elf = total_calories_by_elf.index(max_calories)+1
    print("most_caloric_elf, max_calories")
    print(most_caloric_elf, max_calories)
    return most_caloric_elf, max_calories


if __name__ == '__main__':
    most_caloric_elf, max_calories = get_most_caloric_elf(file="input.txt")
    print(f"Most caloric elf is elf number {most_caloric_elf}, with a total of {max_calories}.\n")
    print("Bon appetit!")

