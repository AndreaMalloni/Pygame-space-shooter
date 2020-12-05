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


class Movable(Surface):
    def __init__(self, x, y, w, h, speed = 1.0):
        super().__init__(x, y, w, h)
        self.speed = speed
        self.dir = IDLE

    def getSpd(self) -> float:
        return self.speed

    def getDir(self) -> int:
        return self.dir

    def setSpd(self, spd):
        self.speed = spd

    def setDir(self, dir):
        self.dir = dir

    def move(self):
        dir = self.getDir()
        if dir == NORD:
            self.setXY(self.x, self.y - self.speed)
        elif dir == NORD_EST:
            self.setXY(self.x + self.speed, self.y - self.speed)
        elif dir == EST:
            self.setXY(self.x + self.speed, self.y)
        elif dir == SUD_EST:
            self.setXY(self.x - self.speed, self.y + self.speed)
        elif dir == SUD:
            self.setXY(self.x, self.y + self.speed)
        elif dir == SUD_OVEST:
            self.setXY(self.x - self.speed, self.y + self.speed)
        elif dir == OVEST:
            self.setXY(self.x - self.speed, self.y)
        elif dir == NORD_OVEST:
            self.setXY(self.x - self.speed, self.y - self.speed)
