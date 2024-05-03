import prompt

ROUNDS_COUNT = 3
TIP = 'is wrong answer ;(. Correct answer was'


def run_game(game_name):
    answer_counter = 0

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_name.RULES)

    while (answer_counter != ROUNDS_COUNT):

        (question, answer) = game_name.get_answers()

        print(f'Question: {question}')
        guess = prompt.string('Your answer: ')

        if (guess != answer):
            print(f'\'{guess}\' {TIP} \'{answer}\'')
            print(f'Let\'s try again, {name}!')
            return False
        else:
            print('Correct!')
            answer_counter += 1

    print(f'Congratulations, {name}!')
