import pygame
import character
import level

pygame.init()

frame_rate = 20  # Frames per second
screen = pygame.display.set_mode((1287, 726))  # display size and resolution

running = True
clock = pygame.time.Clock()
dt = clock.tick(60) / 1000

# Map and Level Class
Map = level.Level("Maps/Hall.png", screen)

# Character Classes
Jadyn = character.Character(
    "Jadyn/Jadyn_idle.png", "Jadyn/Jadyn_walk.png", pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 3,
    screen, dt
)
Teo = character.Character(
    "Teo/Teo_idle.png", "Teo/Teo_walk.png", (600, 450),
    2, screen, dt
)

Map.add_character(Teo)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input Checks
    Jadyn.check_movement()  # Check character movement

    # Background color
    Map.draw_map()

    # Logic
    Jadyn.get_frame()

    # Draw
    pygame.display.flip()

    Jadyn.change_frame()
    Map.map_change_frame()

    clock.tick(frame_rate)