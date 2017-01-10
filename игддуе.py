import sys, pygame
pygame.init()
size = width, height = 800, 800
speed = [1, -1]
black = 0, 0, 0
level = [
    "--------------------------------------------------------------------------------",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "-                                                                              -",
    "--------------------------------------------------------------------------------"]
stone = []

def main():

    screen = pygame.display.set_mode(size)
    win = pygame.Surface(size)

    ball = pygame.Surface((10,5))
    ball.fill(pygame.Color("#ffffff"))

    ballrect = ball.get_rect()
    mousepos = [0,0]
    x = y =0
    for row in level:
        for col in row:
            if col == "-":
                pl = pygame.Surface((10,10))

                pl.fill(pygame.Color("#c231dc"))
                stone.append(pl)
                win.blit(pl,(x,y))
            x+=10
        y+=10
        x =0

    done = False
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                done = True
                print(ballrect)

        if done:
            speed = calc(ballrect, mousepos)
            ballrect = ballrect.move(speed)
            #if ballrect.left < 0 or ballrect.right > width:
             #   speed[0] = -speed[0]
            #if ballrect.top < 0 or ballrect.bottom > height:
            #    speed[1] = -speed[1]



        win.blit(ball, ballrect)
        screen.blit(win,(0,0))
        pygame.display.flip()

def calc(ballrect, mousepos):
    stx, sty = ballrect[0],ballrect[1]
    mx,my = mousepos[0],mousepos[1]
    x,y = mx-stx,my-sty
    print(x,y)
    if x > y:
        movey = 2
    if x < y:
        movey = 0
    if x == y:
        movey =1
    # if sty > my:
    #     movey = -1
    # elif sty == my:
    #     movey = 0
    # else:
    #     movey = 1
    # if stx > mx:
    #     movex = -1
    # elif stx == mx:
    #     movex = 0
    # else:
    #     movex = 1
    # if y == 0:
        # y = 1
    movex = x / y

    move = [movex,movey]
    #print(move)
    return move
if __name__ == "__main__":
    main()