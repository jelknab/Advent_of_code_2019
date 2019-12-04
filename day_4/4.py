import re


repeating_matcher = re.compile(r'(\d)\1*')


def contains_repeating_digit(input: str) -> bool:
    for match in repeating_matcher.finditer(input):
        if len(match.group()) == 2:
            return True

    return False


def digits_not_decreasing(input: str) -> bool:
    for index in range(1, len(input)):
        if int(input[index]) < int(input[index - 1]):
            return False

    return True


conditions = [contains_repeating_digit, digits_not_decreasing]


def password_conditions_met(password: str):
    for condition in conditions:
        if not condition(password):
            return False

    return True


if __name__ == '__main__':
    qualifying_passwords = []

    for password_number in range(136760, 595730):
        password = str(password_number)

        if password_conditions_met(password):
            qualifying_passwords.append(password)

    print(len(qualifying_passwords))
