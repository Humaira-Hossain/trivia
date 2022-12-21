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


number_of_questions()