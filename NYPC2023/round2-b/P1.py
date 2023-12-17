def get_near_bracket(bracket, i):
    currency = i
    if currency >= len(bracket):
        return len(bracket) - 1
    while bracket[currency] == '0' and currency < len(bracket) - 1:
        currency += 1
    return currency


def is_empty(bracket):
    for i in range(len(bracket) - 1):
        if bracket[i] == '(' and bracket[get_near_bracket(bracket, i + 1)] == ')':
            return True
    return False


def get_bracket_count(bracket):
    result = 0
    modified_bracket = list(bracket)
    while is_empty(modified_bracket):
        for i in range(len(modified_bracket) - 1):
            if modified_bracket[i] == '(' and modified_bracket[get_near_bracket(modified_bracket, i + 1)] == ')':
                result += 1
                modified_bracket[i] = '0'
                modified_bracket[get_near_bracket(modified_bracket, i + 1)] = '0'
    result += modified_bracket.count('(') * 2
    return result

n = int(input())
bracket = input()
print(get_bracket_count(bracket))
