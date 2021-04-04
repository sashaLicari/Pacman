import pygame as pg

import game_functions as gf
from maze import Maze
from settings import Settings


# ===================================================================================================
# class Game
# ===================================================================================================
# noinspection PyArgumentList
def to_pixel(): pass


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("PacMan Portal")
        self.font = pg.font.SysFont(None, 48)

        self.maze = Maze()

        self.pacman = self.pacman(game=self)
        from character import Blinky
        from character import Pinky
        from character import Clyde
        from character import Inky
        self.ghosts = [Blinky(game=self), Pinky(game=self), Clyde(game=self), Inky(game=self)]
        for ghost in self.ghosts:
            ghost.set_ghosts(self.ghosts)
        self.finished = False

    def to_grid(self, index):
        row = index // 11
        offset = index % 11
        ss = self.maze.location(row, offset)
        return ss

    def play(self):
        while not self.finished:
            gf.check_events(game=self)
            # self.screen.fill(self.settings.bg_color)
            self.maze.update()
            for ghost in self.ghosts: ghost.update()
            self.pacman.update()
            pg.display.flip()


def main():
    game = Game()
    game.play()


if __name__ == '__main__': main()

