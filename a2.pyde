import random

grid_size = 3
cell_size = 80
moves = 0
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
    size(grid_size * cell_size, grid_size * cell_size + 60)
    reset_game()

def reset_game():
    global grid, moves, game_over
    grid = create_grid()
    moves = 0
    game_over = False

    k = 0
    while k < 10:
        rx = random.randint(0, grid_size - 1)
        ry = random.randint(0, grid_size - 1)
        toggle(rx, ry)
        k += 1
    moves = 0

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

def save_game():
    with open("save.txt", "w") as f:
        f.write("count=\n")
        f.write(str(moves) + "\n")
        f.write("check_win=\n")
        f.write(("1" if game_over else "0") + "\n")
        f.write("grid=\n")
        
        i = 0
        while i < grid_size:
            row_str = ""
            j = 0
            while j < grid_size:
                row_str += str(grid[i][j])
                if j < grid_size - 1:
                    row_str += " "
                j += 1
            f.write(row_str + "\n")
            i += 1
    print("Game Saved to save.txt!")

def load_game():
    global grid, moves, game_over
    try:
        with open("save.txt", "r") as f:
            lines = f.read().splitlines()

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line == "count=":
                i += 1
                moves = int(lines[i].strip())
            elif line == "check_win=":
                i += 1
                game_over = (lines[i].strip() == "1")
            elif line == "grid=":
                i += 1
                new_grid = []
                r = 0
                while r < grid_size:
                    row_vals = lines[i].strip().split()
                    row = []
                    c = 0
                    while c < grid_size:
                        row.append(int(row_vals[c]))
                        c += 1
                    new_grid.append(row)
                    i += 1
                    r += 1
                grid = new_grid
                continue
            i += 1
        print("Game Loaded from save.txt!")
    except Exception as e:
        print("No save.txt file found or format error.")

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

    fill(200)
    textSize(14)
    textAlign(CENTER, CENTER)
    text("Moves: " + str(moves), width / 2, grid_size * cell_size + 18)
    text("S: Save | L: Load | R: Reset", width / 2, grid_size * cell_size + 38)

    if game_over:
        fill(0, 0, 0, 210)
        rect(0, 0, width, height)
        fill(34, 197, 94)
        textSize(32)
        textAlign(CENTER, CENTER)
        text("YOU WIN!", width / 2, height / 2 - 15)
        textSize(16)
        fill(255)
        text("Total Moves: " + str(moves), width / 2, height / 2 + 20)

def mousePressed():
    global moves, game_over

    if game_over:
        return

    y = mouseX // cell_size
    x = mouseY // cell_size

    if 0 <= x < grid_size and 0 <= y < grid_size:
        toggle(x, y)
        moves += 1
        if check_win():
            game_over = True

def keyPressed():
    if key == 's' or key == 'S':
        save_game()
    elif key == 'l' or key == 'L':
        load_game()
    elif key == 'r' or key == 'R':
        reset_game()
