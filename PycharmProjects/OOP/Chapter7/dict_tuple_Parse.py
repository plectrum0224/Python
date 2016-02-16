#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: dict_tuple_Parse.py
@time: 2016/2/9 10:15
"""
from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
                Book("Pratchett", "Nightwatch", "fantacy"),
                Book("Pratchett", "Thief of Time", "fantacy"),
                Book("Le Guin", "The Dispossessed", "scifi"),
                Book("Le Guin", "A Wizard of Earthsea", "fantacy"),
                Book("Turner", "The Thief", "fantacy"),
                Book("Phillips", "Preston Diamond", "western"),
                Book("Phillips", "Twice Upon A Time", "scifi"),
]
#  books :
# [
# Book(author='Pratchett', title='Nightwatch', genre='fantacy'),
# Book(author='Pratchett', title='Thief of Time', genre='fantacy'),
# Book(author='Le Guin', title='The Dispossessed', genre='scifi'),
# Book(author='Le Guin', title='A Wizard of Earthsea', genre='fantacy'),
# Book(author='Turner', title='The Thief', genre='fantacy'),
# Book(author='Phillips', title='Preston Diamond', genre='western'),
# Book(author='Phillips', title='Twice Upon A Time', genre='scifi')
# ]
fantacy_author = {
    b.author for b in books if b.genre == "fantacy"
}
fantacy_titles = {
    b.title: b for b in books if b.genre == 'fantacy'
}

print(fantacy_author)
# {'Pratchett', 'Le Guin', 'Turner'}
print(fantacy_titles)
