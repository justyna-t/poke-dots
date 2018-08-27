# Poke the Dots V1
# This is a graphical game where two dots move around the screen, bouncing off
# the edges.


from uagame import Window
from pygame.time import Clock

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
    # while not player has selected close
        # play frame
            # handle events
            # draw game
            # update game
    pass


def handle_events():
    # for event in event list
        # handle one event
            # if event category equals close
                # remember player has selected close
    pass


def draw_game():
    # draw small dot
    # draw big dot
    # update display
    pass


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
