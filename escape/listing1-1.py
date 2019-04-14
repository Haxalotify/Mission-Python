
#window size variables
WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350

def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))

def game_loop():
    global player_x, player_y #adding a player x, player y lets user control right, left, up, and down. if it was
    if keyboard.right:          #just player x or y, user would only be able to move 2 directions
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5

clock.schedule_interval(game_loop, 0.03)