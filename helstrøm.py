def besvim():
    "du besvimer"
def går1():
    print("Du går til hellstrøm og dere snakker i noen minuter og han hade det bra så han spurte om nummere ditt ")
    nummeret = input("Får han hellstrøm nummeret ditt eller nope")
def nei1():
    print("du sier nei til han han sier at det går greit at")
def ikke1():
    print("Du tenker at du burde respekter Hellstrøms fest og la han være i fred")
    men = input("Han ser deg stire og går mot deg du blir stresset hva gjør du går du mot han eller går du vekk ")
    if men == "vekk":
        besvim()
    if men == "går":
        går1()

def hjemme1():
    print("Du blei hjemme rykter hadde det at selveste Eyvind Hellstrøm var der")
def fester1():
    print("Du gjorde deg klar til festen og dro til festen") 
    kjendis = input("er det selveste Hellstrøm går du og snakker med Hellstrøm eller ikke ")
    if kjendis == "ikke":
        ikke1()
    if kjendis == "snakker":
        går1


def start():
    hus = input("Du har blit invitert til en fest blir du hjemme eller drar du og fester ")
    if hus == "hjemme":
        hjemme1()
    if hus =="fester":
        fester1()


start()