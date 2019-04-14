room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
             ]

for y in range(7):
    for x in range(5):
        print(room_map[y][x], end="")#using end="" so all items from one complete run of the x loop show on the same line
    print()

#istress = ["Mayday!"]
#for y in range(3):
    #print(distress)