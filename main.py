import pygame as pg
from view.menu import *
from model.constants import *

pg.init()

clock = pg.time.Clock()

window = pg.display.set_mode((D_WIDTH, D_HEIGHT))
pg.display.set_caption("Shooter")
