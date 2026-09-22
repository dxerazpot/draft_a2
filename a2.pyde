import random
grid_size = 3
cell_size = 100


grid = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1,]
]

def setup():
    size(300, 300)

def toggle(x, y):
    targets = [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    i = 0
    while i < len(targets):
        tx, ty = targets[i]
        if 0 <= tx < grid_size and 0 <= ty < grid_size:
            grid[tx][ty] = 1 - grid[tx][ty]
        i += 1

def draw():
    background(0)
    i = 0
    while i < grid_size:
        j = 0
        while j < grid_size:
            fill(255) if grid[i][j] == 1 else fill(40)
            stroke(80)
            strokeWeight(2)
            rect(j * cell_size, i * cell_size, cell_size, cell_size)
            j += 1
        i += 1

def mousePressed():
    y = mouseX // cell_size
    x = mouseY // cell_size

    if 0 <= x < cell_size and 0 <= y < cell_size:
        toggle(x, y)
