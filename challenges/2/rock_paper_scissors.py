def read_file_to_array(filename):    games = []    with open(filename) as file:        for line in file:            games.append(line.rstrip().split(" "))    return gameselfMapping = {'A': 'R', 'B': 'P', 'C': 'S'}myMapping = {'X': 'R', 'Y': 'P', 'Z': 'S'}winningMap = {    'R': 'S',    'P': 'R',    'S': 'P'}losingMap = {    'S': 'R',    'R': 'P',    'P': 'S'}choiceScore = {'R': 1, 'P': 2, 'S': 3}def convert_round(round):    return elfMapping[round[0]], myMapping[round[1]]def get_my_score_for_round(round):    round = convert_round(round)    elf = round[0]    me = round[1]    hand_score = choiceScore[me]    if elf == me:        return 3 + hand_score    required_to_win = winningMap[me]    if elf == required_to_win:        return 6 + hand_score    return 0 + hand_scoredef get_my_score_for_rounds(rounds):    total = 0    for round in rounds:        total += get_my_score_for_round(round)    return totaldef get_my_score_for_rounds_full_strat(rounds):    total = 0    for round in rounds:        total += get_my_score_for_round_full_strat(round)    return totaldef get_my_score_for_round_full_strat(round):    elf_shape = elfMapping[round[0]]    strat = round[1]    # Win    if strat == 'Z':        my_shape = losingMap[elf_shape]        return choiceScore[my_shape] + 6    # Lose    if strat == 'X':        my_shape = winningMap[elf_shape]        return choiceScore[my_shape] + 0    # Draw    if strat == 'Y':        return choiceScore[elf_shape] + 3if __name__ == '__main__':    rounds = read_file_to_array("input.txt")    my_score = get_my_score_for_rounds(rounds)    print(f"My score was {my_score}")    my_score_strat = get_my_score_for_rounds_full_strat(rounds)    print(f"My score with full strat was {my_score_strat}")