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
    print(structured_input)
    return structured_input


def sum_values_in_list(file):
    structured_input = read_to_list(file)
    total_calories_by_elf = []
    for el in structured_input:
        i = 0
        total_calories = 0
        while i < len(el):
            total_calories = total_calories + int(el[i])
            print(i)
            print(total_calories)
            i = i+1
        total_calories_by_elf.append(total_calories)
        print(total_calories_by_elf)


if __name__ == '__main__':
    sum_values_in_list(file="input.txt")
