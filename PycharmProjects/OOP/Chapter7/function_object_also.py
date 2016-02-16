#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: function_object_also.py
@time: 2016/2/11 20:08
"""

# def my_function():
#     print("The Function Was Called")
#
#
# my_function.description = "A silly function"
#
#
# def second_function():
#     print("The second was called")
#
#
# second_function.description = "A sillier function"
#
#
# def another_funtion(function):
#     print("The description:", end=" ")
#     print(function.description)
#     print("The name:", end=" ")
#     print(function.__name__)
#     print("The class:", end=" ")
#     print(function.__class__)
#     print("Now I'll call the function passed in")
#     function()
#
#
# another_funtion(my_function)
# another_funtion(second_function)

import datetime
import time


class TimedEvent(object):
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer(object):
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)


def format_time(message, *args):
    now = datetime.datetime.now().strftime("%I:%M:%S")
    print(message.format(*args, now=now))


def one():
    format_time("{now}: Called One")

timer = Timer()
timer.call_after(5, one)
timer.run()
