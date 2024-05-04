from random import randint

MIN_VALUE = 1
MAX_VALUE = 100

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False

    return True


def get_answers():
    question = randint(MIN_VALUE, MAX_VALUE)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'

    return (str(question), answer)
