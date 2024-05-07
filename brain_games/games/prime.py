from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False

    return True


def get_question_answer():
    min_value = 1
    max_value = 100

    question = randint(min_value, max_value)

    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'

    return (str(question), answer)
