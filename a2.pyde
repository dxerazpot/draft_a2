import random

grid_size = 5
cell_size = 80
game_over = False

def create_grid():
    g = []
    i = 0
    while i < grid_size:
        row = []
        j = 0
        while j < grid_size:
            row.append(0)
            j += 1
        g.append(row)
        i += 1
    return g

grid = create_grid()

def setup():
    size(grid_size * cell_size, grid_size * cell_size)
    reset_game()

def reset_game():
    global grid, game_over
    grid = create_grid()
    game_over = False

    k = 0
    while k < 10:
        rx = random.randint(0, grid_size - 1)
        ry = random.randint(0, grid_size - 1)
        toggle(rx, ry)
        k += 1

def toggle(x, y):
    targets = [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    i = 0
    while i < len(targets):
        tx, ty = targets[i]
        if 0 <= tx < grid_size and 0 <= ty < grid_size:
            grid[tx][ty] = 1 - grid[tx][ty]
        i += 1

def check_win():
    i = 0
    while i < grid_size:
        j = 0
        while j < grid_size:
            if grid[i][j] == 1:
                return False
            j += 1
        i += 1
    return True

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

    if game_over:
        fill(0, 0, 0, 210)
        rect(0, 0, width, height)
        fill(34, 197, 94)
        textSize(32)
        textAlign(CENTER, CENTER)
        text("YOU WIN!", width / 2, height / 2)

def mousePressed():
    global game_over

    if game_over:
        return

    y = mouseX // cell_size
    x = mouseY // cell_size

    if 0 <= x < grid_size and 0 <= y < grid_size:
        toggle(x, y)
        if check_win():
            game_over = True

def keyPressed():
    if key == 'r' or key == 'R':
        reset_game()