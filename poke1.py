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
    small_color = "blue"
    small_radius = 30
    small_center = [50, 100]
    small_velocity = [1, 2]
    big_color = "blue"
    big_radius = 40
    big_center = [200, 100]
    big_velocity = [2, 1]
    play_game()
    window.close()


def create_window():
    window = Window("Poke the Dots", 500, 400)
    window.set_bg_color("black")
    return window


def play_game():
    close_selected = False
    while not close_selected:
        # play frame
        #    handle events
        close_selected = handle_events()

        #   draw game
        #   update game


def handle_events():
    closed = False
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            closed = True
    return closed


def draw_game():
    # draw small dot
    # draw big dot
    # update display
    pass


def draw_dot(window, color_string, center, radius):
    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)


def update_game():
    # move small dot
    # move big dot
    # control frame rate
    pass


def move_dot():
    # for index in sequence o to 1
        # update center at index
            # add velocity at index to center at index
            # if dot edge outside window
                # negate velocity at index
    pass


main()
