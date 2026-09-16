import random
grid_size = 5
cell_size = 100

grid = []

def setup():
    size(500, 500)

def toggle(x, y):

def draw():


def mousePressed():
    y = mouseX // cell_size
    x = mouseY // cell_size

    if 0 <= x < cell_size and 0 <= y < cell_size:
        toggle(x, y)
