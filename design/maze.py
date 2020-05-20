# ==============================================
# = Module for labyrinth design and management =
# ==============================================

import pygame as pg
from random import sample
from design import constants as cst


class GameBoard(list):

    def __init__(self):
        """ Window game settings """
        # -- Init game window
        self.master = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE + 55))
        self.title = pg.display.set_caption(cst.GAME_TITLE)
        self.icon = pg.image.load(cst.MACGYVER_PIC)
        pg.display.set_icon(self.icon)

        # -- Init game pictures
        self.wall = pg.image.load(cst.FULLWALL_PIC).convert_alpha()
        self.guard = pg.image.load(cst.GUARDIAN_PIC).convert_alpha()
        self.bkg = pg.image.load(cst.BKG_PIC).convert_alpha()
        self.itempic = (pg.image.load(cst.NEEDLE_PIC).convert_alpha(),
                        pg.image.load(cst.PIPE_PIC).convert_alpha(),
                        pg.image.load(cst.ETHER_PIC).convert_alpha())

        # -- Repeat the moves when the arrow keys are held down.
        pg.key.set_repeat(200, 200)

    # ------------------------------------------------------------------------
    def lab_struct(self):
        # -- Init structure of labyrinth
        with open('design/labyrinth') as maze:
            maze = ''.join(maze.read().splitlines())
            # -- Init Guard
            self.gdpos = divmod(maze.find('G'), 15)
            #self.extend([self.gdpos])
            # -- Init empty sprites
            self.extend([divmod(idx, 15) for idx, value in enumerate(maze)
                        if value == '0'])
            # -- Init items
            self.itempos = sample(self[1:], 3)

    # -------------------------------------------------------------------------
    def draw_objects(self):
        # -- Display walls as background
        self.master.blit(self.wall, (0, 0))
        # -- Display and positioning Guard
        gdy, gdx = self.gdpos
        self.master.blit(self.guard, (gdx * 50, gdy * 50))
        # -- Draw the empty path
        for y, x in self:
            self.master.blit(self.bkg, (x * 50, y * 50),
                             (x * 50, y * 50, 50, 50))
        # -- Display and positioning items
        for it, (y, x) in zip(self.itempic, self.itempos):
            self.master.blit(it, (x * 50, y * 50))
