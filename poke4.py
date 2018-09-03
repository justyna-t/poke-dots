# Poke the Dots V4
# This is a graphical game where two dots move around the screen, bouncing
# off the edges. The user tries to prevent the dots from colliding by
# pressing and releasing the mouse button to teleport the dots to a random
# location. The score is the number of seconds from the start of the game.

from uagame import Window
from random import randint
from time import sleep
from pygame import QUIT, MOUSEBUTTONUP, Color
from pygame.time import get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

# User-defined functions


def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()


def create_window():
    # Create a Window for the game, open it, and return it.

    window = Window("Poke the Dots", 500, 400)
    window.set_font_name('ariel')
    window.set_font_size(64)
    window.set_font_color('white')
    window.set_bg_color("black")
    return window


def create_game(window):
    # Create a Game object for Poke the Dots.
    # - window is the Window that the game is played in

    game = Game()
    game.window = window
    game.frame_rate = 90  # larger is faster game
    game.close_selected = False
    game.small_dot = Dot("red", [50, 100], 30, [1, 2])
    game.big_dot = Dot("blue", [200, 100], 40, [2, 1])
    game.small_dot.randomize(game.window)
    game.big_dot.randomize(game.window)
    game.score = 0
    return game


def play_game(game):
    # Play the game until the player presses the close icon.
    # - game is the Game to play

    while not game.close_selected:
        # play frame
        handle_events(game)
        draw_game(game)
        update_game(game)


def handle_events(game):
    # Handle the current game events by changing the game state appropriately.
    # - game is the Game whose events will be handled
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            game.small_dot.randomize(game.window)
            game.big_dot.randomize(game.window)


def draw_game(game):
    # Draw all game objects.
    # - game is the Game to draw for

    game.window.clear()
    draw_score(game)
    game.small_dot.draw(game.window)
    game.big_dot.draw(game.window)
    game.window.update()


def draw_score(game):
    # Draw scoreboard until the player presses the close icon.
    # - game is the Game to draw for

    score_string = "Score: %d" % game.score
    game.window.draw_string(score_string, 0, 0)


def update_game(game):
    # Update all game objects with state changes that are not due to
    # user events.
    # - game is the Game to update

    game.small_dot.move(game.window)
    game.big_dot.move(game.window)
    # control frame rate
    sleep(0.01)
    game.score = get_ticks() / 1000  # turn milisecods to seconds


class Game:
    # An object in this class represents a complete game.
    # - window
    # - frame_rate
    # - close_selected
    # - small_dot
    # - big_dot
    # - score
    pass


class Dot:
    # An object in this class represents a colored circle that can move.

    def __init__(self, color, center, radius, velocity):
        # - color is the str color of the dot
        # - center is a list containing the x and y int coords of the center
        # of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is the list of horizontal int and vertical int speeds of
        # the dot

        self.color = color
        self.center = center
        self.radius = radius
        self.velocity = velocity

    def move(self, window):
        # Change the location and the velocity of the Dot so it remains on the
        # surface by bouncing from its edges.
        # - window is the Window that the game is played in

        size = [window.get_width(), window.get_height()]
        for index in range(2):
            # update center at coordinate
            self.center[index] += self.velocity[index]
            # dot edge outside window?
            if self.center[index] + self.radius >= size[index] or\
               self.center[index] - self.radius <= 0:
                # change direction
                self.velocity[index] = -self.velocity[index]

    def draw(self, window):
        # Draw the Dot on the window.
        # - window is the Window that the game is played in

        surface = window.get_surface()
        color = Color(self.color)
        draw_circle(surface, color, self.center, self.radius)

    def randomize(self, window):
        # Randomize the x and y int coords of the center of the Dot.
        # Ensure that no part of a dot extends beyond the surface boundary.
        # - window is the Window that the game is played in

        size = [window.get_width(), window.get_height()]
        for index in range(2):
            self.center[index] = randint(self.radius,
                                         size[index] - self.radius)


main()
