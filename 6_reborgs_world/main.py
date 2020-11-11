# Go to: https://reeborg.ca/reeborg.html
# Select 'Maze'
#Paste in code

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# moving in square infinite loop
square_loop_check = 0
square_loop_counter = 0

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
        square_loop_check += 1
    elif not wall_in_front():
        move()
    else:
        turn_left()
    square_loop_counter += 1
    if square_loop_check == 4:
        turn_around()
        print("in the breakout")
    if square_loop_counter == 4:
        square_loop_counter = 0
        square_loop_check = 0
