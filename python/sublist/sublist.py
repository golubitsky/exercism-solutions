SUBLIST = 'sub'
SUPERLIST = 'super'
EQUAL = 'eq'
UNEQUAL = 'neq'


def is_sublist(this_list, other_list):
    indexes_to_check = len(other_list) - len(this_list) + 1

    for i in range(indexes_to_check):
        sub = other_list[i:len(this_list) + i]

        if this_list == sub:
            return True

    return False


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL

    if len(first_list) < len(second_list):
        if is_sublist(first_list, second_list):
            return SUBLIST

    if is_sublist(second_list, first_list):
        return SUPERLIST

    return UNEQUAL
