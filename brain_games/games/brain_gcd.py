from random import randint
from math import gcd

MIN_VALUE = 1
MAX_VALUE = 100

RULES = 'Find the greatest common divisor of given numbers'


def get_answers():
    random_number1 = randint(MIN_VALUE, MAX_VALUE)
    random_number2 = randint(MIN_VALUE, MAX_VALUE)

    question = f'{random_number1} {random_number2}'
    answer = gcd(random_number1, random_number2)

    return (question, str(answer))
