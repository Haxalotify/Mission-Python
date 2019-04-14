room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
             ]

WIDTH = 800
HEIGHT = 600

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar]

room_height = 7
room_width = 5

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw,
                    (top_left_x + (x*30),#each square of image is 30 pixels. tells where to place the image based off of window size
                    top_left_y + (y*30) - image_to_draw.get_height()))

#for y in range(7):
    #for x in range(5):
        #print(room_map[y][x], end="")#using end="" so all items from one complete run of the x loop show on the same line
    #print()

#istress = ["Mayday!"]
#for y in range(3):
    #print(distress)