import pygame
from pygame import font

pygame.init()

WINDOW_SIZE = (700, 500)
FPS = 60
game = True
#BACKGROUND_IMAGE = "background.jpg"

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill((123,123,123))
pygame.display.set_caption("PING PONG")
clock = pygame.time.Clock()
#background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), WINDOW_SIZE)

class DefaultSprite():

    def __init__(self, x, y, width, height, filename):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.filename = filename
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket1(DefaultSprite):
    def __init__(self, x, y, width, height, filename, speed):
        super().__init__(x, y, width, height, filename)
        self.speed = speed
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

        
class Ball(DefaultSprite):

    def __init__(self, x, y, width, height, filename, speed):
        super().__init__(x, y, width, height, filename)
        self.speed = speed
        self.rotate = 60
    
    def move(self):

        if self.rotate == 60:
            self.rect.x += self.speed
            self.rect.y += self.speed
        elif self.rotate == 240:
            self.rect.x -= self.speed
            self.rect.y -= self.speed

        if self.rect.y >= WINDOW_SIZE[1]:
            self.rotate = 240

        if self.rect.y <= 0:
            self.rotate = 60

ball = Ball(0, 0, 50, 50, "ball.jpg", 1)
rocket1 = Rocket1(10,10,100,100, 'rocket1.png', 3)
rocket2 = Rocket1(580,10,200,200, 'rocket2.png', 3)
pygame.font.init()
font = font.Font(None, 35)
lose1 = font.render('player 1 lost soul', True, (180, 0, 0))
lose2 = font.render('player 2 lost soul', True, (180, 0, 0))
game = True
finish = False
while game:
    clock.tick(FPS)

    ball.update()
    rocket1.update()
    rocket2.update()
    rocket2.update_r()
    keys = pygame.key.get_pressed()
    ball.move()
    rocket1.update_l()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not finish:
        window.fill((200, 255, 255))
        ball.rect.x += 3
        ball.rect.y += 3
    if ball.rect.y > 500-50 or ball.rect.y<0:
        3*1
    if ball.rect.x<0:
        finish = True
        window.blit(lose1, (200, 200))
        
    ball.update()
    rocket1.update()
    rocket2.update()
    pygame.display.update()