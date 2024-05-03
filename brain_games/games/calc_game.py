from random import randint, choice

MIN_VALUE = 2
MAX_VALUE = 10

RULES = 'What is the result of the expression?'


def get_answers():
    random_number1 = randint(MIN_VALUE, MAX_VALUE)
    random_number2 = randint(MIN_VALUE, MAX_VALUE)

    operation = choice(['+', '-', '*'])

    match operation:
        case '+':
            answer = random_number1 + random_number2
        case '-':
            answer = random_number1 - random_number2
        case '*':
            answer = random_number1 * random_number2

    question = f'{random_number1} {operation} {random_number2}'

    return (question, str(answer))
