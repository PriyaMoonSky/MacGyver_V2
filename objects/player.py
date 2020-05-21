# ==================================
# = Module for MacGyver management =
# ==================================

import pygame as pg
from design import constants as cst


class McGyver(object):

    def __init__(self, screen):
        self.bkg = cst.BKG_PIC.convert_alpha()
        self.syringepic = cst.SYRINGE_PIC.convert_alpha()
        self.macpic = cst.MACGYVER_PIC.convert_alpha()
        self.macpos = (0, 0)

        self.screen = screen
        self.screen.master.blit(self.macpic, self.macpos)

        self.arrows = {pg.K_UP: (-1, 0),
                       pg.K_DOWN: (1, 0),
                       pg.K_LEFT: (0, -1),
                       pg.K_RIGHT: (0, 1)}

    # -------------------------------------------------------------------------
    def del_mac(self):
        y, x = self.macpos
        self.screen.master.blit(self.bkg, (x * 50, y * 50),
                                (x * 50, y * 50, 50, 50))

    # -------------------------------------------------------------------------
    def update_mac(self, key, board):
        y, x = self.macpos

        offy, offx = self.arrows.get(key, (50, 0))
        if (y + offy, x + offx) in board:
            self.macpos = (y + offy, x + offx)

    # -------------------------------------------------------------------------
    def show_mac(self):
        y, x = self.macpos
        self.screen.master.blit(self.macpic, (x * 50, y * 50))

    # -------------------------------------------------------------------------
    def pickup(self, board, counter):
        if self.macpos in board.itempos:
            board.itempos.remove(self.macpos)
            counter.decrease()
