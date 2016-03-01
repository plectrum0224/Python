#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: FacadePattern.py
@time: 2016/2/28 19:44
"""
class Lights:
    def dim(self, value):
        print("dim the light 10")
    def on(self):
        print("light on")

class Popper:
    def on(self):
        print("popper on")
    def off(self):
        print("popper off")
    def pop(self):
        print("popper pop")

class HomeTheaterFacade:
    def __init__(self, lights, popper):
        # self.amp = amp
        # self.tuner = tuner
        # self.dvd = dvd
        # self.cd = cd
        # self.projector = projector
        # self.screen = screen
        self.lights = lights
        self.popper = popper


    def watchMovie(self):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        # self.screen.down()
        # self.projector.on()
        # self.projector.wideScreenMode()
        # self.amp.on()
        # self.amp.setDvd()
        # self.amp.setSurroundSound()
        # self.amp.setVolume(5)
        # self.dvd.on()
        # self.dvd.play(movie)

    def endMovie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        # self.screen.up()
        # self.projector.off()
        # self.amp.off()
        # self.dvd.stop()
        # self.dvd.eject()
        # self.dvd.off()

def main():
    homeTheater = HomeTheaterFacade(Lights(), Popper())
    homeTheater.watchMovie()
    homeTheater.endMovie()

if __name__ == '__main__':
    main()
