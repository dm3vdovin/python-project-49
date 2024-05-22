from random import randint

RULES = 'What number is missing in the progression?'


def get_progression():
    min_initial = 1
    max_initial = 30
    min_length = 5
    max_length = 10
    min_step = 1
    max_step = 10

    initial_number = randint(min_initial, max_initial)
    length = randint(min_length, max_length)
    step = randint(min_step, max_step)
    final_number = initial_number + (length * step)

    return list(range(initial_number, final_number, step))


def get_question_answer():
    mask = '..'

    progression = get_progression()
    masked_index = randint(0, len(progression) - 1)
    answer = progression[masked_index]
    progression[masked_index] = mask
    question = ' '.join(map(str, progression))

    return (question, str(answer))
