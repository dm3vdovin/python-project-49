from random import randint

MIN_VALUE = 1
MAX_VALUE = 100

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answers():
    random_number = randint(MIN_VALUE, MAX_VALUE)

    if (random_number % 2 == 0):
        answer = 'yes'
    else:
        answer = 'no'

    return (str(random_number), answer)
