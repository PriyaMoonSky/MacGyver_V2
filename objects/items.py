# ===============================
# = Module for items management =
# ===============================

#                            TESTING MODE

import pygame as pg
from design import constants as cst

class GameItems:

    def __init__(self):
        itempic = (pg.image.load(cst.NEEDLE_PIC).convert_alpha(),
                   pg.image.load(cst.PIPE_PIC).convert_alpha(),
                   pg.image.load(cst.ETHER_PIC).convert_alpha())