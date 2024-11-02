import random
import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Recycle paper game"
center_x = WIDTH// 2
center_y = HEIGHT// 2
center = (center_x, center_y)
final_level = 8
start_speed = 10
ITEMS = ["bag", "battery", "bottle", "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        desplay_message("Game over", "Try again next time.")
    elif game_complete:
        desplay_message("You win!", "Good job:)")
    else:
        for item in items:
            item.draw()

def desplay_message(main_msg, sub_msg):
    screen.draw.text(main_msg, fontsize = 60, color = "white", center = (center_x, center_y))
    screen.draw.text(sub_msg, fontsize = 30, color = "white", center = (center_x, center_y + 30))
    

def update():
    global items
    if len (items) == 0 :
        items = make_items(current_level)




pgzrun.go()

