import random
import math
import numpy as np
import pygame

# Number of vertices
n_vertices = 3

# Setting
size = width, height = 600, 600  # window size
col_vertex = (255, 0, 0)  # color vertices
col_points = (255, 255, 255)  # color points
col_back = (0, 0, 0)  # background color
time_int = 1  # interval between screen update (in ms)


class Shape:
    def __init__(self, w, h, n):
        # w: screen width
        # h: screen height
        # n: number of vertices
        self.points = n
        delta_angle = 360 / n
        r = (w / 2) - 10
        v = np.arange(0, n)
        angles = (180 + v * delta_angle) * math.pi / 180
        angle_sin = np.sin(angles)
        angle_cos = np.cos(angles)
        self.x = ((w / 2) + (r * angle_sin)).astype(int)
        self.y = ((h / 2) + (r * angle_cos)).astype(int)


# Define a Shape object
shape = Shape(width, height, n_vertices)

# Define how far a point jumps in the direction of the selected vertex
b = shape.points / (shape.points + 3)


# define a main function
def main(s):

    # initialize the pygame module
    pygame.init()

    # initialize clock object
    clock = pygame.time.Clock()

    # create a surface on screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(f"Chaos game - Numberphile")

    # Background color
    screen.fill(col_back)

    # Draw the vertices
    for i in range(s.points):
        pygame.draw.circle(screen, col_vertex, (s.x[i], s.y[i]), 1)
    pygame.display.update()

    # Draw random starting point
    px = random.randint(int(width * 0.25), int(width * 0.75))
    py = random.randint(int(height * 0.25), int(height * 0.75))
    screen.set_at((px, py), col_points)
    pygame.display.update()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        # Select one of the vertices
        v = random.randint(0, s.points - 1)
        to_x = s.x[v]
        to_y = s.y[v]

        # Calculate the point between the selected vertex and the current point
        px = int(px + ((to_x - px) * b))
        py = int(py + ((to_y - py) * b))
        screen.set_at((px, py), col_points)

        pygame.display.update()

        # Wait
        clock.tick(int(1000/time_int))


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main(shape)
