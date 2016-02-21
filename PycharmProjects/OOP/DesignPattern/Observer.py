#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: Observer.py
@time: 2016/2/21 11:42
"""


class Observed(object):
    def __init__(self):
        self.__observers = []

    def registerObservers(self, observer):
        self.__observers.append(observer)
        observer.update(self)

    def romoveObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update(self)


class WeatherModel(Observed):
    def __init__(self, temp, humidity, pressure):
        super(WeatherModel, self).__init__()
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

    def valueChanged(self, temp, humidity, pressure):
        if self.temp != temp or \
        self.humidity != humidity or \
        self.pressure != pressure:
            self.temp = temp
            self.humidity = humidity
            self.pressure = pressure
            self.notifyObservers()

class CurrentCondition(object):
    def __init__(self):
        self.currData = []
    def update(self, model):
        self.currData.append((model.temp, model.humidity, model.pressure))

class StaticsCondition(object):
    def __init__(self):
        self.statDataHumidity = []
        self.statDataTemp = []
        self.statDataPressure = []
    def update(self, model):
        self.statDataHumidity.append(model.humidity)
        self.statDataTemp.append(model.temp)
        self.statDataPressure.append(model.pressure)



def main():
    current = CurrentCondition()
    statistic = StaticsCondition()
    model = WeatherModel(20.0, 55.0, 1013.11)

    model.registerObservers(current)
    model.registerObservers(statistic)

    model.valueChanged(21.0, 52.3, 1013.12)
    model.valueChanged(21.2, 53.3, 1013.12)
    model.valueChanged(22.8, 56.1, 1013.18)

    print(current.currData)
    print(statistic.statDataTemp)
    print(statistic.statDataHumidity)
    print(statistic.statDataPressure)


if __name__ == '__main__':
    main()
# import datetime
# import time
#
#
# class Observed(object):
#     # 创建一个set用于存放需要进行通知的观察者
#     def __init__(self):
#         self.__observers = set()
#
#     def registerObservers(self, observer):
#         self.__observers.add(observer)
#         observer.update(self)
#
#     def removeObservers(self, observer):
#         self.__observers.discard(observer)
#
#     def notifyObservers(self):
#         for observer in self.__observers:
#             observer.update(self)
#
#
# class SliderModel(Observed):
#     def __init__(self, minimum, value, maximum):
#         super(SliderModel, self).__init__()
#         self.__minimum = self.__value = self.__maximum = None
#         self.minimum = minimum
#         self.value = value
#         self.maximum = maximum
#
#     # get value
#     @property
#     def value(self):
#         return self.__value
#
#     # set value
#     @value.setter
#     def value(self, value):
#         if self.__value != value:
#             self.__value = value
#             self.notifyObservers()
#
#     @property
#     def minimum(self):
#         return self.__minimum
#
#     @minimum.setter
#     def minimum(self, minimum):
#         if self.__minimum != minimum:
#             self.__minimum = minimum
#             self.notifyObservers()
#
#     @property
#     def maximum(self):
#         return self.__maximum
#
#     @maximum.setter
#     def maximum(self, maximum):
#         if self.__maximum != maximum:
#             self.__maximum = maximum
#             self.notifyObservers()
#
#
# class HistoryView(object):
#     def __init__(self):
#         self.data = []
#
#     def update(self, model):
#         self.data.append((model.value, time.time()))
#
#
# def main():
#     history = HistoryView()
#     model = SliderModel(0, 0, 40)
#     model.registerObservers(history)
#     for value in (7, 23, 38):
#         model.value = value
#     for value, timestamp in history.data:
#         print("{0}\t{1}".format(value, datetime.datetime.fromtimestamp(timestamp)))
#
#
# if __name__ == '__main__':
#     main()


# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#         if score < 0 or score >100:
#             raise ValueError('Invalid score')
#         self.__score = score
#
# s = Student('Bart', 59)
# s.score = 60
# print(s.score)
#
# s.score = 99
# print(s.score)
