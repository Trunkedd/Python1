Kokkejakke = 0
hp = 100
def start():
    hus = input("\nDu har blit invitert til en fest blir du hjemme eller drar du og fester 1/2->")
    if hus == "1":
        hjemme1()
    if hus =="2":
        fester1()

def ja2():
    print("\nDu inviterer Hellstrøm til husset ditt og han offrer og lage mat til deg")
    Hellstrømmatgangster = input("ja eller nei")
    if Hellstrømmatgangster == "ja":
        mat1()
    if Hellstrømmatgangster == "nei":
        mat2()   
def mat1():
    print("Hellstrøm lagde deg noe chili con carne etter du hadde spist alt starter du og sovne") 
    besvim()
def mat2():
    print("\nHellstrøm ble sur og slo deg til og alt går svart")
    besvim()
def hus2():
    print("\nDu er nå hjemme men plutselig PLING Hellstrøm har sendt deg en melding")
    Hellstrømhusetditt = input("\nHei du Kan jeg komme på besøk til deg? ja/nei -> ")
    if Hellstrømhusetditt == "ja":
        ja2()
    if Hellstrømhusetditt == "nei":
        Overlevde()
def ja1():
    print("\nDu gå nummeret ditt til Hellstrøm og dro hjem etter det")
    hus2()
def Overlevde():
    print("\nDu sa nei og gikk og la deg du våknet med fult av meldinger at Hellstrøm hadde blit en Ondskapsfull man og drept noen")
    quit()
def besvim():
    print("\ndu besvimer og vokner i et ondskapfult rom der det er 3 dører")
    dører3 = input("Hvilken dør går du i 1,2 eller 3 ")
    if dører3 == "1":
        dør1()
    if dører3 == "2":
        dør2()
    if dører3 == "3":
        dør3()
def dør1():
    print("\ndu åpner dør 1 og der inne er det 1 slange")
    hp -=12
    print("\ndu løpte tilbake til det første rommet nå har du",hp,"igjen Vær forskitig")
    dører3 = input("Hvilken dør går du i 1,2 eller 3 ")
    if dører3 == "1":
        dør1()
    if dører3 == "2":
        dør2()
    if dører3 == "3":
        dør3()
def dør2():
    print("\ndu går gjennom dør 2 inne der finner du en tv stue med 2 til dører, du hører lyd fra dør 2")
    dører4 = input("hvilken dør går du gjennom 1/2-> ")
    if dører4 == "1":
        dør4()
    if dører4 == "2":
        dør5()
def dør3():
    print("\ndu fant et rom fylt med godteri og så du går tilbake")
    dører3 = input("Hvilken dør går du i 1/2 ")
    if dører3 == "1":
        dør1()
    if dører3 == "2":
        dør2()
def dør4():
    global Kokkejakke
    valg = input("\ndu finner du en garderobe med kokkejakke ta den med eller dra videre ->ja/nei ")
    if valg == "ja":
        Kokkejakke += 1
        fram()
    if valg == "nei":
        fram()
def fram():
    global Kokkejakke
    print("\nDu går framover og ser et gigantisk kjøkken")
    if Kokkejakke == 1:
        print("\nDu er heldig at du tok kokkejakka med deg du går in")
        Valg = input("hva gjør du,gå og lage deg noe mat,spør om hjelp,fortsett videre,velg med 1/2/3 ")
        if Valg == "1":
            print("Du går og skal lage deg litt kake men plutselig kjenner du noen røre deg på skuldra")
            skuldrer = input("Hva gjør du 1 angrip den som er bortideg 2 løp dritt raskt 3 snu deg som en vanlig person ")
            if skuldrer == "1":
                print("du slår dem i fjeset og løper imot utgangen")
                rom3
        if Valg == "2":
            print("Du leter etter noen men finner ingen")
            Ingen = input("Fortsett eller lett videre")
        if Valg == "3":
            print("du fortsetter og gå videre till du kjenner en ta deg i skuldra")
            skuldrer = input("Hva gjør du 1 angrip han som er bortideg 2 løp dritt raskt 3 snu deg som en vanlig person ")
            if skuldrer == "1":
                pass
def rom3():
    gjemsell=input("Du er i et rom med et bord et skap og en dør 1/2/3 ->")
    if gjemsell =="1":
        pass
    if gjemsell =="2":
        pass
    if gjemsell =="3":
        pass
def dør5():
    print("\ninne her finner du en med pose på hodet")
    poseman = input("\nTar du Posen av eller fortsetter du 1/2->")
    if poseman == "\nDu tar av han posen og du ser at han er død":
        print("du fortsetter")
        dør4()
def nei1():
    print("\ndu sier nei til han han sier at det går greit at du ikke gidde han nummeret han inviterer deg til og drikke noe du takker ja")
    print("du drikker det han gidde deg og plutselig")
    besvim()
def går1():
    print("\nDu går til hellstrøm og dere snakker i noen minuter og han hadde det bra så han spurte om nummere ditt ")
    nummeret = input("Får han hellstrøm nummeret ditt eller ikke 1/2-> ")
    if nummeret == "2":
        nei1()
    if nummeret == "1":
        ja1()


def ikke1():
    print("\nDu tenker at du burde respekter Hellstrøms fest og la han være i fred")
    men = input("Han ser deg stire og går mot deg du blir stresset hva gjør du går du mot han eller går du vekk 1/2 ->  ")
    if men == "2":
        besvim()
    if men == "1":
        går1()

def hjemme1():
    print("Du blei hjemme rykter hadde det at selveste Eyvind Hellstrøm var der")
def fester1():
    print("Du gjorde deg klar til festen og dro til festen") 
    kjendis = input("\ner det selveste Hellstrøm går du og snakker med Hellstrøm eller ikke 1/2 -> ")
    if kjendis == "2":
        ikke1()
    if kjendis == "1":
        går1()



start()