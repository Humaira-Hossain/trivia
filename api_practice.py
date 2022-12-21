import requests
from pprint import pprint as pp
import random


def number_of_questions():
    while True:
        try:
            num = int(input('How many questions do you want to answer? '))

            if num == 0:
                print('Please enter a number greater than zero')
                continue
        except ValueError:
            print('Please enter a whole number')
        else:
            print('Thank you')
            break

    return num


def get_questions(number):
    num = str(number)
    endpoint = f'https://the-trivia-api.com/api/questions?limit={num}&difficulty=easy'
    response = requests.get(endpoint)

    info = response.json()
    return info


# for i in info:
#     print(i['question'])

# pp(info)
# pp(info[0]['question'])
# print(info[0]['incorrectAnswers'])

num = number_of_questions()
info = get_questions(num)

for i in info:
    print(i['question'])


