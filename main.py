from funcs import *


def main():
    while True:
        num = number_of_questions()
        diff = difficulty()

        url = get_endpoint(num, diff)
        json = get_json(url)

        question_list = get_questions(json)
        answer_list = get_correct_answers(json)
        option_list = get_options(json, answer_list)

        score = 0
        question_number = 0
        while question_number < num:
            question_number += 1
            display_question(question_list, question_number)
            display_options(option_list, question_number)

            ans = user_answer()

            if is_correct(ans, option_list, question_number, answer_list):
                print('CORRECT!')
                print()
                score += 1
                continue
            else:
                print(f'Incorrect! The right answer was {answer_list[question_number-1]}')
                print()
                continue

        print(f'Thanks for playing! You got {score}/{num} right!')
        if not play_again():
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
