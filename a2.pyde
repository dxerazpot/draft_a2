import random
grid_size = 5
cell_size = 100

grid = []

def setup():
    size(500, 500)

def toggle(x, y):

def draw():
    background(0)
        i = 0
        while i < grid_size:
            j = 0
            while j < grid_size:
                if grid[i][j] == 1:
                    fill(255) 
                else:
                    fill(40)
                stroke(80)
                strokeWeight(2)
                rect(j * cell_size, i * cell_size, cell_size, cell_size)
                j += 1
            i += 1
def check_win():

def mousePressed():
    y = mouseX // cell_size
    x = mouseY // cell_size

    if 0 <= x < cell_size and 0 <= y < cell_size:
        toggle(x, y)
