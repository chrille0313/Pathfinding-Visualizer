import pygame as pg


class CellView:
    def __init__(self, cell_size, wall_width=2):
        self.rect = pg.Rect((0, 0), cell_size)
        self.wall_width = wall_width

    def render(self, window, x, y, cell, colors):
        self.rect.topleft = x, y
        pg.draw.rect(window, colors.background, self.rect)
        pg.draw.circle(window, colors.wall, (x + self.rect.width // 2, y + self.rect.height // 2), 1)

        # Because pygame is retarded in how it renders lines, I had to do it like this
        if cell.walls[0]:
            pg.draw.line(window, colors.wall, self.rect.topleft, (x + self.rect.width, y), self.wall_width)
        if cell.walls[1]:
            pg.draw.line(window, colors.wall, (x + self.rect.width - self.wall_width, y), (x + self.rect.width - self.wall_width, y + self.rect.height), self.wall_width)
        if cell.walls[2]:
            pg.draw.line(window, colors.wall, (x, y + self.rect.height - self.wall_width), (x + self.rect.width - self.wall_width // 2, y + self.rect.height - self.wall_width), self.wall_width)
        if cell.walls[3]:
            pg.draw.line(window, colors.wall, self.rect.bottomleft, self.rect.topleft, self.wall_width)
