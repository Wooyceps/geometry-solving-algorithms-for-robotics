import math


def interpolate_turns(ang, line, base_axis='x'):
    steps = 360 // ang
    x, y = 0, 0
    for i in range(1, steps+1):
        angle = math.radians(ang * i)
        if base_axis == 'x':
            x += math.cos(angle) * line
            y += math.sin(angle) * line
        else:
            x += math.sin(angle) * line
            y += math.cos(angle) * line

        if ang*i in [90, 180, 270, 360]:
            print(f"ANGLE = {ang*i}")
            print(f"x = {round(x,4)}, y = {round(y,4)}")


interpolate_turns(1, 3, 'y')