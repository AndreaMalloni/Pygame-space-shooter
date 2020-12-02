from constants import *


class Surface(object):
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.animations = img
        self.hitbox = (0, 0, 0, 0)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getW(self):
        return self.width

    def getH(self):
        return self.height

    def getBox(self):
        return self.hitbox

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setW(self, w):
        self.width = w

    def setH(self, h):
        self.height = h

    def setBox(self, rect):
        self.hitbox = rect

    def draw(self):
        pass


class Movable(Surface):
    def __init__(self, x, y, w, h, img, spd):
        super().__init__(x, y, w, h, img)
        self.speed = spd
        self.dir = IDLE

    def getSpd(self):
        return self.speed

    def getDir(self):
        return self.dir

    def setSpd(self, spd):
        self.speed = spd

    def setDir(self, dir):
        self.dir = dir

    def move(self):
        pass
