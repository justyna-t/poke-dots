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
    game = create_game()
    game.play()


def create_game():
    # Create a Game object for Poke the Dots and return it.
    frame_rate = 90  # larger is faster game
    close_selected = False
    score = 0
    game = Game(frame_rate, close_selected, score)
    return game


class Game:
    # An object in this class represents a complete game.
    def __init__(self, frame_rate, close_selected, score):
        self.frame_rate = frame_rate
        self.close_selected = close_selected
        self.score = score

        # create window
        self.window = Window("Poke the Dots", 500, 400)
        self.window.set_font_name('ariel')
        self.window.set_font_size(64)
        self.window.set_font_color('white')
        self.window.set_bg_color("black")

        # create dots
        self.small_dot = Dot("red", [50, 100], 30, [1, 2])
        self.big_dot = Dot("blue", [200, 100], 40, [2, 1])

        # randomize dots
        self.small_dot.randomize(self.window)
        self.big_dot.randomize(self.window)

    def play(self):
        # Play the game until the player presses the close icon.

        while not self.close_selected:
            # play frame
            self.handle_events()
            self.draw()
            self.update()
        else:
            self.window.close()

    def handle_events(self):
        # Handle the current game events by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled

        event_list = get_events()
        for event in event_list:
            self.handle_one_event(event)

    def handle_one_event(self, event):
        # Handle one event by changing the game state appropriately.
        # - self is the Game whose event will be handled
        # - event is the Event object to handle

        if event.type == QUIT:
            self.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            self.handle_mouse_up()

    def handle_mouse_up(self):
        # Respond to the player releasing the mouse button by taking
        # appropriate actions.
        # - self is the Game where the mouse up occurred
        self.small_dot.randomize(self.window)
        self.big_dot.randomize(self.window)

    def draw(self):
        # Draw all game objects.

        self.window.clear()
        self.draw_score()
        self.small_dot.draw(self.window)
        self.big_dot.draw(self.window)
        self.window.update()

    def draw_score(self):
        # Draw scoreboard until the player presses the close icon.

        score_string = "Score: %d" % self.score
        self.window.draw_string(score_string, 0, 0)

    def update(self):
        # Update all game objects with state changes that are not due to
        # user events.

        self.small_dot.move(self.window)
        self.big_dot.move(self.window)
        # control frame rate
        sleep(0.01)
        self.score = get_ticks() / 1000  # turn milisecods to seconds


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