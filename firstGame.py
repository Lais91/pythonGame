import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('assets/images/R1.png'), pygame.image.load('assets/images/R2.png'), pygame.image.load('assets/images/R3.png'), pygame.image.load('assets/images/R4.png'), pygame.image.load('assets/images/R5.png'), pygame.image.load('assets/images/R6.png'), pygame.image.load('assets/images/R7.png'), pygame.image.load('assets/images/R8.png'), pygame.image.load('assets/images/R9.png')]
walkLeft = [pygame.image.load('assets/images/L1.png'), pygame.image.load('assets/images/L2.png'), pygame.image.load('assets/images/L3.png'), pygame.image.load('assets/images/L4.png'), pygame.image.load('assets/images/L5.png'), pygame.image.load('assets/images/L6.png'), pygame.image.load('assets/images/L7.png'), pygame.image.load('assets/images/L8.png'), pygame.image.load('assets/images/L9.png')]
bg = pygame.image.load('assets/images/bg.jpg')
char = pygame.image.load('assets/images/standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('assets/sounds/bullet.mp3')
hitSound = pygame.mixer.Sound('assets/sounds/hit.mp3')

music = pygame.mixer.music.load('assets/sounds/bullet.mp3')
pygame.mixer.music.play(-1)

score = 0

class  Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.lastDirection = "right"
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.lastDirection == "right":
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1= pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                               
class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class Enemy(object):
    walkRight = [pygame.image.load('assets/images/R1E.png'), pygame.image.load('assets/images/R2E.png'), pygame.image.load('assets/images/R3E.png'), pygame.image.load('assets/images/R4E.png'), pygame.image.load('assets/images/R5E.png'), pygame.image.load('assets/images/R6E.png'), pygame.image.load('assets/images/R7E.png'), pygame.image.load('assets/images/R8E.png'), pygame.image.load('assets/images/R9E.png'), pygame.image.load('assets/images/R10E.png'), pygame.image.load('assets/images/R11E.png')]
    walkLeft = [pygame.image.load('assets/images/L1E.png'), pygame.image.load('assets/images/L2E.png'), pygame.image.load('assets/images/L3E.png'), pygame.image.load('assets/images/L4E.png'), pygame.image.load('assets/images/L5E.png'), pygame.image.load('assets/images/L6E.png'), pygame.image.load('assets/images/L7E.png'), pygame.image.load('assets/images/L8E.png'), pygame.image.load('assets/images/L9E.png'), pygame.image.load('assets/images/L10E.png'), pygame.image.load('assets/images/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw (self, win):
        self.move()
        if self.visible:
            if self.walkCount +1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        
    def move (self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

        
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (360, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
       bullet.draw(win) 
    
    pygame.display.update()

#mainloop
font = pygame.font.SysFont('comicsans', 20, True)
man = Player(300, 410, 64, 64)
goblin = Enemy(0, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    #FPS
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score += -5
            
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    #Movimiento muñeco teclas
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.lastDirection == "left":
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6,(0,0,0), facing))
        shotLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
        man.lastDirection = "left"
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
        man.lastDirection = "right"
    else:
        man.standing = True
        man.walkCount = 0
        
    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1 
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
    
pygame.quit()
