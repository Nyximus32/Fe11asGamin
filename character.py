import pygame


class Character:

    def __init__(self, idle_sheet, walk_sheet, player_pos, facing, screen, dt, stats):
        self.idle_sheet = pygame.image.load(idle_sheet)
        self.walk_sheet = pygame.image.load(walk_sheet)
        self.player_pos = player_pos
        self.player_state = "idle"
        self.frame_count = 2  # Total number of frames in the animation
        self.facing = facing  # which direction the character is walking in 1 is up 2 is left 3 is down 4 is up and 5
        # is stationary
        self.screen = screen
        self.frame_index = 0
        self.dt = dt
        self.xPos = 0
        self.yPos = 0
        self.stats = stats

    #  finds which frame to use based on
    def get_frame(self):
        frame = pygame.Surface((128, 128))
        if self.player_state == "idle":
            frame.blit(self.idle_sheet, (0, 0), ((self.frame_index * 128), (1 - self.facing) * -128, 128, 128))
        if self.player_state == "walk":
            frame.blit(self.walk_sheet, (0, 0), ((self.frame_index * 128), (1 - self.facing) * -128, 128, 128))
        frame.set_colorkey((0, 0, 0))
        self.screen.blit(frame, self.player_pos)

    def get_rect(self):
        return pygame.Rect(self.player_pos.x, self.player_pos.y, 128, 128)

    def get_stats(self):
        return self.stats

    def check_movement(self):
        keys = pygame.key.get_pressed()
        if pygame.key.get_pressed():
            self.player_state = "walk"
            self.frame_count = 8
            if keys[pygame.K_w]:
                self.player_pos.y -= 500 * self.dt
                self.facing = 1
            if keys[pygame.K_s]:
                self.player_pos.y += 500 * self.dt
                self.facing = 3
            if keys[pygame.K_a]:
                self.player_pos.x -= 500 * self.dt
                self.facing = 2
            if keys[pygame.K_d]:
                self.player_pos.x += 500 * self.dt
                self.facing = 4
        if not any(pygame.key.get_pressed()):
            self.player_state = "idle"
            self.frame_count = 2

    def change_frame(self):
        self.frame_index = (self.frame_index + 1) % self.frame_count  # Loop through frames


class CharacterStats:
    def __init__(self, name, hp, damage, role):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.is_turn_over = False
        self.role = role

    def get_turn_over(self):
        return self.is_turn_over

    def set_turn_over(self, turn_over):
        self.is_turn_over = turn_over

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return "{} took {} damage".format(self.name, damage)

    def get_role(self):
        return self.role


class Jadyn(Character):
    def __init__(self, player_pos, facing, screen, dt):
        super().__init__(idle_sheet="Jadyn/Jadyn_idle.png", walk_sheet="Jadyn/Jadyn_walk.png",
                         player_pos=player_pos, facing=facing, screen=screen, dt=dt,
                         stats=CharacterStats(name="Jadyn", hp=130, damage=15,
                                              role="fighter"))


class Teo(Character):
    def __init__(self, player_pos, facing, screen, dt):
        super().__init__(idle_sheet="Teo/Teo_idle.png", walk_sheet="Teo/Teo_walk.png",
                         player_pos=player_pos, facing=facing, screen=screen, dt=dt,
                         stats=CharacterStats(name="Teo", hp=100, damage=20,
                                              role="fighter"))

class Rob(Character):
    def __init__(self, player_pos, facing, screen, dt):
        super().__init__(idle_sheet="Rob/Rob_idle.png", walk_sheet="Rob/Rob_walk.png",
                         player_pos=player_pos, facing=facing, screen=screen, dt=dt,
                         stats=CharacterStats(name="Robert", hp=110, damage=15,
                                              role="fighter"))

class Jaafar(Character):
    def __init__(self, player_pos, facing, screen, dt):
        super().__init__(idle_sheet="Jaafar/Jaafar_idle.png", walk_sheet="Jaafar/Jaafar_walk.png",
                         player_pos=player_pos, facing=facing, screen=screen, dt=dt,
                         stats=CharacterStats(name="Jaafar", hp=80, damage=35,
                                              role="Assassin"))