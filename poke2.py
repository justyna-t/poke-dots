# Poke the Dots V2
# This is a graphical game where two dots move around the screen, bouncing off
# the edges.


from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle


def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()


def create_window():
    # Create a window for the game, open it, and return it.
    window = Window("Poke the Dots", 500, 400)
    window.set_bg_color("black")
    return window


def create_game(window):
    #  Create a Game object for Poke the Dots
    game = Game()
    game.window = window
    game.frame_rate = 90 # larger is faster game
    game.close_selected = False
    game.clock = Clock()
    game.small_dot = create_dot("red", [50, 100], 30, [1, 2])
    game.big_dot = create_dot("blue", [200, 100], 40, [2, 1])
    return game


def create_dot(color, center, radius, velocity):
    dot = Dot()
    dot.color = color
    dot.center = center
    dot.radius = radius
    dot.velocity = velocity
    return dot


def play_game(game):
    # Play the game until the player presses the close icon.
    # - game is the Game to play
    while not game.close_selected:
        # play frame
        #    handle events
        handle_events(game)
        #   draw game
        draw_game(game)
        #   update game
        update_game(game)


def handle_events(game):
    # Handle the current game events. Return True if the player clicked the
    # close icon and False otherwise.
    # - game is the Game whose events should be handled
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            game.close_selected = True


def draw_game(game):
    # Draw all game objects.
    # - game
    game.window.clear()
    # draw small dot
    draw_dot(game.window, game.small_dot)

    # draw big dot
    draw_dot(game.window, game.big_dot)

    # update display
    game.window.update()


def draw_dot(window, dot):
    # Draw the dot on the window.
    # - window
    # - dot is the Dot to be drawn
    surface = window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)


def update_game(game):
    # Update all game objects with state changes that are not due to
    # user events.
    # - game

    # move small dot
    move_dot(game.window, game.small_dot)
    # move big dot
    move_dot(game.window, game.big_dot)
    # control frame rate
    game.clock.tick(game.frame_rate)


def move_dot(window, dot):
    # Change the location and the velocity of the dot so it remains on the
    # surface by bouncing from its edges.
    # - window
    # - dot is the Dot to be moved
    size = [window.get_width(), window.get_height()]
    for index in range(2):
        # update center at coordinate
        dot.center[index] += dot.velocity[index]
        # dot edge outside window?
        if dot.center[index] + dot.radius >= size[index] or\
           dot.center[index] - dot.radius <= 0:
            # change direction
            dot.velocity[index] = -dot.velocity[index]


class Game:
    # An object in this class represents a complete game
    # - window is the Window to play in
    # - frame_rate
    # - close_selected
    # - clock is a Clock used to control game speed
    # - small_dot
    # - big_dot
    pass


class Dot:
    # An object in this class represents a dot
    # - color is the str color of the dot
    # - center is the list of x int and y int coordinates of the center of
    # the dot
    # - radius is the int radius of the dot
    # - velocity is the list of horizontal int and vertical int speeds of
    # the dot
    pass


main()
