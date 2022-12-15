"""
Unscramble implementation by Tiwalade Omotosho

YouTube Kylie Ying: https://www.youtube.com/@tiwaomotosho
Twitter @tiwaomotosho: https://twitter.com/tiwaomotosho
Github: https://www.github.com/tiwaomotosho
"""

import random
from words import words

# Definition of attributes for the game levels
# Easy, Intermediate, Hard, and Legendary
TOTAL_PLAY = 0
WON_PLAY = 0
MAX_WORD = max(map(len, words))  # longest word

# Properties for all levels
# TRIES - This helps to complete a blank space at random
# MIN_W - This is the minimum word count
# MAX_W - This is the maximum word count


levels = {"E": {'TRIES': 3, 'MIN_W': 4, 'MAX_W': 7},
          'I': {'TRIES': 2, 'MIN_W': 7, 'MAX_W': 10},
          'H': {'TRIES': 2, 'MIN_W': 10, 'MAX_W': 12},
          'L': {'TRIES': 1, 'MIN_W': 12, 'MAX_W': MAX_WORD},
          }


def difficulty():
    print("""
    Welcome to Unscramble 1.0 by Tiwalade Omotosho
    Here, you are expected to rearrange random letters to form a word
    
    Type E, I, H, or L for Easy, Intermediate, Hard, or Legendary (no quotes)
    In Easy, you have 3 tries and 4-7 letter word
    In Intermediate, you have 2 tries and 7-10 letter word
    In Hard, you have 2 tries and 10-12 letter word
    In Legendary, you have 1 try and minimum of 12 letter word\n""")

    letter = ''
    while True:
        if letter in ["E", "I", "H", "L"]:
            break
        else:
            letter = input('Please enter a valid input>>> ').upper()

    return letter


def get_valid_word(get_diff, word_list=words):
    lb = levels[get_diff]['MIN_W']  # Minimum word count
    ub = levels[get_diff]['MAX_W']  # Maximum word count
    word_list = [word for word in word_list if lb <= len(word) <= ub]
    word = random.choice(word_list)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(word_list)

    return word.upper()


def unscramble():
    get_diff = difficulty()
    word = get_valid_word(get_diff)
    index_set = set(range(len(word)))
    words_scramble = list(word)
    random.shuffle(words_scramble)
    tries = levels[get_diff]['TRIES']
    hint_word = ['-'] * len(word)

    # Getting User input
    while tries > 0:
        print('You have', tries, 'attempt(s) left. Rearrange the letters of', ''.join(words_scramble), 'to form a word')
        user_letter = input('Whats the word?: ').upper()
        if user_letter == word:
            break
        else:
            tries += -1
            if tries > 0:
                index = random.choice(list(index_set))
                print('\nReshuffling the letters...\n')
                random.shuffle(words_scramble)
                index_set.remove(index)
                hint_word[index] = word[index]
                print('The correct word looks like', ''.join(hint_word), '. We hope you will get it right this time')

    # gets here when tries == 0
    global TOTAL_PLAY, WON_PLAY
    TOTAL_PLAY += 1
    if tries == 0:
        print('You lost, sorry. The word was', word)
    else:
        WON_PLAY += 1
        print('YAY! You got the word', word, '!!')


if __name__ == '__main__':
    unscramble()


while True:
    user_decision = input('\nDo you want to continue playing? (y/n): ').upper()
    if user_decision == 'Y':
        unscramble()
    elif user_decision == 'N':
        print(f'\nYou won {WON_PLAY} out of {TOTAL_PLAY} games')
        print('Thanks for your time. Do have a great day!!!')
        break
    else:
        print("please check your input")
