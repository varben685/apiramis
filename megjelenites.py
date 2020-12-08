import pygame
import menu
import pymunk
import random

#3 számot választ a játékos és listával adja vissza az értékeket
def szam_valasztas(ablak):
    valasztva = [False]*6
    db=0
    #Ciklus amíg a játékos nem választ 3 számot
    while db!=4:
        ablak.fill((17, 41, 102))

        #Cím szöveg kiírása
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 60, "Válassz hogy ebben a körben","white"), (260, 70))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 60, "melyik három lyukból essen le a labda", "white"), (200, 135))
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

        #Gomb 1 kirajzolás
        gomb1 = pygame.Rect(410, 295, 100, 100)
        if valasztva[0]==False:
            pygame.draw.rect(ablak, (11, 29, 74), gomb1)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "1", "white"), (430, 300))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), gomb1)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "1", "white"), (430, 300))

        #Gomb 2 kirajzolás
        gomb2 = pygame.Rect(590, 295, 100, 100)
        if valasztva[1]==False:
            pygame.draw.rect(ablak, (11, 29, 74), gomb2)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "2", "white"), (610, 300))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), gomb2)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "2", "white"), (610, 300))

        #Gomb 3 kirajzolás
        gomb3 = pygame.Rect(770, 295, 100, 100)
        if valasztva[2] == False:
            pygame.draw.rect(ablak, (11, 29, 74), gomb3)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "3", "white"), (790, 300))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), gomb3)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "3", "white"), (790, 300))

        #Gomb 4 kirajzolás
        gomb4 = pygame.Rect(500, 430, 100, 100)
        if valasztva[3]==False:
            pygame.draw.rect(ablak, (11, 29, 74), gomb4)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "4", "white"), (520, 430))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), gomb4)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "4", "white"), (520, 430))

        #Gomb 5 kirajzolás
        gomb5 = pygame.Rect(670, 430, 100, 100)
        if valasztva[4]==False:
            pygame.draw.rect(ablak, (11, 29, 74), gomb5)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "5", "white"), (690, 430))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), gomb5)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "5", "white"), (690, 430))

        #Gomb 6 kirajzolás
        gomb6 = pygame.Rect(585, 560, 100, 100)
        if valasztva[5]==False:
            pygame.draw.rect(ablak, (11, 29, 74), gomb6)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "6", "white"), (605, 560))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), gomb6)
            ablak.blit(menu.szoveg_kiiras("Constatia", 150, "6", "white"), (605, 560))

        #Ha megvan a három válaszott akkor késletetti a tovább lépést
        if db==3:
            pygame.display.update()
            pygame.time.delay(2000)
            db+=1

        if db<=3:
            #gomb1 érzékelése és inaktivvá tétele
            if valasztva[0]==False:
                if gomb1.collidepoint(eger)== True and click==True:
                    valasztva[0] = True
                    db+=1

            #gomb2 érzékelése és inaktivvá tétele
            if valasztva[1]==False:
                if gomb2.collidepoint(eger) == True and click == True:
                    valasztva[1] = True
                    db+=1

            #gomb3 érzékelése és inaktivvá tétele
            if valasztva[2]==False:
                if gomb3.collidepoint(eger) == True and click == True:
                    valasztva[2] = True
                    db+=1

            #gomb4 érzékelése és inaktivvá tétele
            if valasztva[3]==False:
                if gomb4.collidepoint(eger) == True and click == True:
                    valasztva[3] = True
                    db += 1

            #gomb5 érzékelése és inaktivvá tétele
            if valasztva[4]==False:
                if gomb5.collidepoint(eger) == True and click == True:
                    valasztva[4] = True
                    db += 1

            #gomb6 érzékelése és inaktivvá tétele
            if valasztva[5]==False:
                if gomb6.collidepoint(eger) == True and click == True:
                    valasztva[5] = True
                    db += 1

        pygame.display.update()

    return valasztva

#Átvezető szöveget ír ki a fordulók és a kérdések között
def atvezeto_szoveg(ablak,szoveg,x,y):
    while True:
        ablak.fill((17, 41, 102))

        #Cím szöveg kiírása
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 100, szoveg,"white"), (x, y))
        #Eventek nézése
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()
        pygame.time.wait(1500)
        break

#Kérdés hogy a játékos akar e bunosz fordulót
def lesz_bunosz_fordulo(ablak):
    while True:
        ablak.fill((17, 41, 102))

        #Cím szöveg kiírása
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "Szeretnél részt venni a bónusz fordulóban? ","white"), (220, 70))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "Ebben a körben a válaszaid alapján ", "white"), (220, 135))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "duppla vagy semmi értékeket helyeztünk a rekeszekbe. ", "white"), (220, 200))

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

        #Gomb igen kirajzolás
        igen = pygame.Rect(400, 320, 70, 70)
        pygame.draw.rect(ablak, (17, 41, 102), igen)
        ablak.blit(menu.szoveg_kiiras("Constatia", 60, "Igen", "white"), (400, 320))

        #Gomb nem kirajzolás
        nem = pygame.Rect(750, 320, 100, 100)
        pygame.draw.rect(ablak, (17, 41, 102), nem)
        ablak.blit(menu.szoveg_kiiras("Constatia", 60, "Nem", "white"), (750, 320))

        #Igen nem gomb érzékelése
        if igen.collidepoint(eger):
            ablak.blit(menu.szoveg_kiiras("Constatia", 60, "Igen", "darkgray"), (400, 320))
            if click == True:
                return True
        if nem.collidepoint(eger):
            ablak.blit(menu.szoveg_kiiras("Constatia", 60, "Nem", "darkgray"), (750, 320))
            if click == True:
                return False

        pygame.display.update()

#Játék vége szöveg kiírás
def jatek_vege_szoveg(ablak,osszeg):
    while True:
        ablak.fill((17, 41, 102))

        #Cím szöveg kiírása
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 80,"Véget ért a játék!","white"), (350,150))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 60, "Elvitt nyereményed: ", "white"), (250, 260))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 60, str(osszeg), "white"), (750, 260))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 60, "Köszönöm hogy játszottál ", "white"), (270, 350))
        ablak.blit(menu.szoveg_kiiras("Gill Sans", 60, "Készítette: Varga Bence ", "white"), (70, 640))
        #Eventek nézése
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()
        pygame.time.wait(5000)
        break

#Egy kérdés megjelenítése
def egy_kerdes(ablak,adatok):
    valasztva = [False]*4
    db=0
    megjelolt=0
    while True:
        ablak.fill((17, 41, 102))

        #Kérdés hátterét hozza létre
        kerdeshatter = pygame.Rect(0, 255, 1280, 120)
        pygame.draw.rect(ablak, (11, 29, 74), kerdeshatter)

        #Megvizsgálja hogy a kérdés 50 karakternél hosszabb-e ha igen akkor új sorba írja ki így nem lóg ki a képernyőről
        if len(adatok.kerdes)>50:
            i=49
            reszlet=""
            while reszlet!=" " and i<len(adatok.kerdes)-1:
                reszlet = adatok.kerdes[i]
                i+=1
            elsoresz= adatok.kerdes[:i]
            masodikresz = adatok.kerdes[i:]

            #Kérdés kiírása két sorba
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, elsoresz, "white"), (210, 265))
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, masodikresz, "white"), (210, 315))

        elif len(adatok.kerdes)<40:
            #Kérdés kiírása 40 karakternél rövidebb picikét beljebb kezdődik
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, adatok.kerdes,"white"), (310, 280))

        elif len(adatok.kerdes)<30:
            #Kérdés kiírása 30 karakternél rövidebb picikét beljebb kezdődik
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, adatok.kerdes, "white"), (380, 280))

        elif len(adatok.kerdes)<20:
            #Kérdés kiírása 20 karakternél rövidebb picikét beljebb kezdődik
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, adatok.kerdes, "white"), (450, 280))

        elif len(adatok.kerdes)<10:
            #Kérdés kiírása 10 karakternél rövidebb picikét beljebb kezdődik
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, adatok.kerdes, "white"), (540, 280))

        else:
            #Kérdés kiírása
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, adatok.kerdes, "white"), (265, 280))

        #A válasz lehetőség kiírása
        Agomb = pygame.Rect(435, 397, 420, 60)
        if valasztva[0]==False:
            pygame.draw.rect(ablak, (11, 29, 74), Agomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "A, "+adatok.A, "white"), (450, 403))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), Agomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "A, " + adatok.A, "white"), (450, 403))
            db+=1

        #B válasz lehetőség kiírása
        Bgomb = pygame.Rect(435, 477, 420, 60)
        if valasztva[1]==False:
            pygame.draw.rect(ablak, (11, 29, 74), Bgomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "B, " + adatok.B, "white"), (450, 485))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), Bgomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "B, " + adatok.B, "white"), (450, 485))
            db += 1

        #C válasz lehetőség kiírása
        Cgomb = pygame.Rect(435, 559, 420, 60)
        if valasztva[2]==False:
            pygame.draw.rect(ablak, (11, 29, 74), Cgomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "C, " + adatok.C, "white"), (450, 567))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), Cgomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "C, " + adatok.C, "white"), (450, 567))
            db += 1

        #D válasz lehetőség kiírása
        Dgomb = pygame.Rect(435, 641, 420, 60)
        if valasztva[3]==False:
            pygame.draw.rect(ablak, (11, 29, 74), Dgomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "D, " + adatok.D, "white"), (450, 649))
        else:
            pygame.draw.rect(ablak, (76, 77, 79), Dgomb)
            ablak.blit(menu.szoveg_kiiras("Gill Sans", 40, "D, " + adatok.D, "white"), (450, 649))
            db+=1

        #Ha a játékos választott egy választ akkor megnézi hogy melyiket választotta és hogy helyes-e
        #És visszatér hogy jo volt a válasz vagy nem
        if db==1:
            pygame.display.update()
            pygame.time.delay(3000)
            for i in range(len(valasztva)):
                if valasztva[i]==True:
                    if i==0:
                        megjelolt="A"
                    elif i==1:
                        megjelolt="B"
                    elif i==2:
                        megjelolt="C"
                    elif i==3:
                        megjelolt="D"
            if adatok.valasz==megjelolt:
                ablak.fill((5, 173, 30))
                pygame.display.update()
                pygame.time.delay(2000)
                return True
            else:
                ablak.fill((201, 13, 6))
                pygame.display.update()
                pygame.time.delay(2000)
                return False

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

        if db ==0:
            if valasztva[0]==False:
                if Agomb.collidepoint(eger):
                    if click == True:
                        valasztva[0]=True

            if valasztva[1]==False:
                if Bgomb.collidepoint(eger):
                    if click == True:
                        valasztva[1]=True

            if valasztva[2]==False:
                if Cgomb.collidepoint(eger):
                    if click == True:
                        valasztva[2]=True

            if valasztva[3]==False:
                if Dgomb.collidepoint(eger):
                    if click == True:
                        valasztva[3]=True

        pygame.display.update()

#Akadály testének létrehozása
def akadaly_test(jatekter,x,y):
    test = pymunk.Body(body_type=pymunk.Body.STATIC)
    test.position= (x,y)
    forma = pymunk.Circle(test,17)
    jatekter.add(test,forma)
    return forma

#Akadályok kirajzolása
def akadaly_rajzol(ablak,akadalyok):
    for akadaly in akadalyok:
        x = int(akadaly.body.position.x)
        y = int(akadaly.body.position.y)
        pygame.draw.circle(ablak,(195, 204, 219),(x,y),17)

#Labda érzékelése
def labda_test(jatekter,x,y):
    test = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
    test.position=(x, y)
    forma = pymunk.Circle(test, 22)
    jatekter.add(test, forma)
    return forma

#Labda kirajzol piros vagy zöld
def labda_rajzol(ablak,labda,szin):
    x = int(labda.body.position.x)
    y = int(labda.body.position.y)
    pygame.draw.circle(ablak, pygame.Color(szin), (x, y), 22)

#Piramis pálya elemek megrajzolása
def falak_rajzol(ablak,jatekter):
    #Bal fal
    balfal = pymunk.Segment(jatekter.static_body, (100, 475), (310, 20), 5)
    jatekter.add(balfal)
    pygame.draw.line(ablak,(195, 204, 219),(100, 475),(310, 20),5)

    #Jobb fal
    jobbfal = pymunk.Segment(jatekter.static_body, (1180, 475), (970, 20), 5)
    jatekter.add(jobbfal)
    pygame.draw.line(ablak, (195, 204, 219), (1180, 475), (970, 20), 5)

    #Bal fal alatti egyenes
    balegyenes = pymunk.Segment(jatekter.static_body, (100, 475), (100, 620), 5)
    jatekter.add(balegyenes)
    pygame.draw.line(ablak, (195, 204, 219), (100, 475), (100, 620), 5)

    #Jobb fal alatti egyenes
    jobbegyenes = pymunk.Segment(jatekter.static_body, (1180, 475), (1180, 620), 5)
    jatekter.add(jobbegyenes)
    pygame.draw.line(ablak, (195, 204, 219), (1180, 475), (1180, 620), 5)

    #Balról az első rekesz
    egy = pymunk.Segment(jatekter.static_body, (255, 510), (255, 620), 5)
    jatekter.add(egy)
    pygame.draw.line(ablak, (195, 204, 219), (255, 510), (255, 620), 5)

    #Második rekesz
    ketto = pymunk.Segment(jatekter.static_body, (370, 510), (370, 620), 5)
    jatekter.add(ketto)
    pygame.draw.line(ablak, (195, 204, 219), (370, 510), (370, 620), 5)

    #Harmadik rekesz
    harom = pymunk.Segment(jatekter.static_body, (475, 510), (475, 620), 5)
    jatekter.add(harom)
    pygame.draw.line(ablak, (195, 204, 219), (475, 510), (475, 620), 5)

    #Negydik rekesz
    negy = pymunk.Segment(jatekter.static_body, (590, 510), (590, 620), 5)
    jatekter.add(negy)
    pygame.draw.line(ablak, (195, 204, 219), (590, 510), (590, 620), 5)

    #Ötödik rekesz
    ot = pymunk.Segment(jatekter.static_body, (705, 510), (705, 620), 5)
    jatekter.add(ot)
    pygame.draw.line(ablak, (195, 204, 219), (705, 510), (705, 620), 5)

    #Hatodik rekesz
    hat = pymunk.Segment(jatekter.static_body, (810, 510), (810, 620), 5)
    jatekter.add(hat)
    pygame.draw.line(ablak, (195, 204, 219), (810, 510), (810, 620), 5)

    #Hetedik rekesz
    het = pymunk.Segment(jatekter.static_body, (920, 510), (920, 620), 5)
    jatekter.add(het)
    pygame.draw.line(ablak, (195, 204, 219), (920, 510), (920, 620), 5)

    #Nyolcadik rekesz
    nyolc = pymunk.Segment(jatekter.static_body, (1035, 510), (1035, 620), 5)
    jatekter.add(nyolc)
    pygame.draw.line(ablak, (195, 204, 219), (1035, 510), (1035, 620), 5)

#Megrajzolja a lyukakat innen esnek ki a labdák
def lyukak_rajzol(ablak):
    #Első lyuk
    pygame.draw.circle(ablak, (2, 22, 102), (360, 50), 40)
    pygame.draw.circle(ablak, (0, 0, 0), (360, 50),35)

    #Második lyuk
    pygame.draw.circle(ablak, (2, 22, 102), (475, 50), 40)
    pygame.draw.circle(ablak, (0, 0, 0), (475, 50), 35)

    #Harmadik lyuk
    pygame.draw.circle(ablak, (2, 22, 102), (585, 50), 40)
    pygame.draw.circle(ablak, (0, 0, 0), (585, 50), 35)

    #Negyedik lyuk
    pygame.draw.circle(ablak, (2, 22, 102), (695, 50), 40)
    pygame.draw.circle(ablak, (0, 0, 0), (695, 50), 35)

    #Ötödik lyuk
    pygame.draw.circle(ablak, (2, 22, 102), (805, 50), 40)
    pygame.draw.circle(ablak, (0, 0, 0), (805, 50), 35)

    #Hatodik lyuk
    pygame.draw.circle(ablak, (2, 22, 102), (915, 50), 40)
    pygame.draw.circle(ablak, (0, 0, 0), (915, 50), 35)

#Piramisban levő akadályok megjelenítése és egy tömmbel tér vissza az akadályok adataival
def akadalyok_megjelenitese(jatekter):
    #Tömb létrehozása
    akadalyok = []

    #Negyedik sor akadályia
    akadalyok.append(akadaly_test(jatekter, 200, 450))
    akadalyok.append(akadaly_test(jatekter, 310, 450))
    akadalyok.append(akadaly_test(jatekter, 420, 450))
    akadalyok.append(akadaly_test(jatekter, 530, 450))
    akadalyok.append(akadaly_test(jatekter, 640, 450))
    akadalyok.append(akadaly_test(jatekter, 750, 450))
    akadalyok.append(akadaly_test(jatekter, 860, 450))
    akadalyok.append(akadaly_test(jatekter, 970, 450))
    akadalyok.append(akadaly_test(jatekter, 1080, 450))

    #Harmadik sor akadályai
    akadalyok.append(akadaly_test(jatekter, 235, 360))
    akadalyok.append(akadaly_test(jatekter, 345, 360))
    akadalyok.append(akadaly_test(jatekter, 455, 360))
    akadalyok.append(akadaly_test(jatekter, 565, 360))
    akadalyok.append(akadaly_test(jatekter, 675, 360))
    akadalyok.append(akadaly_test(jatekter, 785, 360))
    akadalyok.append(akadaly_test(jatekter, 895, 360))
    akadalyok.append(akadaly_test(jatekter, 1005, 360))

    #Második sor akadályai
    akadalyok.append(akadaly_test(jatekter, 310, 270))
    akadalyok.append(akadaly_test(jatekter, 430, 270))
    akadalyok.append(akadaly_test(jatekter, 540, 270))
    akadalyok.append(akadaly_test(jatekter, 650, 270))
    akadalyok.append(akadaly_test(jatekter, 760, 270))
    akadalyok.append(akadaly_test(jatekter, 870, 270))
    akadalyok.append(akadaly_test(jatekter, 980, 270))

    #Első sor akadályai
    akadalyok.append(akadaly_test(jatekter, 360, 180))
    akadalyok.append(akadaly_test(jatekter, 475, 180))
    akadalyok.append(akadaly_test(jatekter, 585, 180))
    akadalyok.append(akadaly_test(jatekter, 695, 180))
    akadalyok.append(akadaly_test(jatekter, 805, 180))
    akadalyok.append(akadaly_test(jatekter, 915, 180))

    return akadalyok

#Piramisban nyerhető összegek kiírása
def nyeremenyek_kiir(ablak,kor):
    nyermenyek=[["250.000","10.000","500.000","20.000","1.000.000","20.000","500.000","10.000","250.000"],["500.000","20.000","1.000.000","40.000","2.000.000","40.000","1.000.000","20.000","500.000"],["750.000","40.000","2.000.000","60.000","10.000.000","60.000","2.000.000","40.000","750.000"]]
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][0], "white"), (150, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][1], "white"), (280, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][2], "white"), (380, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][3], "white"), (500, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][4], "white"), (600, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][5], "white"), (730, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][6], "white"), (825, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30,nyermenyek[kor][7], "white"), (950, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[kor][8], "white"), (1080, 600))
#Labdaesés megjelenítése és kezelése

#Labdaesés teljese megjelenítése és kezelése
def labdaeses(ablak,szinek,labdak,kor,osszeg):
    #Játéktér és gravitáció beállítása
    jatekter = pymunk.Space()
    jatekter.gravity = (0, 110)

    #Összes akadály eltárolása
    akadalyok = akadalyok_megjelenitese(jatekter)

    #Megnyerhető nyeremények mátrixban
    nyermenyek=[[250000,10000,500000,20000,1000000,20000,500000,10000,250000],[500000,20000,1000000,40000,2000000,40000,1000000,20000,500000],[750000,40000,2000000,60000,10000000,60000,2000000,40000,750000]]

    for i in range(len(szinek)):

        #A játékos által választott lyukba helyezi a labdát
        veletlen=random.randint(-10,10)
        if veletlen==0:
            veletlen = random.randint(-10, 10)
            if veletlen==0:
                veletlen = random.randint(-10, 10)
        if labdak[i]==1:
            labda = (labda_test(jatekter, 360+veletlen, 50))
        if labdak[i]==2:
            labda = (labda_test(jatekter, 475+veletlen, 50))
        if labdak[i]==3:
            labda = (labda_test(jatekter, 585+veletlen, 50))
        if labdak[i]==4:
            labda = (labda_test(jatekter, 695+veletlen, 50))
        if labdak[i]==5:
            labda = (labda_test(jatekter, 805+veletlen, 50))
        if labdak[i]==6:
            labda = (labda_test(jatekter, 915+veletlen, 50))

        while True:
            ablak.fill((17, 41, 102))

            #Eventek nézése
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #Elemek megrajzolása
            lyukak_rajzol(ablak)
            falak_rajzol(ablak,jatekter)
            akadaly_rajzol(ablak,akadalyok)
            labda_rajzol(ablak,labda,szinek[i])

            #Figyeli a labdának a pozicióját és az összegeket az alapján növeli csökkenti
            if (labda.body.position.x>=100 and labda.body.position.x<255)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][0]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][0]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>255 and labda.body.position.x<370)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][1]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][1]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>370 and labda.body.position.x<475)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][2]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][2]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>475 and labda.body.position.x<590)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][3]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][3]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>590 and labda.body.position.x<705)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][4]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][4]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>705 and labda.body.position.x<810)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][5]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][5]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>810 and labda.body.position.x<920)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][6]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][6]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>920 and labda.body.position.x<1035)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][7]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][7]

                pygame.time.delay(1000)
                break

            if (labda.body.position.x>1035 and labda.body.position.x<1180)and labda.body.position.y>560:
                if szinek[i]=="Red":
                    osszeg-=nyermenyek[kor][8]
                    if osszeg<0:
                        osszeg=0
                else:
                    osszeg+=nyermenyek[kor][8]

                pygame.time.delay(1000)
                break

            #Kiírja a nyeremény szöveget és a jelenlegi összeget
            ablak.blit(menu.szoveg_kiiras("Constatia", 60, "Nyeremény: ", "white"), (290, 670))
            ablak.blit(menu.szoveg_kiiras("Constatia", 50, str(osszeg), "white"), (570, 675))
            nyeremenyek_kiir(ablak,kor)

            jatekter.step(1 / 50)
            pygame.display.update()

    return osszeg

#Kiírja a bunosz forduló "összegeit"
def bonusz_eredmenyek_kiir(ablak,nyermenyek):
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[0], "white"), (150, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[1], "white"), (280, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[2], "white"), (400, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[3], "white"), (500, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[4], "white"), (615, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[5], "white"), (730, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[6], "white"), (838, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[7], "white"), (950, 600))
    ablak.blit(menu.szoveg_kiiras("Constatia", 30, nyermenyek[8], "white"), (1080, 600))

#Elkészíti a bunosz kör nyerményeinek listáját
def bonusz_nyeremyenk_lista(jovalaszok):
    nyermenyek =[]
    if jovalaszok == 1:
        nyermenyek = ["Dupla", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi"]
    elif jovalaszok == 2:
        nyermenyek = ["Dupla", "Semmi", "Dupla", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi"]
    elif jovalaszok == 3:
        nyermenyek = ["Dupla", "Semmi", "Dupla", "Semmi", "Semmi", "Semmi", "Semmi", "Semmi", "Dupla"]
    elif jovalaszok == 4:
        nyermenyek = ["Dupla", "Semmi", "Dupla", "Semmi", "Semmi", "Semmi", "Dupla", "Semmi", "Dupla"]
    elif jovalaszok == 5:
        nyermenyek = ["Dupla", "Dupla", "Dupla", "Semmi", "Semmi", "Semmi", "Dupla", "Semmi", "Dupla"]
    elif jovalaszok == 6:
        nyermenyek = ["Dupla", "Dupla", "Dupla", "Semmi", "Semmi", "Semmi", "Dupla", "Dupla", "Dupla"]
    elif jovalaszok == 7:
        nyermenyek = ["Dupla", "Dupla", "Dupla", "Dupla", "Semmi", "Semmi", "Dupla", "Dupla", "Dupla"]
    elif jovalaszok == 8:
        nyermenyek = ["Dupla", "Dupla", "Dupla", "Dupla", "Semmi", "Dupla", "Dupla", "Dupla", "Dupla"]
    elif jovalaszok == 9:
        nyermenyek = ["Dupla", "Dupla", "Dupla", "Dupla", "Dupla", "Dupla", "Dupla", "Dupla", "Semmi"]
    return nyermenyek

#Bunosz forduló felépítése
def bonusz_fordulo(ablak,jovalaszok,osszeg):
    #Játéktér és gravitáció beállítása
        jatekter = pymunk.Space()
        jatekter.gravity = (0, 110)

        #Összes akadály eltárolása
        akadalyok = akadalyok_megjelenitese(jatekter)

        #Megnyerhető nyeremények mátrixban

        nyeremenyek = bonusz_nyeremyenk_lista(jovalaszok)

        #3. lyukba helyezi a labdát
        veletlen=random.randint(-10,10)
        if veletlen==0:
            veletlen = random.randint(-10, 10)
            if veletlen==0:
                veletlen = random.randint(-10, 10)
        labda = (labda_test(jatekter, 585+veletlen, 50))

        while True:
            ablak.fill((17, 41, 102))

            #Eventek nézése
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                #Elemek megrajzolása
            lyukak_rajzol(ablak)
            falak_rajzol(ablak,jatekter)
            akadaly_rajzol(ablak,akadalyok)
            labda_rajzol(ablak,labda,"Yellow")

            #Figyeli a labdának a pozicióját és az összegeket az alapján növeli csökkenti
            if (labda.body.position.x>=100 and labda.body.position.x<255)and labda.body.position.y>560:
                if nyeremenyek[0]=="Dupla":
                    osszeg = osszeg*2
                else:
                    osszeg=0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>255 and labda.body.position.x<370)and labda.body.position.y>560:
                if nyeremenyek[1] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>370 and labda.body.position.x<475)and labda.body.position.y>560:
                if nyeremenyek[2] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>475 and labda.body.position.x<590)and labda.body.position.y>560:
                if nyeremenyek[3] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>590 and labda.body.position.x<705)and labda.body.position.y>560:
                if nyeremenyek[4] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>705 and labda.body.position.x<810)and labda.body.position.y>560:
                if nyeremenyek[5] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>810 and labda.body.position.x<920)and labda.body.position.y>560:
                if nyeremenyek[6] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>920 and labda.body.position.x<1035)and labda.body.position.y>560:
                if nyeremenyek[7] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            if (labda.body.position.x>1035 and labda.body.position.x<1180)and labda.body.position.y>560:
                if nyeremenyek[8] == "Dupla":
                    osszeg = osszeg * 2
                else:
                    osszeg = 0
                pygame.time.delay(1000)
                return osszeg

            #Kiírja a nyeremény szöveget és a jelenlegi összeget
            ablak.blit(menu.szoveg_kiiras("Constatia", 60, "Nyeremény: ", "white"), (290, 670))
            ablak.blit(menu.szoveg_kiiras("Constatia", 50, str(osszeg), "white"), (570, 675))
            bonusz_eredmenyek_kiir(ablak,nyeremenyek)


            jatekter.step(1 / 50)
            pygame.display.update()




