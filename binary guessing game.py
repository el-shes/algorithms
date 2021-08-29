
LEFT = 0
RIGHT = 127


def guess(left_field, right_field):
    potential = (right_field - left_field) // 2 + left_field
    print('Is this your number: {}?'.format(potential))
    return potential


def guess_number(possible_number, number, left_border, right_border):
    if possible_number == number:
        return [possible_number, possible_number]
    elif possible_number > number:
        right_border = possible_number - 1
        return [left_border, right_border]
    elif possible_number < number:
        left_border = possible_number + 1
        return [left_border, right_border]


if __name__ == '__main__':
    print("Choose a number in range {} to {}".format(LEFT, RIGHT))
    n = int(input())
    new_left, new_right = LEFT, RIGHT
    while new_left != new_right:
        new_left, new_right = guess_number(guess(new_left, new_right), n, new_left, new_right)
    print("YAY! Found your number. I guess it is {}".format(new_left))