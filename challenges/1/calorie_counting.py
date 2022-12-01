def read_file_to_trimmed_array(filename):
    elves = []
    with open(filename) as file:
        elf = []
        for line in file:
            line = line.rstrip()
            if line == "":
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line))
    elves.append(elf)
    return elves


def find_most_calories(elves):
    highest_index = 0
    highest_calories = 0
    for i in range(1, len(elves) - 1):
        calories = sum_items(elves[i])
        if calories > highest_calories:
            highest_index = i
            highest_calories = calories
    return highest_index + 1, highest_calories


def sort_descending(elves):
    elves.sort(reverse=True, key=sum_items)
    return elves


def remove_at_index(list, index):
    left = list[0::index]
    right = list[index + 1::len(list) - 1]
    left.append(right)
    return left


def sum_items(list):
    total = 0
    for item in list:
        total += item
    return total


def get_top_total(elves, num):
    top = elves[0:num]
    total = 0
    for elf in top:
        total += sum_items(elf)
    return total


if __name__ == '__main__':
    filename = "input.txt"
    elves = read_file_to_trimmed_array(filename)
    elf_with_most_calories = find_most_calories(elves)
    print(f"Elf {elf_with_most_calories} has the most calories")

    sorted_elves = sort_descending(elves)
    top_total = get_top_total(sorted_elves, 3)
    print(f"Top 3 elves have {top_total} calories total")
