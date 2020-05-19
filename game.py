#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

#                            TESTING MODE

# ==========================================================================
# =                  MACGYVER LABYRINTH GAME USING PYGAME                  =
# =                       OPENCLASSROOMS - PROJECT 03                      =
# =                                                                        =
# =  Help MacGyver to get out of the labyrinth.                            =
# =  He must get all items before he puts the guard to sleep and get out.  =
# =  Use direction arrows for MacGyver's moves                             =
# ==========================================================================

#--- Import Python modules
import pygame as pg
from os import system, environ
#--- Import personnal modules
from design import maze, constants as cst
from objects import player
# Not needed just for me
system('clear')
# -- Force center screen
environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()

def main():
    screen = maze.GameBoard()
    draw = screen.draw()
    hero = player.McGyver(screen)

    pg.display.flip()

    # -------------------------------------------------------------------------
    while True:
        #pg.time.Clock().tick(30)  # -- 30 FPS limit
        ev = pg.event.wait()
        key_pressed = pg.key.get_pressed()
        # -- Close the window game by the cross button or ESCAPE key
        if ev.type == pg.QUIT or key_pressed[pg.K_ESCAPE]:
            break
        elif ev.type == pg.KEYDOWN:
            hero.mac_update(draw.maze, screen)

        pg.display.flip()