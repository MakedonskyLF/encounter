#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import product
from itertools import permutations


def find_letters(num: int, prefix: str, sufix: str, dictionary):
    prefix_dict = (word for word in dictionary if (len(word) == (len(prefix) + num)) and (word.startswith(prefix)))
    sufix_dict = set(word for word in dictionary if (len(word) == (len(sufix) + num)) and (word.endswith(sufix)))
    res = set()
    for word in prefix_dict:
        if (word[-num:] + sufix) in sufix_dict: res.add(word[-num:])
    return res


def render(question: str):
    question = question.lower().strip()
    prefix = question.split('(')[0]
    sufix = question.split(')')[-1]
    num = len(question) - len(prefix) - len(sufix) - 2
    return dict(num=num, prefix=prefix, sufix=sufix)


def find_word(*args, dictionary):
    words=[]
    for case in permutations(args, len(args)):
        for test_word in product(*case):
            if ''.join(test_word) in dictionary: words.append(''.join(test_word))
    return words


def solve(*args, dictionary):
    letters = []
    for arg in args: letters.append(list(find_letters(**render(arg), dictionary=dictionary)))
    return find_word(*letters, dictionary=dictionary)
