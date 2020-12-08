import jatekvezerles

#Ranglista fájl beolvasása meghívja a játékos_adatok osztályt és ilyen listát hoz létre melyet rendezz összeg szerint
def ranglista_beolvas():
    try:
        f = open("ranglista.txt","rt",encoding="utf-8")
        lista =[]
        for sor in f:
            sor = sor.rstrip("\n")
            darabok = sor.split(":")
            adat = jatekvezerles.jatekos_adatok(darabok[0],darabok[1],darabok[2])
            lista.append(adat)
        f.close()
        lista.sort(key=lambda x: x.osszeg,reverse=True)
        return lista
    except FileNotFoundError as e:
        print("Nem található a fájl (ranglista.txt)", e)

#Eredmények kiírása a ranglistába
def ranglista_kiir(lista):
    try:
        f = open("ranglista.txt","a+",encoding="utf-8")
        for i in lista:
            f.write("\n")
            f.write("{}:{}:{}".format(i.nev,i.nehezseg,i.osszeg))
        f.close()
    except FileNotFoundError as e:
        print("Nem található a fájl (ranglista.txt)",e)

#Kerdesek beolvasása egy kerdes osztályú listát ad vissza
def kerdesek_beolvas():
    try:
        f = open("kerdesek.txt","rt",encoding="utf-8")
        lista =[]
        for sor in f:
            darabok = sor.split("\t")
            adat = jatekvezerles.kerdes_adatok(int(darabok[0]), darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6], darabok[7])
            lista.append(adat)
        f.close()
        return lista
    except FileNotFoundError as e:
        print("Nem található a fájl (kerdesek.txt)", e)




