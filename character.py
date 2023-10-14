import pygame


class Character:

    def __init__(self, idle_sheet, walk_sheet, player_pos, facing, screen, dt):
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

    #  finds which frame to use based on
    def get_frame(self):
        frame = pygame.Surface((128, 128))
        if self.player_state == "idle":
            frame.blit(self.idle_sheet, (0, 0), ((self.frame_index * 128), (1 - self.facing) * -128, 128, 128))
        if self.player_state == "walk":
            frame.blit(self.walk_sheet, (0, 0), ((self.frame_index * 128), (1 - self.facing) * -128, 128, 128))
        frame.set_colorkey((0, 0, 0))
        self.screen.blit(frame, self.player_pos)

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

