# Poke the Dots V1
# This is a graphical game where two dots move around the screen, bouncing off
# the edges.


from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle


def main():
    window = create_window()
    # create game
    clock = Clock()
    small_color = "red"
    small_center = [50, 100]
    small_radius = 30
    small_velocity = [1, 2]
    small_dot = [small_color, small_center, small_radius, small_velocity]
    big_color = "blue"
    big_center = [200, 100]
    big_radius = 40
    big_velocity = [2, 1]
    play_game(window, small_dot, big_color, big_center, big_radius, big_velocity, clock)
    window.close()


def create_window():
    window = Window("Poke the Dots", 500, 400)
    window.set_bg_color("black")
    return window


def play_game(window, small_dot, big_color, big_center, big_radius, big_velocity, clock):
    close_selected = False
    while not close_selected:
        # play frame
        #    handle events
        close_selected = handle_events()

        #   draw game
        draw_game(window, small_dot, big_color, big_center, big_radius)
        #   update game
        update_game(window, small_dot, big_center, big_radius, big_velocity, clock)


def handle_events():
    closed = False
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            closed = True
    return closed


def draw_game(window, small_dot, big_color, big_center, big_radius):
    window.clear()
    # draw small dot
    draw_dot(window, small_dot[0], small_dot[1], small_dot[2])

    # draw big dot
    draw_dot(window, big_color, big_center, big_radius)

    # update display
    window.update()


def draw_dot(window, color_string, center, radius):
    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)


def update_game(window, small_dot, big_center, big_radius, big_velocity, clock):
    frame_rate = 90
    # move small dot
    move_dot(window, small_dot[1], small_dot[2], small_dot[3])
    # move big dot
    move_dot(window, big_center, big_radius, big_velocity)
    # control frame rate
    clock.tick(frame_rate)


def move_dot(window, center, radius, velocity):
    size = [window.get_width(), window.get_height()]
    for index in range(2):
        # update center at index
        center[index] += velocity[index]
        if center[index] + radius >= size[index] or\
           center[index] - radius <= 0:
            velocity[index] = -velocity[index]


main()
