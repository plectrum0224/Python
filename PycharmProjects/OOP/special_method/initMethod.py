#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: initMethod.py
@time: 2016/2/15 22:08
"""

import random


# =====================================================================================================================#
# Create card class
# =====================================================================================================================#
class Card(object):
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        # self.hard, self.soft = self._points()
        self.hard = hard
        self.soft = soft


class NumberCard(Card):
    def __init__(self, rank, suit):
        super(NumberCard, self).__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank, suit):
        super(AceCard, self).__init__("A", suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank, suit):
        super(FaceCard, self).__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit, 10, 10)


# =====================================================================================================================#
# Creat suit class
# =====================================================================================================================#
class Suit(object):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


# =====================================================================================================================#
# callable Card class
# =====================================================================================================================#
def card(rank, suit):
    if rank == 1:
        return AceCard(rank, suit)

    elif 2 <= rank < 11:
        return NumberCard(rank, suit)
#****************************************************************#
    elif 11 <= rank < 14:
        # name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(rank, suit)

    else:
        raise Exception("Rank out of range")
#****************************************************************#
    # try other....
    # else:
    #     name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
    #     return FaceCard(name, suit)
#****************************************************************#
# use elif exchange the mapping method
#     elif rank == 11:
#         return FaceCard('J', suit)
#     elif rank == 12:
#         return FaceCard('Q', suit)
#     elif rank == 13:
#         return FaceCard('K', suit)
#     else:
#         raise Exception("Rank out of range")
# =====================================================================================================================#
# main function
# =====================================================================================================================#
if __name__ == '__main__':
    Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')

    deck = []
    for rank in range(1, 14):
        for suit in (Club, Diamond, Heart, Spade):
            deck.append(card(rank, suit))
    random.shuffle(deck)
    hand = [deck.pop(), deck.pop()]
    for item in hand:
        print("rank: {0}\tsuit: {1}".format(item.rank, item.suit.symbol))