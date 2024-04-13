from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

back = (234,78,101)

window = display.set_mode((600,500))
window.fill(back)

game = True
finish = False
FPS = 60

racket1 = Player('',30,200,5,50,35)

racket1 = Player('',560,200,5,35)

ball = GameSprite('',250,200,30,30,10)

font.init()
font = font.Font(None,40)
lose1 = font.render('игрок 1 лошара', True, (79,190,233))
lose2 = font.render('игрок 2 лошара', True, (190,220,111))

win1 = font.render('игрок 1 победа', True, (79,190,233))
win2 = font.render('игрок 2 победа', True, (190,220,111))

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    
    if finish != True:
        window.fill(back)
        racket1.racket_l()
        racket2.update_r()

        ball.rect.x = speed_x
        ball.rect.y = speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > 465 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,200,210)
        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, 200,210)
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
        







