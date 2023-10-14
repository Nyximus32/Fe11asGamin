import pygame
import character


class Level:

    def __init__(self, map_image, screen):
        self.map_image = pygame.image.load(map_image)
        self.screen = screen
        self.characters = []

    def add_character(self, char):
        self.characters.append(char)

    def draw_map(self):
        # Draw the Map
        self.screen.blit(self.map_image, (0, 0))
        # Draw the characters around the map
        for x in self.characters:
            x.get_frame()
            x.change_frame()

    def map_change_frame(self):
        # Draw the characters around the map
        for x in self.characters:
            x.change_frame()

