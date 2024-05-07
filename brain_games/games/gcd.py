from random import randint
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    min_value = 1
    max_value = 100

    random_number1 = randint(min_value, max_value)
    random_number2 = randint(min_value, max_value)
    question = f'{random_number1} {random_number2}'
    answer = gcd(random_number1, random_number2)

    return (question, str(answer))
