import pygame
import character
import level
import enemy

pygame.init()

frame_rate = 20  # Frames per second
screen = pygame.display.set_mode((1287, 726))  # display size and resolution

running = True
clock = pygame.time.Clock()
dt = clock.tick(60) / 1000
in_battle = False
dmg_taken = True

# Map and Level Class
Map = level.Level("Maps/Hall.png", screen)
BattleMap = level.Level("Maps/JadynHands.png", screen)

# Character Classes
# Jadyn = character.Character(
#     "Jadyn/Jadyn_idle.png", "Jadyn/Jadyn_walk.png", pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 3,
#     screen, dt, character.CharacterStats(name="Jadyn", hp=100, damage=20,
#                                          role="fighter")
# )
Jadyn = character.Jadyn(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 3, screen, dt)
# Teo = character.Character(
#     "Teo/Teo_idle.png", "Teo/Teo_walk.png", (600, 450),
#     2, screen, dt, character.CharacterStats(name="Teo", hp=100, damage=20,
#                                             role="fighter")
# )
Teo = character.Teo(pygame.Vector2(600, 450), 2, screen, dt)

dragon1 = enemy.Dragon(700, 0)
dragon2 = enemy.Dragon(100, 100)
dragon3 = enemy.Dragon(360, 70)
dragons = [dragon2, dragon3]

Map.add_character(Teo)
Map.add_enemies(dragon1)


def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


def quit_game():
    global in_battle
    global Map
    in_battle = False
    Map = level.Level("Maps/Hall.png", screen)
    Map.add_character(Teo)
    Map.add_enemies(dragon1)




def do_dmg():
    global dmg_taken
    dmg_taken = False


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not dmg_taken:
            for dragon in dragons:
                if dragon.get_rect().collidepoint(pygame.mouse.get_pos()):
                    dragon.take_damage(Jadyn.get_stats().damage)
                    dmg_taken = True
                    Jadyn.get_stats().set_turn_over(True)
                    if not dragon.is_alive():
                        dragons.remove(dragon)
                        BattleMap.remove_enemies(dragon)
                        Jadyn.get_stats().set_turn_over(False)
                        dmg_taken = True
                        print("Dragon is dead")
                    else:
                        dragon.set_turn_over(False)

        if Jadyn.get_rect().colliderect(dragon1.get_rect()) and Map is not BattleMap:
            Map = BattleMap
            Map.add_character(Jadyn)
            Map.add_enemies(dragon2)
            Map.add_enemies(dragon3)
            Jadyn.player_pos = pygame.Vector2(1080, 150)
            Jadyn.facing = 2
            Jadyn.player_state = "idle"
            Jadyn.frame_count = 2
            in_battle = True

    if len(dragons) == 0:
        in_battle = False
        Map = level.Level("Maps/Hall.png", screen)
        Map.add_character(Teo)

    # Input Checks
    if not in_battle:
        Jadyn.check_movement()  # Check character movement

    # Background color
    Map.draw_map()

    # Logic
    Jadyn.get_frame()

    if in_battle:
        for dragon in dragons:
            if dragon.is_alive():
                original_x, original_y = dragon.get_position()
                dragon.draw_hp_bar(original_x + 80, original_y + 270, dragon.hp, 100, screen)
        button("Attack!", 550, 450, 100, 50, "blue", "black", do_dmg)
        button("Quit", 550, 550, 100, 50, "red", "white", quit_game)

    # Draw
    pygame.display.flip()

    Jadyn.change_frame()
    Map.map_change_frame()

    clock.tick(frame_rate)


