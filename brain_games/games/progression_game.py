from random import randint

MIN_INITIAL_VALUE = 1
MAX_INITIAL_VALUE = 30

MIN_LENGTH_VALUE = 5
MAX_LENGTH_VALUE = 10

MIN_STEP_VALUE = 1
MAX_STEP_VALUE = 10

MASK = '..'

RULES = 'What number is missing in the progression?'


def get_progression():
    initial_number = randint(MIN_INITIAL_VALUE, MAX_INITIAL_VALUE)
    length = randint(MIN_LENGTH_VALUE, MAX_LENGTH_VALUE)
    step = randint(MIN_STEP_VALUE, MAX_STEP_VALUE)

    progression = []
    final_number = initial_number + (length * step)

    for number in range(initial_number, final_number, step):
        progression.append(str(number))

    return progression


def get_answers():
    progression = get_progression()
    masked_index = randint(0, len(progression) - 1)
    masked_number = progression[masked_index]
    progression[masked_index] = MASK
    progression = ' '.join(progression)

    question = f'{progression}'

    return (question, masked_number)
