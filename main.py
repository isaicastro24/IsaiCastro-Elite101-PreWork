
from datetime import date # found from python library

today = date.today() # intitializes date variable to tell the current day when user opens program
 

print('Hello!')
name = input('What is your name? : ')
age = input('Pleased to meet you, ' + name +', how old are you? : ')

print('Great!')

reception = '''
    How may I assist you?
    1. What day is it?
    2. What is your name?
    3. What's your company's name?
    4. Exit
    '''



options = int(input(reception))  # allows the reception string to be able to be used as an input where user types numbers

while options != 1000000000: # any number besides 1,2,or 3 will cause the program to end
    if options == 1: #if user types 1
        print('\nThe day is', today )
        options = int(input(reception)) # re prompt the user
    elif options == 2: #if user types 2
        print('\nMy name is Isai the Chatbot!')
        options = int(input(reception))   # re prompt the user
    elif options == 3: #if user types 3
        print('\nCode2College!')
        options = int(input(reception))  # re prompt the user
    else: # if user types any other number besides those 3
        print("\nThanks for talking with me, " + name + "!" + "\nHave an awesome day!")
        break #end program

