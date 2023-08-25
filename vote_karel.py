from stanfordkarel import *

def main():
    put_beeper()
    while front_is_clear():
        jump_across()
        put_beeper()
    turn_right()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        jump_across()
        put_beeper()

def jump_across():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/5x5.w')
