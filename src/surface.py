from constants import *
import pygame as pg


class Surface(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.animations = []
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)

    def getXY(self) -> tuple:
        return self.x, self.y

    def getWH(self) -> tuple:
        return self.width, self.height

    def getBox(self) -> object:
        return self.hitbox

    def setXY(self, x, y):
        self.x, self.y = x, y
        self.__update()

    def setWH(self, w, h):
        self.width, self.height = w, h
        self.__update()

    def __update(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pass


class Button(Surface):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.pointed = False

    def getPoint(self) -> bool:
        return self.pointed

    def setPoint(self):
        self.pointed = not self.pointed

    def click(self):
        pass


class Movable(Surface):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.speed = 1
        self.dir = IDLE

    def getSpd(self) -> int:
        return self.speed

    def getDir(self) -> int:
        return self.dir

    def setSpd(self, spd):
        self.speed = spd

    def setDir(self, dir):
        self.dir = dir

    def move(self):
        pass


class Bullet(Movable):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.dmg = 1.0
        self.multiplier = 1.0
        self.radius = 0

    def getDmg(self) -> float:
        return self.dmg

    def getMulti(self) -> float:
        return self.multiplier

    def getRad(self) -> float:
        return self.radius

    def setDmg(self, dmg):
        self.dmg = dmg

    def setMulti(self, multiplier):
        self.multiplier = multiplier

    def setRad(self, radius):
        self.radius = radius

    def hit(self):
        pass
