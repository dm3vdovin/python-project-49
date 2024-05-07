from random import randint

RULES = 'What number is missing in the progression?'


def get_progression():
    min_initial_value = 1
    max_initial_value = 30
    min_length_value = 5
    max_length_value = 10
    min_step_value = 1
    max_step_value = 10

    initial_number = randint(min_initial_value, max_initial_value)
    length = randint(min_length_value, max_length_value)
    step = randint(min_step_value, max_step_value)
    progression = []
    final_number = initial_number + (length * step)

    for number in range(initial_number, final_number, step):
        progression.append(str(number))

    return progression


def get_question_answer():
    mask = '..'

    progression = get_progression()
    masked_index = randint(0, len(progression) - 1)
    masked_number = progression[masked_index]
    progression[masked_index] = mask
    progression = ' '.join(progression)
    question = f'{progression}'

    return (question, masked_number)
