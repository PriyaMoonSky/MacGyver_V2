# ==================================
# = Module for MacGyver management =
# ==================================

#                            TESTING MODE

import pygame as pg
from design import constants as cst


class McGyver:

    def __init__(self, screen):
        self.macpic = pg.image.load(cst.MACGYVER_PIC).convert_alpha()
        self.macpos = (0, 0)

        screen.master.blit(self.macpic, self.macpos)

    #--------------------------------------------------------------------------
    def mac_moves(self):
        offset = {pg.K_UP: (-1, 0),
                  pg.K_DOWN: (1, 0),
                  pg.K_LEFT: (0, -1),
                  pg.K_RIGHT: (0, 1)}

    def mac_update(self, maze, screen):
        if (y + offy, x + offx) in maze:
            screen.master.blit(cst.BKG_PIC, (x * 50, y * 50),
                               (x * 50, y * 50, 50, 50))
            self.macpos = y, x = (y + offy, x + offx)
            screen.master.blit(self.macpic), (x * 50, y * 50)

            pg.display.flip()
