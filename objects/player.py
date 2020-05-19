# ==================================
# = Module for MacGyver management =
# ==================================

#                            TESTING MODE

import pygame as pg
from design import constants as cst


class McGyver(object):

    def __init__(self, screen):
        self.macpic = pg.image.load(cst.MACGYVER_PIC).convert_alpha()
        self.macpos = (0, 0)

        screen.master.blit(self.macpic, self.macpos)

        self.arrows = {pg.K_UP: (-1, 0),
                       pg.K_DOWN: (1, 0),
                       pg.K_LEFT: (0, -1),
                       pg.K_RIGHT: (0, 1)}
        
    # -------------------------------------------------------------------------
    def del_mac(self):
        y, x = self.macpos
        screen.master.blit(cst.BKG_PIC, (x * 50, y * 50), (x * 50, y * 50, 50, 50))

    # -------------------------------------------------------------------------
    def update_mac(self, key, lab):
        y, x = self.macpos

        offy, offx = self.arrows.get(key, (0, 0))
        if (y + offy, x + offx) in lab:
            self.macpos = (y + offy, x + offx)

