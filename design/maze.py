# ==============================================
# = Module for labyrinth design and management =
# ==============================================

import pygame as pg
from random import sample
from design import constants as cst


class GameBoard(list):

    def __init__(self):
        # -- Init game window
        self.master = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE + 55))
        self.title = pg.display.set_caption(cst.GAME_TITLE)
        self.icon = cst.MACGYVER_PIC
        pg.display.set_icon(self.icon)

        # -- Init game pictures
        self.wallpic = cst.FULLWALL_PIC.convert_alpha()
        self.guardpic = cst.GUARDIAN_PIC.convert_alpha()
        self.bkg = cst.BKG_PIC.convert_alpha()
        self.syringepic = cst.SYRINGE_PIC.convert_alpha()
        self.win = cst.YOUWIN_PIC.convert_alpha()
        self.loose = cst.GAMEOVER_PIC.convert_alpha()
        self.itempic = (cst.NEEDLE_PIC.convert_alpha(),
                        cst.PIPE_PIC.convert_alpha(),
                        cst.ETHER_PIC.convert_alpha())

        # -- Repeat the moves when the arrow keys are held down.
        pg.key.set_repeat(50, 100)

    # ------------------------------------------------------------------------
    def lab_struct(self):
        # -- Init structure of labyrinth
        with open('design/labyrinth') as maze:
            maze = ''.join(maze.read().splitlines())
            # -- Init empty sprites
            self.extend([divmod(idx, 15) for idx, value in enumerate(maze)
                        if value == '0'])
            # -- Init Guard
            self.gdpos = divmod(maze.find('G'), 15)
            self.extend([self.gdpos])
            # -- Init the 3 items random position
            self.itempos = sample(self[1:], 3)

            return self

    # -------------------------------------------------------------------------
    def draw_objects(self):
        # -- Display walls as background
        self.master.blit(self.wallpic, (0, 0))
        # -- Display and positioning Guard
        gdy, gdx = self.gdpos
        self.master.blit(self.guardpic, (gdx * 50, gdy * 50))
        # -- Draw the empty path
        for y, x in self:
            self.master.blit(self.bkg, (x * 50, y * 50),
                             (x * 50, y * 50, 50, 50))
        # -- Display and positioning items
        for it, (y, x) in zip(self.itempic, self.itempos):
            self.master.blit(it, (x * 50, y * 50))

    # -------------------------------------------------------------------------
    def itembar(self):
        print(self.itempos)
        if len(self.itempos) == 2:
            self.master.blit(self.itempic[0], (0, 752))
        if len(self.itempos) == 1:
            self.master.blit(self.itempic[1], (50, 752))
        if len(self.itempos) == 0:
            self.master.blit(self.itempic[2], (100, 752))
            self.master.blit(self.syringepic, (390, 752))

    # -------------------------------------------------------------------------
    def win_loose(self):
        # if macgyver pos == guard pos:
        if len(self.itempos) == 0:
            self.endgame = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE))
            self.endgame.blit(self.win, (0, 0))
            print("--- YOU WIN ---")
        elif len(self.itempos) == 1:    # != 0
            self.endgame = pg.display.set_mode((cst.WINSIZE, cst.WINSIZE))
            self.endgame.blit(self.loose, (0, 0))
            print("--- ITEMS MISSING ---")
