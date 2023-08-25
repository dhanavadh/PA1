from stanfordkarel import *

def main():
        move()
        while front_is_clear():
            go_down()
            fill_hole()

def go_down():
    while front_is_clear() and right_is_blocked():
        move()
    if right_is_clear():
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left()

def fill_hole():
    while front_is_clear():
        move()
        put_beeper()
    if front_is_blocked() and left_is_blocked():
        turn_around()
        while front_is_clear() and right_is_blocked():
            move()
        turn_right()
        move()
        
    
    
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/fix_road1.w')
