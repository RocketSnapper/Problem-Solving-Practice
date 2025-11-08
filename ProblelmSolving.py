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