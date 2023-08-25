from stanfordkarel import *

def main():
        put_beeper()
        put_beeper_odd()
        if front_is_clear():
             turn_left()
        while front_is_clear() and left_is_blocked():
            move()
            turn_right()
            put_beeper_even()
        if front_is_clear():
             turn_left()
             move()
             turn_right()
        put_beeper()
        put_beeper_odd()
        if front_is_clear():
             turn_left()
        while front_is_clear() and left_is_blocked():
            move()
            turn_right()
            put_beeper_even()
        if front_is_clear():
             turn_left()
             move()
             turn_right()
        put_beeper()
        put_beeper_odd()
        if front_is_clear():
             turn_left()
        while front_is_clear() and left_is_blocked():
            move()
            turn_right()
            put_beeper_even()
        if front_is_clear():
             turn_left()
             move()
             turn_right()
        put_beeper()
        put_beeper_odd()
        if front_is_clear():
             turn_left()
             if front_is_clear() and left_is_blocked():
                move()
                turn_right()
                put_beeper_even()
                 
        # if front_is_clear() :
        #     turn_left()
        #     move()
        #     turn_right()
        #     put_beeper()
        #     put_beeper_odd()
        #     turn_left()
        #     while front_is_clear() and left_is_blocked():
        #         move()
        #         turn_right()
        #         put_beeper_even()
        # if front_is_clear() :
        #     turn_left()
        #     move()
        #     turn_right()
        #     put_beeper()
        #     put_beeper_odd()
        #     turn_left()
        #     while front_is_clear() and left_is_blocked():
        #         move()
        #         turn_right()
        #         put_beeper_even()
        
            
    
    # while front_is_clear():
    #     move()
    #     if front_is_clear():
    #         move()
    #         put_beeper()
    # if front_is_blocked():
    #         go_back()

def put_beeper_odd():
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    if front_is_blocked():
            go_back()

def put_beeper_even():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    if front_is_blocked():
            go_back()

def go_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

    
    
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/5x5.w')
