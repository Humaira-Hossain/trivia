import random

example = [
    {
        'category': 'Geography',
        'correctAnswer': 'The Ganges',
        'difficulty': 'easy',
        'id': '6233843e62eaad73716a8bf7',
        'incorrectAnswers': ['The Indus', 'The Brahmaputra', 'The Krishna'],
        'isNiche': False,
        'question': 'What is the most sacred river in India?',
        'regions': [],
        'tags': ['rivers', 'bodies_of_water', 'religion', 'hinduism', 'geography'],
        'type': 'Multiple Choice'},
    {
        'category': 'Geography',
        'correctAnswer': 'Bilbao',
        'difficulty': 'easy',
        'id': '62602e034b176d54800e3cbb',
        'incorrectAnswers': ['Dublin', 'Stuttgart', 'Cologne'],
        'isNiche': False,
        'question': 'Which of these cities is in Spain?',
        'regions': [],
        'tags': ['cities', 'europe', 'spain', 'geography'],
        'type': 'Multiple Choice'
    }
]
#
options = example[0]['incorrectAnswers']
correct = example[0]['correctAnswer']

question = example[0]['question']

options.append(correct)
random.shuffle(options)

print(question)

for index in range(1, len(options) + 1):
    print(f'[{index}] {options[index - 1]}')

answer = input('ANSWER: ')
if options[int(answer) - 1] == correct:
    print('CORRECT :)')
else:
    print('INCORRECT :(')
