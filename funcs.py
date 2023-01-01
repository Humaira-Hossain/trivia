import requests
import random


def number_of_questions():
    while True:
        try:
            num = input('How many questions would you like to answer? ')
            if num.lower().strip() in ['q', 'quit']:
                print('Goodbye!')
                exit()
            elif num == '0':
                print('Sorry, please enter a number greater than zero or Q to exit.')
                continue
            else:
                num = int(num)
        except ValueError:
            print('Sorry, please enter a whole number or Q to exit.')
        else:
            break

    return num


def difficulty():
    levels = {
        '1': 'easy',
        '2': 'medium',
        '3': 'hard',
        'easy': 'easy',
        'medium': 'medium',
        'hard': 'hard'
    }

    while True:
        try:
            choice = input('Please choose a difficulty level:'
                           '\n[1] Easy'
                           '\n[2] Medium'
                           '\n[3] Hard'
                           '\n[4] Quit'
                           '\n')
            if choice.strip().lower() in ['4', 'quit']:
                print('Goodbye!')
                exit()
            elif choice.strip().lower() in ['1', '2', '3', 'easy', 'medium', 'hard']:
                return levels[choice]
            else:
                raise ValueError
        except ValueError:
            print('Sorry, please enter 1, 2, or 3. Alternatively, type the word easy, medium, or hard')


def get_endpoint(number, difficulty):
    num = str(number)
    endpoint = f'https://the-trivia-api.com/api/questions?limit={num}&difficulty={difficulty}'

    return endpoint


def get_json(endpoint):
    response = requests.get(endpoint)

    info = response.json()

    return info


def get_questions(info):
    questions = []
    for i in range(len(info)):
        questions.append(info[i]['question'])

    return questions


def get_correct_answers(info):
    correct = []
    for i in range(len(info)):
        correct.append(info[i]['correctAnswer'])

    return correct


def get_options(info, correct):
    options = []
    for i in range(len(info)):
        answers = info[i]['incorrectAnswers']
        answers.append(correct[i])
        random.shuffle(answers)

        options.append(answers)

    return options


def display_question(questions, question_number):
    index = question_number - 1
    print(f'----------QUESTION {question_number}----------')
    print()
    print(f'{questions[index]}')
    print()


def display_options(options, question_number):
    index = question_number - 1
    answers = options[index]
    for i in range(len(answers)):
        print(f'[{i + 1}] {answers[i]}')


def user_answer():
    while True:
        try:
            ans = input('ANS: ')
            if ans.strip().lower() in ['q', 'quit']:
                print('Goodbye!')
                exit()
            elif ans.strip().isdigit() and 0 < int(ans) < 5:
                return int(ans)
            else:
                raise ValueError
        except ValueError:
            print('Sorry, please enter 1, 2, 3, or 4. Enter Q to quit')


def is_correct(user_choice, option_list, question_number, answer_list):
    if option_list[question_number - 1][user_choice - 1] == answer_list[question_number - 1]:
        return True
    else:
        return False


def play_again():
    while True:
        try:
            again = input('Play again? y/n: ').lower().strip()
            if again == 'y':
                return True
            elif again == 'n':
                return False
            else:
                raise ValueError
        except ValueError:
            print('Please enter either y or n')

