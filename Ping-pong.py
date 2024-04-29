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
    def update_2(self):
        key_pressed = key.get_pressed()  
        if key_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= 5
        if key_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += 5   

    def update_1(self):
        key_pressed = key.get_pressed()  
        if key_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= 5
        if key_pressed[K_s] and self.rect.y < 350:
            self.rect.y += 5             

window = display.set_mode((700, 500))
display.set_caption("Ping-pong")  
window.fill(LIGHT_BLUE)

clock = time.Clock()

player2 = Player('platform.bmp', 2, 20, 200, 150, 30)
player1 = Player('platform.bmp', 2, 650, 200, 150, 30)
ball = Player('Ball.bmp', 1.5, 100, 100, 45, 45)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True:

        window.fill(LIGHT_BLUE)

        player2.update_2()
        player2.reset()

        player1.update_1()
        player1.reset()

        ball.reset()

        clock.tick(60)  
        display.update()       