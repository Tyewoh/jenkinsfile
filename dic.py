'''
Created on Feb 11, 2019
@author: tyewoh
'''
import json
from difflib import get_close_matches

tay = json.load(open(r'C:\Users\tyewo\OneDrive\Desktop\UD1\data.json', 'r'))


def kay(word):
    word = word.lower()

    if word in tay:
        return tay.get(word)

    elif len(get_close_matches(word, tay.keys(), 3, 0.8)) > 0:
        lob = input("Did you mean to search for %s? Enter Y for Yes and N for No" % get_close_matches(word, tay.keys(), 1, 0.8)[0])
        if lob == 'Y' or lob == 'y':
            return tay[get_close_matches(word, tay.keys(), 1, 0.8)[0]]
        else:
            return 'The word you entered does not exist! Enter another word!'

    else:
        return 'The word you entered does not exist! Enter another word!'

word = input('Enter a word: ')
print(kay(word))
