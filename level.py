import pygame
import character


class Level:

    def __init__(self, map_image, map_name, screen):
        self.map_image = pygame.image.load(map_image)
        self.map_name = map_name
        self.screen = screen
        self.characters = []
        self.enemies = []

    def add_character(self, char):
        self.characters.append(char)

    def add_enemies(self, enemy):
        self.enemies.append(enemy)

    def remove_enemies(self, enemy):
        self.enemies.remove(enemy)

    def draw_map(self):
        # Draw the Map
        self.screen.blit(self.map_image, (0, 0))
        # Draw the characters around the map
        for x in self.characters:
            x.get_frame()
            x.change_frame()
        for y in self.enemies:
            y.get_enemy_image(self.screen)

    def check_map_borders(self, top_left, bottom_right, player):
        # print(type(top_left), top_left)
        # print(type(bottom_right), bottom_right)
        # print(type(tuple(player.player_pos)), tuple(player.player_pos))
        if top_left <= tuple(player.player_pos) <= bottom_right:
            return True
        else:
            return False

    def map_change_frame(self):
        # Draw the characters around the map
        for x in self.characters:
            x.change_frame()
        for y in self.enemies:
            y.get_enemy_image(self.screen)


