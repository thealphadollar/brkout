from __future__ import absolute_import

# function to set path to current folder (py 2 to 3)
from builtins import str
from builtins import chr
def import_modify():
    if __name__ == '__main__':
        if __package__ is None:
            import sys
            from os import path
            sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

import random
try:
    from .constants import *
except SystemError:
    from constants import *    
import string

# An untampered file will have 12048 characters in it with the only $ character
# in the 5734 th position after which 9 digits follow the first five of which is the score
# and the rest four is the time

# The high score can only be tampered if a $ sign is inserted anywhere in the file
# or the numbers after the $ is changed

# For other means of disturbing the file have been taken care of

ini_score = "000000000"  # combination of time and score


def encode(score_str):  # function to encode the string
    i = 0
    score = ""
    while i < 9:
        a = score_str[i]
        score += chr(ord(a) + i*5)
        i += 1
    return score


def decode(score_str):  # function to decode the string
    i = 0
    score = ""
    while i < 9:
        a = score_str[i]
        score += chr(ord(a) - i*5)
        i += 1
    return score

# Function returns 1/0 (1 for a tampered file, 0 otherwise), score, time


def read_highscore():
    ini_score = "000000000"  # combination of time and score
    try:
        file_name = open("highscore.txt")
        contents = file_name.read()
        position = contents.find('$')

        # If length is not 12048 characters or 5734 th character is not $
        if len(contents) == 12048 and contents[5733] == '$':
            encoded_score = contents[position + 1:position + 10]
            decoded_score = decode(encoded_score)
            if decoded_score.isdigit():
                return decoded_score[:5], decoded_score[-4:]
            else:
                raise IOError

        else:
            # If dollar sign is not present
            if position == -1:
                raise IOError

            else:
                encoded_score = contents[position + 1:position + 10]
                decoded_score = decode(encoded_score)
                if decoded_score.isdigit():
                    ini_score = decoded_score
                raise IOError

    except IOError:
        file_name = open("highscore.txt", "w")
        x = 1
        while x < 12049:
            y = random.choice(file_list)
            file_name.write(chr(y))
            x += 1
        file_name.seek(5733)
        file_name.write("$"+encode(ini_score))
        file_name.close()
        return ini_score[:5], ini_score[-4:]

# Writes the score and time


def write_highscore(score, time1, time2, time3, time4):
    file_name = open("highscore.txt", "r+")
    file_name.seek(5733)
    cor_str = str(score)
    while len(cor_str) < 5:
        cor_str = '0' + cor_str
    file_name.write("$"+encode(cor_str + str(time1) +
                               str(time2) + str(time3) + str(time4)))
    file_name.close()
