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
    # ****************************************************************#
    elif 11 <= rank < 14:
        # name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(rank, suit)

    else:
        raise Exception("Rank out of range")
        # ****************************************************************#
        # try other....
        # else:
        #     name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        #     return FaceCard(name, suit)


# ****************************************************************#
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
# wrapping a collection class
# =====================================================================================================================#
# class Deck(object):
#     def __init__(self):
#         self._card = []
#         for rank in range(1, 14):
#             for suit in (Club, Diamond, Heart, Spade):
#                 self._card.append(card(rank, suit))
#         random.shuffle(self._card)
#
#     def pop(self):
#         return self._card.pop()
# =====================================================================================================================#
# extending a collection class
# =====================================================================================================================#
# class Deck(list):
#     def __init__(self):
#         super(Deck, self).__init__(card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))
#         random.shuffle(self)

class Deck(list):  # 此类实现将一副牌或者几副牌混合及切牌的功能
    def __init__(self, decks=1):  # 此处deck表示一共使用多少副牌
        super(Deck, self).__init__()
        for i in range(decks):
            self.extend(card(r + 1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))  # 返回Card类的不同实例
            random.shuffle(self)  # 将所有牌打乱顺序,就是所谓的洗牌
            # Return a random integer N such that a <= N <= b
            burn = random.randint(1, 52)  # 此处实现切牌的功能,随机取出一个数,然后将这些数量的牌舍弃不用
            for i in range(burn):
                self.pop()


class Hand(object):  # 创建一个类实现获取一手牌的模拟方法
    def __init__(self, dealer_card, *cards):  # 此处传递了连个参数,一个是位置参数,一个是元组参数
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def hard_total(self):  # 计算hard的和
        return sum(c.hard for c in self.cards)

    def soft_total(self):  # 计算soft的和
        return sum(c.soft for c in self.cards)


class GameStrategy(object):
    def insurance(self, hand):  # 如果庄家牌面朝上的牌是A,玩家可以买保险,也就是相当于原赌金一半的额外赌金,如果玩家确信庄家
        # 下一张是10点牌,则可以买保险.如果庄家确实是黑杰克,则玩家可以赢的2倍的保险赌金;如果庄家没有,玩家将输掉保险赌金
        return False

    def split(self, hand):  # 分牌, 再下一注与原赌金相等的赌金即可分牌,就可将前两张牌分成两副单独的牌,这两张牌的点数必须相同,
        # 分牌后的黑杰克只能当作普通的21点计算,赔率是1赔1
        return False

    def doule(self, hand):  # 双倍下注
        return False

    def hit(self, hand):  # 拿牌, 只要玩家(包括闲家和庄家)手上的牌不超过21点都可以拿牌
        return sum(c.hard for c in hand.cards) <= 17


class Table(object):
    def __init__(self):
        self.deck = Deck()

    def place_bet(self, amount):
        print("Bet", amount)

    def get_hand(self):
        try:
            self.hand = Hand(d.pop(), d.pop(), d.pop())
            self.hole_card = d.pop()
        except  IndexError:
            self.deck = Deck()
            return self.get_hand()
        print("Deal", self.hand)
        return self.hand

    def can_insure(self, hand):
        return hand.dealer_card.insure


if __name__ == '__main__':
    Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')

    d = Deck()  # 创建一副洗好并且实现了切牌的一副牌
    h = Hand(d.pop(), d.pop(), d.pop())  # 此处第一个d.pop()传递给位置参数dealer_card,后两个d.pop()作为元组参数传递给*cards,之后
    # 转变成包含两张牌的列表
    # h.cards.append(d.pop())
    # h.cards.append(d.pop())
    # print (h.hard_total())
    # print (h.soft_total())
    for item in h.cards:
        print("rank: {0}\tsuit: {1}".format(item.rank, item.suit.symbol))
