import math

# This function interpolates turns based on the given angle and line length.
# It calculates the x and y coordinates for each step of the turn and prints them when the angle is a multiple of 90.
# The base axis for the turn can be specified ('x' or 'y').
#
# Parameters:
# ang (int): The angle in degrees for each step of the turn.
# line (int): The length of the line for each step of the turn.
# base_axis (str): The base axis for the turn ('x' or 'y'). Default is 'x'.


def interpolate_turns(ang, line, base_axis='x'):
    # Calculate the number of steps for the turn
    steps = 360 // ang
    x, y = 0, 0
    # Loop over each step of the turn
    for i in range(1, steps+1):
        # Calculate the angle in radians for the current step
        angle = math.radians(ang * i)
        # Update the x and y coordinates based on the base axis and the current angle and line length
        if base_axis == 'x':
            x += math.cos(angle) * line
            y += math.sin(angle) * line
        else:
            x += math.sin(angle) * line
            y += math.cos(angle) * line
        # If the current angle is a multiple of 90, print the x and y coordinates
        if ang*i in [90, 180, 270, 360]:
            print(f"ANGLE = {ang*i}")
            print(f"x = {round(x,4)}, y = {round(y,4)}")


# Call the function with an angle of 1 degree, a line length of 3, and 'y' as the base axis
interpolate_turns(1, 3, 'y')