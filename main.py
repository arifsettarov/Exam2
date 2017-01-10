import pygame
from file import *
from pygame import *

WinGeometry = (800, 650)



def main():
    init()
    score = 0
    reload = up = down = shoot = False
    heroy = 50
    window = display.set_mode(WinGeometry)
    display.set_caption("Ball shooter")

    ball = Ball(600,500,"images/ball.png")


    bullet = Bullet("images/bullet.png")
    heroimage = pygame.image.load("images/shooter2.png")
    hero = heroimage.copy()

    screen = pygame.image.load("images/brick_red.png")
    inf = Surface((800,100))

    font = pygame.font.Font(None, 50)


    group = sprite.Group()
    group.add(ball)
    group.add(bullet)

    while 1:

        for e in event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down=  True
            if e.type == KEYDOWN and e.key == K_SPACE and not reload:
                shoot=  True
                bullet.rect.x = 100
                bullet.rect.y = heroy + 65
            if e.type ==  KEYUP:
                if e.key == K_UP:
                    up = False
                if e.key == K_DOWN:
                    down = False
        heroy = move_hero(up,down,heroy)
        collide = sprite.collide_rect(bullet,ball)

        if shoot:
            reload = True
            bullet.rect.x  +=10
            if bullet.rect.x >= 800:
                shoot = False
                reload = False
                bullet.rect.x = -10


        if ball.rect.y < -50:
            ball.rect.y = 650
            ball.speed, ball.rect.x = ball.move_ball()
            score = 0

        if collide:
            score +=1
            ball.rect.y = 650
            ball.speed, ball.rect.x = ball.move_ball()




        screen.blit(hero, (10,heroy))
        inf.blit(font.render("CЧЕТ: " + str(score), True, [255, 0, 0]), (25, 10))
        group.draw(screen)
        group.update()
        window.blit(screen, (0, 0))
        window.blit(inf, (0, 600))

        screen = pygame.image.load("images/brick_red.png")
        inf.fill([0,0,255])
        display.update()

def move_hero(up,down, heroy):
    if heroy >0:
        if up:
            heroy = heroy - 5
    if heroy <450:
        if down:
            heroy = heroy + 5
    return heroy


if __name__ == "__main__":
    main()