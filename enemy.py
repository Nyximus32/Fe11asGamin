import pygame


class EnemyPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class EnemyStats:
    def __init__(self, name, hp, damage, enemy_position, image):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.enemy_position = enemy_position
        self.is_turn_over = False
        self.is_on_field = False
        self.image = image

    def get_position(self):
        return self.enemy_position.x, self.enemy_position.y

    def set_position(self, x, y):
        self.enemy_position.x = x
        self.enemy_position.y = y

    def get_turn_over(self):
        return self.is_turn_over

    def set_turn_over(self, turn_over):
        self.is_turn_over = turn_over

    def get_if_on_field(self):
        return self.is_on_field

    def set_if_on_field(self, on_field):
        self.is_on_field = on_field

    def get_rect(self):
        return pygame.Rect(self.enemy_position.x, self.enemy_position.y, 256, 256)

    def get_enemy_image(self, game_display):
        if self.hp <= 20:
            color = (255, 0, 0)
        elif self.hp <= 50:
            color = (255, 255, 0)
        else:
            color = (0, 255, 0)
        image = pygame.image.load(self.image)
        game_display.blit(image, (self.enemy_position.x, self.enemy_position.y))
        # pygame.draw.rect(game_display, color, (self.enemy_position.x, self.enemy_position.y, 32, 32))
        return game_display

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self, target):
        target.take_damage(self.damage)

    def draw_hp_bar(self, x, y, hp, max_hp, screen):
        hp_bar_width = 100
        hp_bar_height = 20

        pygame.draw.rect(screen, (255, 0, 0), (x, y, hp_bar_width, hp_bar_height))  # Draw the red background
        current_hp_width = (hp / max_hp) * hp_bar_width
        pygame.draw.rect(screen, (0, 255, 0), (x, y, current_hp_width, hp_bar_height))  # Draw the green HP bar

    def __str__(self):
        return "{} has {} hit points remaining.".format(self.name, self.hp)


class Goblin(EnemyStats):
    def __init__(self):
        super().__init__(name="Goblin", hp=50, damage=2, enemy_position=EnemyPosition(20, 120), image='goblin.png')


class Slime(EnemyStats):
    def __init__(self):
        super().__init__(name="Slime", hp=20, damage=5, enemy_position=EnemyPosition(20, 70), image='slime.png')


class Dragon(EnemyStats):
    def __init__(self, x: int = 10, y: int = 10):
        super().__init__(name="Dragon", hp=100, damage=10, enemy_position=EnemyPosition(x, y), image='Imgs/dragon.gif')
