
hp = 100
def start():
    hus = input("Du har blit invitert til en fest blir du hjemme eller drar du og fester ")
    if hus == "hjemme":
        hjemme1()
    if hus =="fester":
        fester1()

def ja2():
    print("Du inviterer Hellstrøm til husset ditt og han offrer og lage mat til deg")
    Hellstrømmatgangster = input("ja eller nei")
    if Hellstrømmatgangster == "ja":
        mat1
    if Hellstrømmatgangster == "nei":
        mat2    
def mat1():
    print("Hellstrøm lagde deg noe chili con carne men plutselig starter du og sovne") 
    besvim
def mat2():
    print("Hellstrøm ble sur og slo deg til og alt går svart")
    besvim
def hus2():
    print("Du er nå hjemme men plutselig PLING Hellstrøm har sendt deg en melding")
    Hellstrømhusetditt = input("Hei du Kan jeg komme på besøk til deg? ja/nei -> ")
    if Hellstrømhusetditt == "ja":
        ja2
    if Hellstrømhusetditt == "nei":
        Overlevde
def ja1():
    print("Du gå nummeret ditt til Hellstrøm og dro hjem etter det")
    hus2
def Overlevde():
    print("Du sa nei og gikk og la deg du våknet med fult av meldinger at Hellstrøm hadde blit en Ondskapsfull man og drept noen")
    quit
def besvim():
    print("du besvimer og vokner i et ondskapfult rom der det er 3 dører")
    dører3 = input("Hvilken dør går du i 1,2 eller 3")
    if dører3 == "1":
        dør1
    if dører3 == "2":
        dør2
    if dører3 == "3":
        dør3
def dør1():
    print("du åpner dør 1 og der inne er det 1 slange")
    hp -=12
    print("du løpte tilbake til det første rommet nå har du",hp,"igjen Vær forskitig")
    dører3 = input("Hvilken dør går du i 1,2 eller 3")
    if dører3 == "1":
        dør1
    if dører3 == "2":
        dør2
    if dører3 == "3":
        dør3
def nei1():
    print("du sier nei til han han sier at det går greit at du ikke gidde han nummeret han inviterer deg til og drikke noe du takker ja")

def går1():
    print("Du går til hellstrøm og dere snakker i noen minuter og han hadde det bra så han spurte om nummere ditt ")
    nummeret = input("Får han hellstrøm nummeret ditt eller nope ")
    if nummeret == "nope":
        nei1()
    if nummeret == "ja":
        ja1


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
    if kjendis == "går":
        går1()



start()