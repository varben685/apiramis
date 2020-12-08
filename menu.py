import pygame
import tkinter as tk
from tkinter import messagebox
import fajlkezeles
import jatekvezerles

#Szövegek kiírása, ezek jelennek meg a játékban
def szoveg_kiiras(betutipus,meret,szoveg,szin):
    betutipus = pygame.font.SysFont(betutipus,meret)
    szin = pygame.Color(szin)
    szoveg = betutipus.render(szoveg,True,szin)
    return szoveg

#Kilépés a játékból, megkérdezi hogy biztos ki akarsz e lépni
def kilepes():
    ablak = tk.Tk()
    ablak.withdraw()
    box = messagebox.askquestion('Játék bezárása',"Biztosan kiszeretnél lépni a játékból? ")
    if box == 'yes':
        pygame.quit()
        exit()

#Ranglistában szereplő helyezések sorszámának kiírása
def ranglista_sorszamok_kiirasa(ablak):
    k = 0
    for i in range(1, 11):
        # 1 helyezés kiírása arannyal
        if i == 1:
            ablak.blit(szoveg_kiiras("Constatia", 45, "1.", "gold"), (280, 260))

        # 2. helyezés kiírása ezüsttel
        elif i == 2:
            ablak.blit(szoveg_kiiras("Constatia", 45, "2.", "grey"), (280, 260 + k))

        # 3.helyezés kiírása bronzzal
        elif i == 3:
            ablak.blit(szoveg_kiiras("Constatia", 45, "3.", "orange4"), (280, 260 + k))

        # 10.helyezés kiírása picikét arébb csusztatva
        elif i == 10:
            ablak.blit(szoveg_kiiras("Constatia", 45, str(i) + ".", "white"), (272, 260 + k))

        # Összes többi kiírása
        else:
            ablak.blit(szoveg_kiiras("Constatia", 45, str(i) + ".", "white"), (280, 260 + k))
        k += 45

#Ranglistában szereplő nevek,összegek,nehézségek kiírása
def ranglista_helyezesek_kiirasa(ablak):
    lista = fajlkezeles.ranglista_beolvas()
    k = 0
    db = 0
    for i in lista:
        ablak.blit(szoveg_kiiras("Constantia", 32, i.nev, "white"), (500, 260 + k))
        ablak.blit(szoveg_kiiras("Constantia", 32, i.nehezseg, "white"), (700, 260 + k))
        ablak.blit(szoveg_kiiras("Constantia", 32, str(i.osszeg), "white"), (1000, 260 + k))
        k += 45
        db += 1
        if db >= 10:
            break

#Ranglista menű kiírása
def ranglista(ablak):
    #Visszanyíl logo
    visszanyil = pygame.image.load("vissza.png")

    while True:
        #Ablak tisztázása
        ablak.fill((23, 53, 128))

        click = False
        eger = pygame.mouse.get_pos()

        #Visszalépés gomb megjelenítése
        visszalepesgomb = pygame.Rect(150, 85, 95, 80)
        pygame.draw.rect(ablak, (23, 53, 128), visszalepesgomb)
        ablak.blit(visszanyil,(150,85))

        #Cím szöveg kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 100, "Ranglista", "white"), (450, 60))

        #Helyezés fejléc kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 40, "Helyezés", "white"), (230, 200))

        #Helyezés sorszámok kiírása
        ranglista_sorszamok_kiirasa(ablak)

        #Név fejléc kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 40, "Név", "white"), (500, 200))

        #Nehézség fejléc kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 40, "Nehézség", "white"), (700, 200))

        #Összeg fejléc kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 40, "Összeg", "white"), (1000, 200))

        #Ranglista elemek kiírása
        ranglista_helyezesek_kiirasa(ablak)

        #Eventek kezelése
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        #Visszalépés gomb megnyomása
        if visszalepesgomb.collidepoint(eger):
            if click == True:
                break

        pygame.display.update()

#Játékos név megadása
def jatekos_nev_megadasa(ablak):
    # Visszanyíl logo
    visszanyil = pygame.image.load("vissza.png")

    jatekosnev =""
    jatekosnev_doboz = pygame.Rect(450,300,400,50)
    aktiv = False
    while True:
        # Ablak tisztázása
        ablak.fill((23, 53, 128))

        # Visszalépés gomb megjelenítése
        visszalepesgomb = pygame.Rect(150, 85, 95, 80)
        pygame.draw.rect(ablak, (23, 53, 128), visszalepesgomb)
        ablak.blit(visszanyil, (150, 85))

        click = False
        eger = pygame.mouse.get_pos()

        #Cím szöveg kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 70, "Add meg milyen névvel", "white"), (350, 80))
        ablak.blit(szoveg_kiiras("Gill Sans", 70, "szeretnél játszani", "white"), (400, 150))

        #Indítás szöveg kiírása
        inditasgomb = pygame.Rect(850, 470, 140, 40)
        if jatekosnev!="":
            pygame.draw.rect(ablak, (23, 53, 128), inditasgomb)
            ablak.blit(szoveg_kiiras("Constatia", 64, "Indítás", "white"), (850, 470))

        #Eventek kezelése
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.KEYDOWN:
                if aktiv == True:

                    #Max csak 15 karakter hosszú lehet a név ha több akkor csak törölni lehet
                    #Minden karakter engedélyezett kivéve a space,enter és a tab
                    if len(jatekosnev)<15:
                        if event.key == pygame.K_BACKSPACE:
                            jatekosnev=jatekosnev[:-1]
                            pass
                        elif event.key == pygame.K_TAB:
                            pass
                        elif event.key == pygame.K_SPACE:
                            pass
                        elif event.key == pygame.K_RETURN:
                            pass
                        else:
                            jatekosnev+= event.unicode
                    else:
                        if event.key == pygame.K_BACKSPACE:
                            jatekosnev=jatekosnev[:-1]
                            continue

        #Játékos név megadása beviteli mező
        if aktiv == False:
            pygame.draw.rect(ablak, (23, 53, 100), jatekosnev_doboz)
        else:
            pygame.draw.rect(ablak, (23, 53, 85), jatekosnev_doboz)
        ablak.blit(szoveg_kiiras("Constatia", 64, jatekosnev, "white"), (450, 302))

        #Játékos név megadása kattintás ellenörzés
        if jatekosnev_doboz.collidepoint(eger):
            if click == True:
                aktiv = True

        #Indítás gomb érzékelése
        if inditasgomb.collidepoint(eger) and jatekosnev!="":
            ablak.blit(szoveg_kiiras("Constatia", 64, "Indítás", "darkgray"), (850, 470))
            if click == True:
                return jatekosnev

        #Visszalépés gomb megnyomása
        if visszalepesgomb.collidepoint(eger):
            if click == True:
                break

        pygame.display.update()

#Játék elindítása: kezdetben a nehezség választásával indul, utána pedig a név megadásával
def jatek_inditasa(ablak):
    # Visszanyíl logo
    visszanyil = pygame.image.load("vissza.png")
    nehezseg = None
    jatekosnev=None
    while True:
        #Ablak tisztázása
        ablak.fill((23, 53, 128))

        click = False
        eger = pygame.mouse.get_pos()

        #Visszalépés gomb megjelenítése
        visszalepesgomb = pygame.Rect(150, 85, 95, 80)
        pygame.draw.rect(ablak, (23, 53, 128), visszalepesgomb)
        ablak.blit(visszanyil,(150,85))

        #Cím szöveg kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 70, "Válassz nehézséget", "white"), (400, 80))

        #Könnyű szöveg kiírása
        konnyugomb = pygame.Rect(550, 250, 160, 40)
        pygame.draw.rect(ablak, (23, 53, 128), konnyugomb)
        ablak.blit(szoveg_kiiras("Constatia", 64, "Könnyű", "white"), (550, 250))

        #Közepes szöveg kiírása
        kozepesgomb = pygame.Rect(550, 350, 185, 40)
        pygame.draw.rect(ablak, (23, 53, 128), kozepesgomb)
        ablak.blit(szoveg_kiiras("Constatia", 64, "Közepes", "white"), (550, 350))

        #Kilépés szöveg kiírása
        nehezgomb = pygame.Rect(550, 450, 130, 40)
        pygame.draw.rect(ablak, (23, 53, 128), nehezgomb)
        ablak.blit(szoveg_kiiras("Constatia", 64, "Nehéz", "white"), (550, 450))

        #Eventek kezelése
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        #Visszalépés gomb megnyomása
        if visszalepesgomb.collidepoint(eger):
            if click == True:
                break

        #Könnyű gomb érzékelése
        if konnyugomb.collidepoint(eger):
            ablak.blit(szoveg_kiiras("Constatia", 64, "Könnyű", "darkgray"), (550, 250))
            if click == True:
                nehezseg = "könnyű"
                jatekosnev=jatekos_nev_megadasa(ablak)

        #Közepes gomb érzékelése
        elif kozepesgomb.collidepoint(eger):
            ablak.blit(szoveg_kiiras("Constatia", 64, "Közepes", "darkgray"), (550, 350))
            if click == True:
                nehezseg = "közepes"
                jatekosnev=jatekos_nev_megadasa(ablak)

        #Nehéz gomb érzékelése
        elif nehezgomb.collidepoint(eger):
            ablak.blit(szoveg_kiiras("Constatia", 64, "Nehéz", "darkgray"), (550, 450))
            if click == True:
                nehezseg = "nehéz"
                jatekosnev=jatekos_nev_megadasa(ablak)

        if jatekosnev is not None:
            jatekvezerles.main(ablak, nehezseg, jatekosnev)

        pygame.display.update()

#Főmenű megjelenítése
def main_menu(ablak):
    while True:
        ablak.fill((23, 53, 128))

        #Cím szöveg kiírása
        ablak.blit(szoveg_kiiras("Gill Sans", 100, "A piramis","white"), (450, 50))

        #Játék indítása szöveg kiírása
        jatekinditasagomb = pygame.Rect(450, 250, 300, 50)
        pygame.draw.rect(ablak, (23, 53, 128), jatekinditasagomb)
        ablak.blit(szoveg_kiiras("Constatia", 64, "Játék indítása","white"), (450, 250))

        #Ranglista szöveg kiírása
        ranglistagomb = pygame.Rect(450, 350, 207, 50)
        pygame.draw.rect(ablak, (23, 53, 128), ranglistagomb)
        ablak.blit(szoveg_kiiras("Constatia", 64, "Ranglista", "white"), (450, 350))

        #Kilépés szöveg kiírása
        kilepesgomb = pygame.Rect(450, 450, 160, 50)
        pygame.draw.rect(ablak, (23, 53, 128), kilepesgomb)
        ablak.blit(szoveg_kiiras("Constatia", 64, "Kilépés", "white"), (450, 450))

        #Eventek nézése
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        #Egér pozíció
        eger = pygame.mouse.get_pos()

        #Játék indítása gomb érzékelése
        if jatekinditasagomb.collidepoint(eger):
            ablak.blit(szoveg_kiiras("Constatia", 64, "Játék indítása","darkgray"), (450, 250))
            if click == True:
                jatek_inditasa(ablak)

        #Ranglista gomb érzékelése
        elif ranglistagomb.collidepoint(eger):
            ablak.blit(szoveg_kiiras("Constatia", 64, "Ranglista", "darkgray"), (450, 350))
            if click == True:
                ranglista(ablak)


        #Kilépés gomb érzékelése
        elif kilepesgomb.collidepoint(eger):
            ablak.blit(szoveg_kiiras("Constatia", 64, "Kilépés", "darkgray"), (450, 450))
            if click == True:
                kilepes()

        pygame.display.update()

