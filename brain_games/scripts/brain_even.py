import prompt
import random

MIN_VALUE = 1
MAX_VALUE = 100
TIP = 'is wrong answer ;(. Correct answer was'
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    answer_counter = 0

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(RULES)

    while (answer_counter != 3):

        random_number = random.randint(MIN_VALUE, MAX_VALUE)

        if (random_number % 2 == 0):
            answer = 'yes'
        else:
            answer = 'no'

        guess = prompt.string(f'Question: {random_number} ')

        print(f'Your answer: {guess}')

        # if (guess != answer or guess != YES or guess != NO):
        if (guess != answer):
            print(f'{guess} {TIP} {answer}')
            print(f'Let\'s try again, {name}!')
            return False
        else:
            print('Correct!')
            answer_counter += 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
