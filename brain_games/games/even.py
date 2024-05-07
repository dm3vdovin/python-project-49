from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    min_value = 1
    max_value = 100

    random_number = randint(min_value, max_value)

    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return (str(random_number), answer)
