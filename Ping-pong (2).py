from pygame import *
font.init()

def section(player, ball):
    height = player.rect.bottom - player.rect.top
    if ball.rect.centery <= player.rect.y + height * 1/8:
        return -45
    elif ball.rect.centery <= player.rect.y + height * 2/8:
        return -30 
    elif ball.rect.centery <= player.rect.y + height * 3/8:
        return -15  
    elif ball.rect.centery <= player.rect.y + height * 4/8:
        return 0     
    elif ball.rect.centery <= player.rect.y + height * 5/8:
        return 0    
    elif ball.rect.centery <= player.rect.y + height * 6/8:
        return 15
    elif ball.rect.centery <= player.rect.y + height * 7/8:
        return 30
    else:
        return 45              

score_1 = 0
score_2 = 0
speed_x = 5.5
speed_y = 5.5
game = True
finish = False
LIGHT_BLUE = (200, 255, 255)
RED = (255, 9, 23)
GREEN = (0, 255, 0)

font = font.SysFont('Arial', 30)

win2 = font.render('Поражение 1 игрока!', True, RED)
win1 = font.render('Поражение 2 игрока!', True, RED)
no_win = font.render('Ничья!', True, RED)
score_text_1 = font.render('Счёт: '+ str(score_1), 1, GREEN)
score_text_2 = font.render('Счёт: '+ str(score_2), 1, GREEN)

class GameSprite(sprite.Sprite):
    def __init__(self, play_image, speed, x, y, h, l):
        super(). __init__()
        self.h = h
        self.l = l
        self.image = transform.scale(image.load(play_image), (l, h))
        self.speed = speed
        self.rect = self.image.get_rect()
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

class Ball(GameSprite):
    def __init__(self, play_image, speed, x, y, h, l):
        super().__init__(play_image, speed, x, y, h, l)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y   
    def hit(self, player):
        if sprite.collide_rect(self, player):
            angle = section(player, self)
            if abs(angle) == 45:
                self.speed_x = 5.5
                self.speed_y = 5.5
            if abs(angle) == 30:
                self.speed_x = 5.5
                self.speed_y = 5.5
            if abs(angle) == 15:
                self.speed_x = 5.5
                self.speed_y = 5.5 
            if abs(angle) == 0:
                self.speed_x = 5.5
                self.speed_y = 5.5  
            if angle < 0:
                self.speed_y *= -1
            if self.rect.x > 500/2:
                self.speed_x *= -1                

window = display.set_mode((700, 500))
display.set_caption("Ping-pong")  
window.fill(LIGHT_BLUE)

clock = time.Clock()

player1 = Player('platform.png', 0.3, 3, 200, 150, 30)
player2 = Player('platform.png', 0.3, 665, 200, 150, 30)
ball = Ball('Ball.png', 2, 300, 200, 45, 45)

#Обратный отсчёт
counter, text = 100, '100'.rjust(3)
time.set_timer(USEREVENT, 1000)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

        #обратный отсчёт
        if e.type == USEREVENT: 
            counter -= 1
            if counter > 0:
                text = str(counter).rjust(3)    
            else: 
                if score_1 == score_2: 
                    'Ничья!' 

    if finish != True:
        window.fill(LIGHT_BLUE)

        window.blit(font.render(text, True, RED), (300, 30))
        window.blit(score_text_1, (15, 15))
        window.blit(score_text_2, (595, 15))

        player1.update_1()
        player1.reset()

        player2.update_2()
        player2.reset()

        ball.update()
        ball.reset()

        if ball.rect.y > 455:
            ball.speed_y *= -1

        if ball.rect.y <= 0:
            ball.speed_y = abs(ball.speed_y)

        ball.hit(player1)
        ball.hit(player2)

        # Условие проигрыша
        if ball.rect.x > 700:
            score_1 += 1
            score_text_1 = font.render('Счёт: '+ str(score_1), 1, GREEN)
            window.blit(score_text_1, (15, 15))
            ball.kill()
            player2.kill()
            player1.kill()
            player1 = Player('platform.png', 2, 3, 200, 150, 30)
            player2 = Player('platform.png', 2, 665, 200, 150, 30)
            ball = Ball('Ball.png', 1.5, 300, 200, 45, 45)

            if score_1 >= 3:
                window.blit(win1, (200, 200))
                finish = True
            
        elif ball.rect.x < -50:
            score_2 += 1
            score_text_2 = font.render('Счёт: '+ str(score_2), 1, GREEN)
            window.blit(score_text_2, (595, 15))
            ball.kill()
            player2.kill()
            player1.kill()
            player1 = Player('platform.png', 2, 3, 200, 150, 30)
            player2 = Player('platform.png', 2, 665, 200, 150, 30)
            ball = Ball('Ball.png', 1.5, 300, 200, 45, 45)

            if score_2 >= 3:
                window.blit(win2, (200, 200))
                finish = True

        elif counter == 0:
            if score_1 > score_2:
                window.blit(win1, (200, 200))
                finish = True
            elif score_2 > score_1:
                window.blit(win2, (200, 200))
                finish = True    
            elif score_1 == score_2:
                window.blit(no_win, (300, 200))
                finish = True

    clock.tick(60)  
    display.update()       