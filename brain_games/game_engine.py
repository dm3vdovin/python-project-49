import prompt


def run_game(game_name):
    rounds_count = 3

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_name.RULES)

    for _ in range(rounds_count):
        (question, answer) = game_name.get_question_answer()
        print(f'Question: {question}')
        rate = prompt.string('Your answer: ')

        if rate != answer:
            print(f"'{rate}' is wrong answer ;(. Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            break

        print('Correct!')

    else:
        print(f'Congratulations, {name}!')
