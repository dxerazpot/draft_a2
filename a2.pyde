import random

grid_size = 5
cell_size = 80
moves = 0
game_over = False

def create_grid():
    return [[0] * grid_size for _ in range(grid_size)]

grid = create_grid()

def setup():
    size(grid_size * cell_size, grid_size * cell_size + 60)
    reset_game()

def reset_game():
    global grid, moves, game_over
    grid = create_grid()
    moves = 0
    game_over = False

    for _ in range(10):
        rx = random.randint(0, grid_size - 1)
        ry = random.randint(0, grid_size - 1)
        toggle(rx, ry)
    moves = 0

def toggle(x, y):
    targets = [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for tx, ty in targets:
        if 0 <= tx < grid_size and 0 <= ty < grid_size:
            grid[tx][ty] = 1 - grid[tx][ty]

def check_win():
    return all(cell == 0 for row in grid for cell in row)

def save_game():
    with open("save.txt", "w") as f:
        f.write("count=\n")
        f.write(str(moves) + "\n")
        f.write("check_win=\n")
        f.write(("1" if game_over else "0") + "\n")
        f.write("grid=\n")
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")
    print("Game Saved to save.txt!")

def load_game():
    global grid, moves, game_over
    try:
        with open("save.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        for i, line in enumerate(lines):
            if line == "count=":
                moves = int(lines[i + 1])
            elif line == "check_win=":
                game_over = (lines[i + 1] == "1")
            elif line == "grid=":
                grid = [[int(val) for val in lines[i + 1 + r].split()] for r in range(grid_size)]
        print("Game Loaded from save.txt!")
    except Exception as e:
        print("No save.txt file found or format error.")

def draw():
    hover_col = mouseX // cell_size
    hover_row = mouseY // cell_size
    hover_active = not game_over and (0 <= hover_row < grid_size) and (0 <= hover_col < grid_size)

    for i in range(grid_size):
        for j in range(grid_size):
            is_hover = hover_active and (abs(i - hover_row) + abs(j - hover_col) <= 1)

            if grid[i][j] == 1:
                fill(170 if is_hover else 255)
            else:
                fill(15 if is_hover else 40)

            stroke(80)
            strokeWeight(2)
            rect(j * cell_size, i * cell_size, cell_size, cell_size)

    fill(30)
    noStroke()
    rect(0, grid_size * cell_size, width, 60)

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
    k = str(key).lower()
    if k == 's':
        save_game()
    elif k == 'l':
        load_game()
    elif k == 'r':
        reset_game()
