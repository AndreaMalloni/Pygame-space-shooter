import surface as sf


class Button(sf.Surface):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.pointed = False

    def getPoint(self) -> bool:
        return self.pointed

    def setPoint(self):
        self.pointed = not self.pointed

    def click(self):
        pass


class Entity(sf.Movable):
    def __init__(self, x, y, w, h, speed = 1.0, hp = 0.0):
        super().__init__(x, y, w, h, speed)
        self.health = hp

    def getHP(self) -> float:
        return self.health

    def setHP(self, hp):
        self.health = hp

    def die(self):
        pass


class Bullet(sf.Movable):
    def __init__(self, x, y, w, h, speed = 1.0, dmg = 1.0, multi = 1.0, rad = 1.0):
        super().__init__(x, y, w, h, speed)
        self.dmg = dmg
        self.multiplier = multi
        self.radius = rad

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

    def move(self):
        pass


class Player(Entity):
    def __init__(self, x, y, w, h, speed = 1.0, hp = 0.0, rate = 1.0, shield = 0.0):
        super().__init__(x, y, w, h, speed, hp)
        self.fireRate = rate
        self.shield = shield

    def getShield(self) -> float:
        return self.shield

    def getRate(self) -> float:
        return self.fireRate

    def setShield(self, shield):
        self.shield = shield

    def setRate(self, rate):
        self.fireRate = rate

    def shoot(self):
        pass
