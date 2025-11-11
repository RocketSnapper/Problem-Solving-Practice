def combine_letters(team):
    first_last = team[0] + team[4]
    print(first_last)
combine_letters('Blues')

for number in range(101):
    if number % 3 == 0 and number % 5 == 0:
        print(f'{number} peanut butter jelly')
    elif number % 5 == 0:
        print(f'{number} jelly')
    elif number % 3 == 0:
        print(f'{number} peanut butter')

def letter_index(word):
    final_result = ''
    index_number = 0
    for character in word:
        index_number += 1
        final_result += str(index_number) + character
    print(final_result)
letter_index('Peace')

def ingredient_check(ingredients):
    user_search = input('What ingredient are you searching for?')
    for ingredient in ingredients:
        if ingredient == user_search:
            return ingredient
    user_choice = input('Ingredient not present, would you like to search again?')
    if user_choice == 'Yes':
        matched_ingredient = ingredient_check(['Salt', 'Pepper', 'Egg', 'Flour'])
matched_ingredient = ingredient_check(['Salt', 'Pepper', 'Egg', 'Flour'])

def reverse_list(sticks):
    last_index = len(sticks) - 1
    reversed_list = []
    while last_index >= 0:
        last_element = sticks.pop()
        reversed_list += [last_element]
        last_index -= 1
    return reversed_list

stick_list = reverse_list(['Tracer', 'Smoke', 'Pulse'])
print(stick_list)

def count_characters(names):
    new_list = []
    for name in names:
        if len(name) > 4:
            new_list += [name]
    return new_list        

atleast_five = count_characters(['Bob', 'Sam', 'Henry', 'Sally', 'Jonny', 'Thomas'])
print(atleast_five)

def reverse_string(word):
    new_string = ''
    for index in range(len(word) -1, -1, -1):
        new_string += word[index]
    return new_string

reversed_word = reverse_string('Hello') 
print(reversed_word)

def capitalize_first(words):
    cap_words = words.title()
    print(cap_words)
capitalize_first('hockey rules')

def palindrome_check():
    reversed_string = ''
    user_word = input('Pick a word')
    for index in range(len(user_word) -1, -1, -1):
        reversed_string += user_word[index]
    if user_word == reversed_string:
        print('Palindrome indeed!')
    else:
        print('Try again')

palindrome_check()

def string_compression():
    my_string = 'aaaabbvvvvkkkklllldddiiiiihwwww'
    last_character = my_string[0]
    count = 0
    new_string = ''
    for character in my_string:
        if character == last_character:
            count += 1
        else:
            new_string += last_character + str(count)
            last_character = character
            count = 1
    new_string += last_character + str(count)
    print(new_string)
string_compression()
