import pygame
import random
import megjelenites
import fajlkezeles

#Játékos adatait tároló osztály: Név, választott nehézség, megnyert vagy aktuális összeg
class jatekos_adatok:
    def __init__(self,nev,nehezseg,osszeg):
        self.nev = nev
        self.nehezseg = nehezseg
        self.osszeg = int(osszeg)

#Kérdések adatait tároló osztály
class kerdes_adatok:
    def __init__(self,nehezseg,kerdes,A,B,C,D,valasz,kategoria):
        if nehezseg >=1 and nehezseg <4:
            self.nehezseg ="könnyű"
        elif nehezseg>=4 and nehezseg <9:
            self.nehezseg ="közepes"
        elif nehezseg>=9:
            self.nehezseg = "nehéz"
        self.kerdes = kerdes
        self.A = str(A)
        self.B = str(B)
        self.C = str(C)
        self.D = str(D)
        self.valasz = valasz
        self.kategoria = kategoria

#Játékvezérlése minden függvény ide tér vissza ez kezeli a játékot
def main(ablak,nehezseg,jatekosnev):
#Listák dekralálása

    #Játékos által választott számok
    valasztottszamok = []

    #Összes kérdés tárolása nehézségtől függetlenül
    osszeskerdes = fajlkezeles.kerdesek_beolvas()

    #Nehézség szerint külön a kérdések
    kerdesek = kerdesek_nehezseg_szerint(osszeskerdes,nehezseg)

    #Kérdés eredmények jól vagy rosszul válaszolt a kérdésre a játékos
    eredmeny=None
    eredmenyek = []

    #Játékos összege
    osszeg=0

    #Játékos jó válaszainak száma
    jovalaszok=0

    #Bool érték hogy akar e a játékos bunoszfordulot
    bunoszfordulo = False

    #Fordulok szövegei bővíteni kell ha több fordulót szeretnénk
    fordulokszoveg = ["Első forduló","Második forduló","Harmadik forduló"]

    #Mátrix és tárolja a kérdések címét fordulóként
    kerdesekszoveg = [["Első kérdés","Második kérdés","Harmadik kérdés"],["Negyedik kérdés","Ötödik kérdés","Hatodik kérdés"],["Hetedik kérdés","Nyolcadik kérdés","Kilencedik kérdés"]]

    #Egy forduló lefutása range max értéke adja meg a körök számát
    for i in range(3):
    #forduló kezdet
        megjelenites.atvezeto_szoveg(ablak, fordulokszoveg[i], 380, 250)

        valasztottszamok = megjelenites.szam_valasztas(ablak)
        valasztottszamok = jatekos_valasztott_szamok(valasztottszamok)

        # Kérdés 1
        megjelenites.atvezeto_szoveg(ablak, kerdesekszoveg[i][0], 380, 250)
        k = veletlen_kerdes(kerdesek)
        eredmeny = megjelenites.egy_kerdes(ablak, kerdesek[k])
        eredmenyek.append(eredmeny)
        kerdesek.pop(k)

        # Kérdés 2
        megjelenites.atvezeto_szoveg(ablak, kerdesekszoveg[i][1], 380, 250)
        k = veletlen_kerdes(kerdesek)
        eredmeny = megjelenites.egy_kerdes(ablak, kerdesek[k])
        eredmenyek.append(eredmeny)
        kerdesek.pop(k)

        # Kérdés 3
        megjelenites.atvezeto_szoveg(ablak, kerdesekszoveg[i][2], 360, 250)
        k = veletlen_kerdes(kerdesek)
        eredmeny = megjelenites.egy_kerdes(ablak, kerdesek[k])
        eredmenyek.append(eredmeny)
        kerdesek.pop(k)

        # Nőveli a joválaszok számát
        eredmenyek = labdak_szine(eredmenyek)
        jovalaszok += jo_valaszok_szama(eredmenyek)

        # Labdaleesés
        osszeg = megjelenites.labdaeses(ablak, eredmenyek, valasztottszamok, i, osszeg)
        megjelenites.atvezeto_szoveg(ablak, "Eddig nyermény: " + str(osszeg), 180, 250)

        # Eredmények listát nulláza
        eredmenyek = []



    #Megnézi hogy a játékos összege nulla-e ha nulla akkor kiírja játék végét és véget ér a játék
    #Ha nem nulla akkor a játékos dönti el hogy szeretne-e a bunosz fordulóval játszani
    #Mindkét esetben hozzáadaj az adatokat a ranglistához és kilép a játékból
    if osszeg==0:
        megjelenites.jatek_vege_szoveg(ablak,osszeg)
        ranglista(jatekosnev,nehezseg,osszeg)
        pygame.quit()
        exit()
    else:
        bunoszfordulo = megjelenites.lesz_bunosz_fordulo(ablak)
        if bunoszfordulo==True:
            osszeg =megjelenites.bonusz_fordulo(ablak,jovalaszok,osszeg)
            megjelenites.jatek_vege_szoveg(ablak, osszeg)
            ranglista(jatekosnev, nehezseg, osszeg)
            pygame.quit()
            exit()
        else:
            megjelenites.jatek_vege_szoveg(ablak, osszeg)
            ranglista(jatekosnev, nehezseg, osszeg)
            pygame.quit()
            exit()

#A játékos áltál választott nehézségi szint kérdéseit kigyűjti az összes kérdésből
def kerdesek_nehezseg_szerint(lista,nehezseg):
    kerdesek = []
    for i in lista:
        if i.nehezseg == nehezseg:
            kerdesek.append(i)
    return kerdesek

#Véletlenül kiválaszt egy kérdést
def veletlen_kerdes(lista):
    return random.randint(0,len(lista))

#Listát bool listát kap baraméterként és visszaadja egy listában azokat a számokat amiket választott a játékos
def jatekos_valasztott_szamok(lista):
    szamok =[]
    for i in range(len(lista)):
        if lista[i]==True:
            szamok.append(i+1)
    return szamok

#Listát kap hogy a játékos hogyan válaszolt a kérdésekre és visszaadja a labdák szineit
def labdak_szine(lista):
    szinek = []
    for i in lista:
        if i == True:
            szinek.append("Green")
        else:
            szinek.append("Red")
    return szinek

#Számolja a jó válaszok számát a bunosz forduló miatt érdekes
def jo_valaszok_szama(lista):
    db=0
    for i in lista:
        if i =="Green":
            db+=1
    return db

#Játékos hozzáadása a ranglistához
def ranglista(jatekosnev,nehezseg,osszeg):
    lista = [jatekos_adatok(jatekosnev,nehezseg,osszeg)]
    fajlkezeles.ranglista_kiir(lista)



