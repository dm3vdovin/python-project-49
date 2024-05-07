from random import randint, choice

RULES = 'What is the result of the expression?'


def get_question_answer():
    min_value = 2
    max_value = 10

    random_number1 = randint(min_value, max_value)
    random_number2 = randint(min_value, max_value)
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
