hp = 100

def rom_1():
    print("du er i et rom og du må enten")
    valg = input("Velge rom 2 med A,eller rom 2 med B")
    if valg =="A":
        rom_2()# starter rom 2
        if valg =="B":
            rom_3()# start rom 3


def rom_2():
    global hp
    print("Her var det en løve som angriper deg")
    hp -= 90
    print("Du har nå", hp,"liv igjen")

    if hp <= 0:
        game_over()

    rom_1()

def rom_3():
    print("du er i rom 3 så du vant ikke sant eller vil du tilbake til rom 1")

def game_over():
    print("du døde")
    exit()

rom_1()