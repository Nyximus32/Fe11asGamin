import pygame
import sys

# Initialisatie van Pygame
pygame.init()

# Schermgrootte en kleuren
scherm_breedte = 1287
scherm_hoogte = 726
achtergrond_kleur = (255, 255, 255)
tekst_kleur = (255, 0, 0)

# Maak het scherm
scherm = pygame.display.set_mode((scherm_breedte, scherm_hoogte))
pygame.display.set_caption("Meat 'Em Up")

# Laad een achtergrondafbeelding (optioneel)
achtergrond = pygame.image.load("Imgs/jadyn.png")

# Functie om tekst weer te geven
def toon_tekst(tekst, x, y, lettergrootte, kleur, schaduw=True):
    lettertype = pygame.font.SysFont("ComicSans", 32)
    tekstoppervlak = lettertype.render(tekst, True, kleur)
    tekstrechthoek = tekstoppervlak.get_rect()
    tekstrechthoek.center = (x, y)
    if schaduw:
        tekst_achtergrond = lettertype.render(tekst, True, achtergrond_kleur)
        schaduw_rect = tekst_achtergrond.get_rect()
        schaduw_rect.center = (x + 4, y + 4)  # Voeg een schaduw toe
        scherm.blit(tekst_achtergrond, schaduw_rect)
    scherm.blit(tekstoppervlak, tekstrechthoek)

# Set the new dimensions
new_width = 1287
new_height = 726

# Resize the image
resized_image = pygame.transform.scale(achtergrond, (new_width, new_height))

# Inialiseer de mixer (geluid)
pygame.mixer.init()

# Laad en speel de achtergrondmuziek
pygame.mixer.music.load("Sounds/terrorsquad.mp3")  # Vervang "background_music.mp3" met je audiobestand
pygame.mixer.music.set_volume(10)  # Pas het volume aan indien nodig
pygame.mixer.music.play(-1)  # De '-1' betekent oneindig spelen

# De gameloop
lopend = True
while lopend:
    for gebeurtenis in pygame.event.get():
        if gebeurtenis.type == pygame.QUIT:
            lopend = False
        if gebeurtenis.type == pygame.KEYDOWN:
            if gebeurtenis.key == pygame.K_SPACE:
                # Start het spel wanneer de spatiebalk wordt ingedrukt
                lopend = False  # Verlaat de gameloop

    # Teken de achtergrondafbeelding (optioneel)
    scherm.blit(resized_image, (0, 0))

    # Toon de titel van het spel
    toon_tekst("Meat 'Em Up", scherm_breedte // 2, scherm_hoogte // 3, None, 64)

    # Toon instructies om het spel te starten
    toon_tekst("Druk op de spatiebalk om te beginnen", scherm_breedte // 2, scherm_hoogte // 2, None, 32)

    pygame.display.flip()

# Beëindig Pygame
pygame.quit()

# Sluit het Python-script
sys.exit()
