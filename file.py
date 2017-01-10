from pygame import *
import random
class Bullet(sprite.Sprite):
    def __init__(self, file):
        sprite.Sprite.__init__(self)

        self.image = image.load(file)
        self.rect = self.image.get_rect()
        self.rect.x = -10
        self.rect.y =0

    def move(self):
        self.rect.x +=5


class Ball(sprite.Sprite):
    def __init__(self, x,y,file):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image.load(file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed, self.rect.x = self.move_ball()
    def move_ball(self):
        ball_speed = random.randint(2,7)
        ball_x = random.randrange(200,700,50)
        return ball_speed,ball_x
    def update(self):
            self.rect.y -= self.speed

