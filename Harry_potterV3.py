def wall():
    while not can_move():
            turn_right()
            if can_move():
                move()
                turn_left()
            else:
                while not can_move():
                    turn_right()
                    turn_right()
                    move()
                    turn_right()
    move()


while not is_on_target():
    
    if get_x() < get_target_x():
        while get_direction() != EAST:
            turn_right()
        if can_move() and not in_front_of_the_enemy():
            move()
        else:
            wall
    elif get_x() > get_target_x():
        while get_direction() != WEST:
            turn_right()
        if can_move() and not in_front_of_the_enemy():
            move()
        else:
            wall

    if get_y() < get_target_y():
        while get_direction() != SOUTH:
            turn_right()
        if can_move() and not in_front_of_the_enemy():
            move()
        else:
            wall
    elif get_y() > get_target_y():
        while get_direction() != NORTH:
            turn_right()
        if can_move() and not in_front_of_the_enemy():
            move()
        else:
            wall

destroy_target()