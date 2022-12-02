# my final main file
# sources cited
# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
# from platform import platform
# here is some code that might fix your problem...

import pygame as pg
from pygame.sprite import Sprite
import random
# from random import randint



vec = pg.math.Vector2

# game settings 
WIDTH = 1280
HEIGHT = 720
FPS = 30


# player settings
PLAYER_GRAVITY = 3

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
TEAL = (177, 255, 255)

# score
SCORE = 5

# difficulty
DIFFICULTY = int(input("Difficulty: 0 being the easiest, 4 being the hardest: "))

# amount of enemies killed
MOBS = 0
# to get rid of the hint about the space bar - press space
HINT = 0

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# sprites...
class Player(Sprite):
    def __init__(self):
        # defines player sprite parameters
        Sprite.__init__(self)
        if DIFFICULTY == 4:
            self.image = pg.Surface((50, 50))
        if DIFFICULTY == 3:
            self.image = pg.Surface((75, 75))
        if DIFFICULTY == 2:
            self.image = pg.Surface((100,100))
        if DIFFICULTY == 1:   
            self.image = pg.Surface((125,125))
        if DIFFICULTY == 0:  
            self.image = pg.Surface((150,150))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
 

        
        
         


    # what happens when a key gets pressed: horizontal movement
    def controls(self):
        global HINT
        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            self.pos = vec(WIDTH / 2, HEIGHT / 2) # resets position
        if keys[pg.K_LEFT]:
            self.acc.x = -2.5
            # print(self.vel)
        if keys[pg.K_RIGHT]:
            self.acc.x = 2.5
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]: # floats while space is held in the direction the player was moving, still has friction
            self.acc.y = -1.5
            if hits:
                    player.rect.top = hits[0].rect.bottom
                    # self.acc.y = 0
                    self.vel.y = 100
           
            # if self.vel.y >= 10:
            #     self.acc.y = 1
            HINT += 1    
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -40
    # updating all movement and acceleration and gravity
    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        self.controls()
        # hits = pg.sprite.spritecollide(self, all_platforms, False)
        # if hits:
        #     print("collision")
        # friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos


class Sweep(Sprite):
    def __init__(sweep, x, y, w, h):
        # defines sweep sprite parameters
        Sprite.__init__(sweep)
        player.rect.x = x
        player.rect.y = y
        sweep.w = w
        sweep.h = h
        sweep.image = pg.Surface((300, 300))
        sweep.image.fill(TEAL)
        sweep.rect = sweep.image.get_rect()
        sweep.rect.center = (WIDTH / 2, HEIGHT / 2)
        sweep.pos = vec(WIDTH / 2, HEIGHT / 2)
        sweep.vel = vec(0,0)
        sweep.acc = vec(0,0)
        
def blast(sweep):
    keys = pg.key.get_pressed()
    if keys[pg.K_KP_ENTER]:
        sweep.pos = vec(player.x, player.y)
        color = TEAL
        s = Sweep(x, y, color, 150, 150)
        all_sprites.add(s)
        sweep.add(s)
        print("sweep")
def update(sweep):
    sweep.blast()




# creates platform class
# platforms is sublass of sprite
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

'''
class Elevator(Platform(Sprite)):
    def __init__(self, lift):
        Platform.__init__(self)
        Sprite.__init__(self)
        self.lift = lift
        lift = self.vel.y
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
'''
# scrapped elevator idea        

class Enemy(Sprite):
    def __init__(self, x, y, color, w, h):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        
        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
enemies = pg.sprite.Group()
sweep = pg.sprite.Group()

# instantiate the player class
player = Player()
# enemy1 = Enemy(100, 200, RED, 25, 25)
# plat = Platform(x, y, width, height)
plat = Platform(WIDTH/2, HEIGHT/2 + 100, 100, 10)
plat2 = Platform(0 - WIDTH / 2, HEIGHT/1.05, WIDTH * 2, 35) # Bottom
plat3 = Platform(50, 200, 200, 10)
plat4 = Platform(800, 375, 200, 10)
plat5 = Platform(0 - WIDTH / 2, 0, WIDTH * 2, 10) # Top 
# elevator = Elevator(0, 0, 50, 100, 10)
# sweep
colors = [WHITE, RED, GREEN, BLUE]


for i in range(1):
    x = random.randint(0, WIDTH)
    y = random.randint(15, HEIGHT - 40)
    movex = random.randint(-2, 2)
    movey = random.randint(-2, 2)
    color = random.choice(colors)
    e = Enemy(x, y, color, 25, 25)
    all_sprites.add(e)
    enemies.add(e)
    print(e)
# creates the first enemy 
# source: Andrew


# add player to all sprites group
all_sprites.add(player, plat, plat2, plat3, plat4, plat5)
all_platforms.add(plat, plat2, plat3, plat4, plat5)


# Timer
FRAME = 1
TIMER = 0
RAMP = 150
# ramp sets the time in ticks when the score will decrease

# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    
    


    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.jump()
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()
    all_platforms.update()
    sweep.update()
    hits = pg.sprite.spritecollide(player, all_platforms, False)
    kill = pg.sprite.spritecollide(player, enemies, True)
    if kill and SCORE < 15:
        SCORE += 1
        print("Kill")
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        MOBS += 1
    if kill and 15 <= SCORE <= 25: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        MOBS += 1
    if kill and 25 <= SCORE <= 35: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)    
        MOBS += 1
    if kill and 35 <= SCORE <= 45: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)  
        MOBS += 1
    if kill and 45 <= SCORE <= 55: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)    
        MOBS += 1          
    # every time a point threshold is crossed, even if it isn't the first time, add another enemy
    '''
    displace = pg.sprite.spritecollide(plat or plat2 or plat3 or plat4 or plat5, enemies, True)
    if displace: 
        print("Displace")
        x = random.randint(0, WIDTH)
        y = random.randint(40, HEIGHT)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
    '''
    # supposed to move enemies if they spawn inside a platform. Doesn't work. Changed parameters of enemy spawns to fix

    if player.vel.y > 0:
        if hits:
            player.pos.y = hits[0].rect.top
            player.vel.y = 0
            # negative vel means player is moving down, so when it hits a platform it needs to rest
    if player.vel.y < 0:
        if hits:
            player.rect.top = hits[0].rect.bottom
            player.vel.y = 10
            # positive vel means player is moving up, so it should be set to the bottom and make the velocity from negative to positive
    # sometimes, with enough intial velocity, the player will phase through from the bottom
    # this is because the vel.y will momentarily be zero because of the math
    # if I could use derivatives to determine the direction of the velocity, I could fix the lack of collision issues
    # currently, there is no distinction between if vel.y = 0 is from the top or bottom

    

    if FRAME % RAMP == 0 and SCORE < 15:
        SCORE -= 2
    if FRAME % RAMP == 0 and 15 < SCORE <= 25:
        SCORE -= 5
    if FRAME % RAMP == 0 and 25 < SCORE <= 35:
        SCORE -= 10
    if FRAME % RAMP == 0 and 35 < SCORE <= 45:
        SCORE -= 15    
    # if FRAME % RAMP == 0 and 45 < SCORE <= 55:
    #     SCORE -= 20
    if FRAME % RAMP == 0 and 45 < SCORE <= 55: # Instead of
        RAMP = 90
        SCORE -= 10
    # establishes the point thresholds and how many points are lost per 150 ticks
    
    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    
    # draw_text("Enemies: " + str(i in range(e)), 30, WHITE, WIDTH / 4, 70)
    draw_text("Kills: " + str(MOBS), 30, WHITE, WIDTH / 4, 50)
    draw_text("POINTS: " + str(SCORE), 24, WHITE, WIDTH / 2, HEIGHT / 20)
    draw_text("Timer: " + str(int(TIMER)), 24, WHITE, WIDTH / 2, HEIGHT / 10)
    draw_text("CONTROLS", 24, WHITE, WIDTH - 150, 10)
    draw_text("Arrow keys:       Movement", 24, WHITE, WIDTH - 175, 30)   
    draw_text("R:       Reset Position", 24, WHITE, WIDTH - 116, 55)
    if HINT == 0:
        draw_text("Stuck? Question: Where might gravity not be an issue?", 24, WHITE, 500, 500)
    if HINT != 0:
        draw_text("Space:       Float", 24, WHITE, WIDTH - 176, 80)
    if SCORE >= 56:
        draw_text("You won!", 50, WHITE, WIDTH / 2, HEIGHT / 2)  
    if SCORE < 0:
        draw_text("Surprise! No stakes!", 30, WHITE, WIDTH / 2, HEIGHT / 2)
    # draws on-screen text

    # Bug testing 
    # draw_text("Velocity x: " + str())    

    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()
    FRAME += 1
    TIMER += 1 / 30
    # adds to system timer and human timer
    if SCORE >= 56:    
        TIMER = 0

    

pg.quit()
