import pygame
import sys
from player import Player

class Game(object):

    def __init__(self):
        # config
        self.tps_max = 100.0

        # initialisation
        pygame.init()
        self.display_width = 1280
        self.display_height = 720
        self.size = (self.display_width, self.display_height)

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.light_gray = (210, 210, 210)
        self.gray = (180, 180, 180)

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Definitely Not A Square Game")
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.game_objects = []

        self.player = Player(self)
        self.player2 = Player(self)

        self.game_objects.append(self.player)
        self.game_objects.append(self.player2)

        self.player2.color = (25, 25, 255)
        self.player2.down_key = pygame.K_s
        self.player2.up_key = pygame.K_w
        self.player2.left_key = pygame.K_a
        self.player2.right_key = pygame.K_d

        self.start_menu()

    def tick(self):
        for game_object in self.game_objects:
            game_object.tick() 

    def draw(self):
        for game_object in self.game_objects:
            game_object.draw()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.white)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, x, y, size):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (x, y)
        self.screen.blit(TextSurf, TextRect)

    def button(self, c1, c2, x, y, width, height, message, font_size, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, c2, (x, y, width, height))

            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.screen, c1, (x, y, width, height))

        self.message_display(message, x + (width / 2), y + (height / 2), font_size)

    def start_menu(self):

        self.message_display("Definitely Not A Square Game",
                             (self.display_width / 2), (self.display_height / 4), 70)

        while True:

            self.button(self.gray, self.light_gray, self.display_width / 2.5, self.display_height / 3,
                        self.display_width / 8, self.display_height / 8, "Play", 30, self.game_loop)
            self.button(self.gray, self.light_gray, self.display_width / 2.5, self.display_height / 2,
                        self.display_width / 8, self.display_height / 8, "Quit", 30, sys.exit)

            # checks if user quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            pygame.display.update()

    def game_loop(self):
        while True:
            # checks if user quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # handles ticks
            # delta holds the time in seconds
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # drawing
            self.screen.fill(self.black)
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    Game()
