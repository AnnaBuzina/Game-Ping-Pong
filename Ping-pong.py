from pygame import *

game = True
finish = False
LIGHT_BLUE = (200, 255, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, play_image, speed, x, y, h, l):
        super(). __init__()
        self.h = h
        self.l = l
        self.image = transform.scale(image.load(play_image), (l, h))
        self.speed = speed
        self.rect = self.image.get_rect()  #создание прямоугольной подложки
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()  
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if key_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += 5

window = display.set_mode((700, 500))
display.set_caption("Ping-pong")  
window.fill(LIGHT_BLUE)

clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True:
        


        clock.tick(60)  
        display.update()       
