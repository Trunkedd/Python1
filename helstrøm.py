import random
Kokkejakke = 0
hp = 100
def start():
    asking = True
    while asking == True:
        hus = input("\nDu har blit invitert til en fest blir du hjemme eller drar du og fester 1/2->")
        if hus == "1" or hus == "2":
            asking = False
        else:
            print("Du skreiv feil skriv 1 eller 2")
    if hus == "1":
        hjemme1()
    elif hus == "2":
        fester1()

   

def ja2():
    print("\nDu inviterer Hellstrøm til husset ditt og han offrer og lage mat til deg")

    asking = True
    while asking == True:                              
        Hellstrømmatgangster = input("ja eller nei").lower()
        if Hellstrømmatgangster.lower() == "ja"or Hellstrømmatgangster.lower() == "nei":
            asking = False  
        else:
            print("Du skreiv feil skriv ja eller nei")
    if Hellstrømmatgangster =="ja":
        mat1()
    if Hellstrømmatgangster =="nei":
        mat2() 
def mat1():
    print("Hellstrøm lagde deg noe chili con carne etter du hadde spist alt starter du og sovne") 
    besvim()
def mat2():
    print("\nHellstrøm ble sur og slo deg til og alt går svart")
    besvim()
def hus2():
    print("\nDu er nå hjemme men plutselig PLING Hellstrøm har sendt deg en melding")
    asking = True
    while asking == True:
        Hellstrømhusetditt = input("\nHei du Kan jeg komme på besøk til deg? ja/nei -> ")
        if Hellstrømhusetditt == "ja" or Hellstrømhusetditt == "nei":
            asking = False
        else:
            print("Du skreiv feil skriv enten ja eller nei ")
    if hus2 == "ja":
        ja2()
    if hus2 == "nei":
        Overlevde()
def ja1():
    print("\nDu gå nummeret ditt til Hellstrøm og dro hjem etter det")
    hus2()
def Overlevde():
    print("\nDu sa nei og gikk og la deg du våknet med fult av meldinger at Hellstrøm hadde blit en Ondskapsfull man og drept noen")
    quit()
def besvim():
    print("\ndu besvimer og vokner i et ondskapfult rom der det er 3 dører")
    asking = True
    while asking == True:
        dører3 = input("Hvilken dør går du i 1,2 eller 3 ")
        if dører3 =="1" or dører3 == "2" or dører3 == "3":
            asking = False
        else:
            print("Du skreiv feil skriv enten 1,2 eller 3")
    if dører3 == "1":
        dør1()
    elif dører3 == "2":
        dør2()
    elif dører3 == "3":
        dør3()
def dør1():
    print("\ndu åpner dør 1 og der inne er det en død apekat")
    print("Du løper tilbake")
    dører3 = input("Hvilken dør går du i 1,2 eller 3 ")
    if dører3 == "1":
        dør1()
    if dører3 == "2":
        dør2()
    if dører3 == "3":
        dør3()
def dør2():
    print("\ndu går gjennom dør 2 inne der finner du en tv stue med 2 til dører, du hører lyd fra dør 2")
    asking = True
    while asking == True:
        dører4 = input("hvilken dør går du gjennom 1/2-> ")
        if dører4 == "1" or dører4 == "2":
            asking = False
        else:
            print("du skreiv feil skriv enten 1 eller 2")
        if dører4 == "1":
            dør4()
        elif dører4 == "2":
            dør5()
def dør3():
    print("\ndu fant et rom fylt med godteri og så du går tilbake")
    asking = True
    while asking == True:
        dører3 = input("Hvilken dør går du i 1/2 ")
        if dører3 =="1" or dører3 == "2":
            asking = False
        else:
            print("Du skreiv feil prøv 1 eller 2")
        if dører3 == "1":
            dør1()
        elif dører3 == "2":
            dør2()
def dør4():
    global Kokkejakke
    asking = True
    while asking == True:
        valg = input("\ndu finner du en garderobe med kokkejakke ta den med eller dra videre ->ja/nei ")
        if valg == "ja" or valg == "nei":
            asking=False
        else:
            print("Du må enten skrive ja eller nei husk liten bokstav")
        if valg == "ja":
            Kokkejakke += 1
            fram()
        elif valg == "nei":
            fram()
def fram():
    global Kokkejakke
    print("\nDu går framover og ser et gigantisk kjøkken")
    if Kokkejakke == 1:
        print("\nDu er heldig at du tok kokkejakka med deg du går in")
        asking = True
        while asking == True:
            Valg = input("hva gjør du,gå og lage deg noe mat,spør om hjelp,fortsett videre,velg med 1/2/3 ")
            if Valg =="1" or Valg =="2" or Valg =="3":
                asking = False
            else:
                print("Du skreiv feil skriv enten 1 , 2 , 3")
            if Valg == "1":
                print("Du går og skal lage deg litt kake men plutselig kjenner du noen røre deg på skuldra")
                asking = True
                while asking == True:
                    skuldrer = input("Hva gjør du 1 angrip den som er bortideg 2 løp dritt raskt 3 snu deg som en vanlig person ")
                    if skuldrer == "1" or skuldrer == "2" or skuldrer == "3":
                        asking = False
                    else:
                        print("du skreiv feil skriv 1 2 eller 3")
                    if skuldrer == "1":
                        print("du slår dem i fjeset og løper imot utgangen")
                        rom8()
                    elif skuldrer == "2":
                        print("Du løper raskt som bare faen")
                        rom8()
                    elif skuldrer == "3":
                        print("du snur deg og ser en han sier at Hellstrøm venter på deg")
                        print("han følger deg til et rom der det står Hellstrøm sin private kamprom")
                        Kamp()
                if Valg == "2":
                    print("Du leter etter noen men finner ingen")
                    asking = True
                    while asking == True:
                        Ingen = input("Fortsett eller lett videre 1/2 ->")
                        if Ingen == "1" or Ingen == "3":
                            asking = False
                        else:
                            print("Du skreiv feil skriv enten 1 eller 2")
                        if Ingen == "1":
                            print("Du fortsetter videre ")
                            rom8()
                        elif Ingen == "2":
                            print ("du fortsetter og gå til du kjenner noen ta deg i skulderen")
                            asking = True
                            while asking == True:
                                skuldrer = input("Hva gjør du 1 angrip den som er bortideg 2 løp dritt raskt 3 snu deg som en vanlig person ")
                                if skuldrer == "1" or skuldrer == "2" or skuldrer == "3":
                                    asking = False
                                else:
                                    print("Du skreiv feil velg enten 1 , 2 eller 3")
                            if skuldrer == "1":
                                print("du slår dem i fjeset og løper imot utgangen")
                                rom8()
                            elif skuldrer == "2":
                                print("Du løper raskt som bare faen")
                                rom8()
                            elif skuldrer == "3":
                                print("du snur deg og ser en han sier at Hellstrøm venter på deg")
                                print("han følger deg til et rom der det står Hellstrøm sin private kamprom")
                                Kamp()

        if Valg == "3":
            print("du fortsetter og gå videre till du kjenner en ta deg i skuldra")
            asking = True
        while asking == True:
            skuldrer = input("Hva gjør du 1 angrip den som er bortideg 2 løp dritt raskt 3 snu deg som en vanlig person ")
            if skuldrer == "1" or skuldrer == "2" or skuldrer == "3":
                asking = False
            else:
                print("Du skreiv feil velg enten 1 , 2 eller 3")
        if skuldrer == "1":
            print("du slår dem i fjeset og løper imot utgangen")
            rom8()
        elif skuldrer == "2":
            print("Du løper raskt som bare faen")
            rom8()
        elif skuldrer == "3":
            print("du snur deg og ser en han sier at Hellstrøm venter på deg")
            print("han følger deg til et rom der det står Hellstrøm sin private kamprom")
            Kamp()
    if Kokkejakke >= 0:
        print("du ser et stort kjøkken som du løper igjennom en man ser deg og løper etter")
        rom8()
def rom8():
    asking = True
    while asking == True:
        gjemsell=input("Du er i et rom med et bord et skap og en dør 1/2/3 ->")
        if gjemsell =="1" or gjemsell =="2" or gjemsell =="3":
            asking = False
        else:
            print("Du skreiv feil prøv 1,2,3")
        if gjemsell =="1":
                print("du løper under bordet og holder pusten")
                input()
                tilfeldig = random.randint(1,10)

                if tilfeldig <= 3: # mindre enn 3
                    print("du ble funnet\n")
                    start()
                elif tilfeldig > 3: # mer enn 3
                    print("han gikk forby deg\n")
                    Boss=input("Du ser et rom der det står 'Hellstrøm Sin private Kamprom'Går du in ja/nei->")
                    if Boss == "ja":
                        Kamp()

                    if Boss == "nei":
                        print("Du finner ingen utgang ser ut som du må gå til Hellstrøm sin private kamprom")
                        Kamp()
                
        elif gjemsell =="2":
                print("du løper under bordet og holder pusten")
                input()
                tilfeldig = random.randint(1,10)
            
                if tilfeldig <= 3: # mindre enn 3
                    print("du ble funnet\n")
                    start()
                elif tilfeldig > 3: # mer enn 3
                    print("han gikk forby deg\n")
                Boss=input("Du ser et rom der det står 'Hellstrøm Sin private Kamprom'Går du in ja/nei->")
                if Boss == "ja":
                    Kamp()

                if Boss == "nei":
                    print("Du finner ingen utgang ser ut som du må gå til Hellstrøm sin private kamprom")
                    Kamp()
        
        elif gjemsell =="3":
            print("du løper under bordet og holder pusten")
            input()
            tilfeldig = random.randint(1,10)
        
            if tilfeldig >= 3: # mindre enn 3
                print("du ble funnet\n")
                start()
            elif tilfeldig < 3: # mer enn 3
                print("han gikk forby deg\n")
                Boss=input("Du ser et rom der det står 'Hellstrøm Sin private Kamprom'Går du in ja/nei->")
                if Boss == "ja":
                    Kamp()

                if Boss == "nei":
                    print("Du finner ingen utgang ser ut som du må gå til Hellstrøm sin private kamprom")
                    Kamp()
def Kamp():
    global hp
    print("Du Ser HELLSTRØM! ")
    boss_hp = 75
    fighting = True
    while fighting:
        print(f"\nDu har {hp} liv.")
        print(f"Bossen har {boss_hp} hp.")
        dodge_chance = 0 # tilbakestill dodge chance hver runde
        valg = input("\nA: Angrip B: Dodge -> ")
        if valg == "A":
            dmg = random.randint(1,10)
            boss_hp -= dmg
            print(f"Du slo Hellstrøm for {dmg} dmg.")
 
        elif valg == "B":
            dodge_chance = random.randint(1,10)
 
        
        
        if boss_hp < 0:
            print("Du klarte det Hellstrøm døde du vant")
            victory()
 
        else: # boss attack
            if dodge_chance < 2:
                boss_dmg = random.randint(5,10)
                hp -= boss_dmg
                print(f"Hellstrøm slo deg for {boss_dmg} dmg.")
        if hp < 1:
            print("Du er død")
            game_over()
      
def game_over():
    print("du tapte mot hellstrøm ")
    start()
 
def victory():
    print("du klarte det!")
    creds()
def creds():
    print("Du vant gratis men nå hva")
    print("enkelt prøv igjen")
    igjen = input("vil du prøve igjen ja/nei")
    if igjen == "ja":
        start()
    if igjen == "nei":
        print("lykke til")
def dør5():
    print("\ninne her finner du en med pose på hodet")
    poseman = input("\nTar du Posen av eller fortsetter du 1/2->")
    if poseman == "1":
        print("\nDu tar av han posen og du ser at han er død")
        print("du fortsetter")
        dør4()
    if poseman == "2":
        print("du forlater han og fortsetter")
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
    start()
def fester1():
    print("Du gjorde deg klar til festen og dro til festen") 
    kjendis = input("\ner det selveste Hellstrøm går du og snakker med Hellstrøm eller ikke 1/2 -> ")
    if kjendis == "2":
        ikke1()
    if kjendis == "1":
        går1()



start()