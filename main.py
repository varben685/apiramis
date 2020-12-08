import pygame
import menu

def main():
    pygame.init()

    #Ablak létrehozása
    ablak = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("A piramis")
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    ablak.fill((23, 53, 128))

    #Menü
    menu.main_menu(ablak)


main()