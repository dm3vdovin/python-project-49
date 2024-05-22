import operator
from random import randint, choice

RULES = 'What is the result of the expression?'


def get_question_answer():
    min_value = 2
    max_value = 10

    random_number1 = randint(min_value, max_value)
    random_number2 = randint(min_value, max_value)

    addition = ('+', operator.add(random_number1, random_number2))
    subtraction = ('-', operator.sub(random_number1, random_number2))
    multiplication = ('*', operator.mul(random_number1, random_number2))

    operations = [addition, subtraction, multiplication]
    operation = choice(operations)
    (operand, answer) = operation
    question = f'{random_number1} {operand} {random_number2}'

    return (question, str(answer))
