import pygame as pg

pg.init()

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

screen = pg.display.set_mode((800,600))

clock = pg.time.Clock()


pos_x = 100
pos_y = 100
i = 0
playing = True
while playing:
    clock.tick(60)
    print("FPS:", i)
    print("playing")
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False 
            pg.quit()

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pos_y -= 5
    if keys[pg.K_s]:
        pos_y += 5
    if keys[pg.K_a]:
        pos_x -= 5
    if keys[pg.K_d]:
        pos_x += 5
    if pos_x > 800:
        pos_x = 800
    if pos_x > 0:
        pos_x = 0
    if pos_y > 600:
        pos_y = 600
    if pos_y > 0:
        pos_y = 0





    screen.fill(white)
    play_box = pg.Rect(pos_x,pos_y, 100,100)
    
    

    pg.draw.rect(screen,red,play_box)

    pg.display.update()