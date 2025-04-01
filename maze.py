#создай игру "Лабиринт"!
from pygame import *

width = 700
height = 500
window = display.set_mode((700,500))
display.set_caption("Лабириииииииииинт")

backdround = transform.scale(image.load("background.jpg"),(700,500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def run(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def run(self):
        if self.rect.x <= 500:
            self.direction = 'right'
        if self.rect.x >= width - 40:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, width, height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

hero = Player("hero.png", 5, height - 80, 10)
enemy = Enemy("cyborg.png", width - 80, 280, 10)
gold = GameSprite("treasure.png", width - 120, height - 80, 0)

w1 = Wall(187, 5, 114, 100, 20, 450, 10)
w2 = Wall(187, 5, 114, 100, 480, 350, 10)
w3 = Wall(187, 5, 114, 100, 20, 10, 380)
w4 = Wall(187, 5, 114, 200, 150, 10, 330)
w5 = Wall(187, 5, 114, 300, 20, 10, 380)
w6 = Wall(187, 5, 114, 450, 150, 10, 340)
w7 = Wall(187, 5, 114, 400, 150, 150, 10)

game = True
finish = False
FPS = 60
clock = time.Clock()

font.init()
font = font.SysFont('Arial', 70)
win = font.render("Самый умный что-ли?", True, (0,0,0))
lose = font.render("Самый тупой что-ли?", True, (0,0,0))

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(backdround,(0,0))
        hero.reset()
        enemy.reset()
        gold.reset()

        hero.run()
        enemy.run()

        w1.reset()
        w2.reset()
        w3.reset()
        w4.reset()
        w5.reset()
        w6.reset()
        w7.reset()

    if sprite.collide_rect(hero, gold):
        finish = True
        window.blit(win,(200,200))
        money.play()

    if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or sprite.collide_rect(hero, w6) or sprite.collide_rect(hero, w7):
        finish = True
        window.blit(lose,(200,200))
        kick.play()
        
    display.update()
    clock.tick(FPS)
