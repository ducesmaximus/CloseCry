#this is Closecry 1: Ancient Warfare: Bad Puns
#Developed by Heidesthai Entertainment
import pygame, sys, time, random, pickle
from pygame.locals import *


pygame.init()

def menu(level):
    FPS = 30
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((500, 300))
    pygame.display.set_caption('Closecry: Ancient Warfare 1: Bad Puns')
    #Defining colors
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    #Setting basicfont
    BASICFONT = pygame.font.SysFont('Arial', 32)
    LoadGame = pygame.image.load("LoadGame.png")
    LoadGame = pygame.transform.scale(LoadGame, (500, 300))
    NewGame = pygame.image.load("NewGame.png")
    NewGame = pygame.transform.scale(NewGame, (500, 300))
    Quit = pygame.image.load("Quit.png")
    Quit = pygame.transform.scale(Quit, (500, 300))
    Ninja = pygame.image.load("NinjaRightLook.png")
    Ninja = pygame.transform.scale(Ninja, (128, 128))
    Samurai = pygame.image.load("SamuraiRightLook.png")
    Samurai = pygame.transform.scale(Samurai, (128, 128))
    Assassin = pygame.image.load("AssaJumpLeft.png")
    Assassin = pygame.transform.scale(Assassin, (128, 128))
    Knight = pygame.image.load("KnightLookRight.png")
    Knight = pygame.transform.scale(Knight, (128, 128))
    Background = pygame.image.load("Lvl1Forest.png")
    Background = pygame.transform.scale(Background, (500, 300))
    DISPLAYSURF.fill(BLUE)
    bg = NewGame
    def loadgame():
        DISPLAYSURF.fill(BLUE)
        DISPLAYSURF.blit(Background, (0, 0))
        with open('savefile.ccsf', 'rb') as f:
            level = pickle.load(f)
            if level != None:
                levelt = "level"+str(level)
                return str(levelt)
            else:
                return "level1"
    def levels(lvl):
        DISPLAYSURF.fill(BLUE)
        DISPLAYSURF.blit(Background, (0, 0))
        if lvl == "level1":
            DISPLAYSURF.blit(Ninja, (30, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                        if 30 < x < 160:
                            return "level1"
        elif lvl == "level2":
            DISPLAYSURF.blit(Ninja, (30, 150))
            DISPLAYSURF.blit(Samurai, (200, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                        if 30 < x < 160:
                            return "level1"
                        elif 160 < x < 290:
                            return "level2"
        elif lvl == "level3":
            DISPLAYSURF.blit(Ninja, (30, 150))
            DISPLAYSURF.blit(Samurai, (200, 150))
            DISPLAYSURF.blit(Assassin, (370, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                        if 30 < x < 160:
                            return "level1"
                        elif 160 < x < 290:
                            return "level2"
                        elif 290 < x < 420:
                            return "level3"
        elif lvl == "level4":
            DISPLAYSURF.blit(Ninja, (30, 150))
            DISPLAYSURF.blit(Samurai, (200, 150))
            DISPLAYSURF.blit(Assassin, (370, 150))
            DISPLAYSURF.blit(Knight, (540, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                        if 30 < x < 160:
                            return "level1"
                        elif 160 < x < 290:
                            return "level2"
                        elif 290 < x < 420:
                            return "level3"
                        elif 420 < x < 550:
                            return "level4"                            
    loop = True
    while loop:
        DISPLAYSURF.blit(bg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEMOTION:
                x = event.pos[0]
                y = event.pos[1]
                if 20 < x < 180 and 50 < y < 80:
                    bg = NewGame
                elif 20 < x < 180 and 140 < y < 165:
                    bg = LoadGame
                elif 20 < x < 180 and 220 < y < 250:
                    bg = Quit
            elif event.type == MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 20 < x < 180 and 50 < y < 80:
                    return "level1"
                if 20 < x < 180 and 140 < y < 165:
                    gamelevel = loadgame()
                    return levels(gamelevel)
                elif 20 < x < 180 and 220 < y < 250:
                    pygame.quit()
                    

def level1():
    currentlevel = 1
    FPS = 30
    level1height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2]
    level1type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 3]
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((500, 300))
    #loading the images
    Heidesthai = pygame.image.load("LogoHeidesthai.png")
    pygame.display.set_caption('Closecry: Ancient Warfare 1: Bad Puns')
    JamesLeftLook = pygame.image.load('JamesLeftLook.png')
    JamesLeftLook = pygame.transform.scale(JamesLeftLook, (64, 64))
    JamesRightLook = pygame.image.load('JamesRightLook.png')
    JamesRightLook = pygame.transform.scale(JamesRightLook, (64, 64))
    JamesWalkLeft1 = pygame.image.load('JamesLeftWalkLeftLeg.png')
    JamesWalkLeft1 = pygame.transform.scale(JamesWalkLeft1, (64, 64))
    JamesWalkLeft2 = pygame.image.load('JamesLeftWalkRightLeg.png')
    JamesWalkRight1 = pygame.image.load('JamesRightWalkLeftLeg.png')
    JamesWalkRight1 = pygame.transform.scale(JamesWalkRight1, (64, 64))
    JamesWalkRight2 = pygame.image.load('JamesRightWalkRightLeg.png')
    JamesWalkRight2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.flip(JamesWalkRight2, 1, 0)
    JamesRightBeat = pygame.image.load("JamesRightBeatUp.png")
    JamesRightBeat = pygame.transform.scale(JamesRightBeat, (64, 64))
    JamesLeftBeat = pygame.image.load("JamesLeftBeatUp.png")
    JamesLeftBeat = pygame.transform.scale(JamesLeftBeat, (64, 64))
    JamesRightStand = pygame.image.load("JamesRightStandingAttack.png")
    JamesRightStand = pygame.transform.scale(JamesRightStand, (64, 64))
    JamesLeftStand = pygame.image.load("JamesLeftStandingAttack.png")
    JamesLeftStand = pygame.transform.scale(JamesLeftStand, (64, 64))
    JamesRightAttack = pygame.image.load("JamesAttackRight.png")
    JamesRightAttack = pygame.transform.scale(JamesRightAttack, (64, 64))
    JamesLeftAttack = pygame.image.load("JamesAttackLeft.png")
    JamesLeftAttack = pygame.transform.scale(JamesLeftAttack, (64, 64))
    Grass = pygame.image.load("Grass_Block.png")
    Dirt = pygame.image.load("Dirt_Block.png")
    LevelEnemyRightLook = pygame.image.load("NinjaRightLook.png")
    LevelEnemyRightLook = pygame.transform.scale(LevelEnemyRightLook, (64, 64))
    LevelEnemyWalkRight1 = pygame.image.load("NinjaRightWalkRightLegF.png")
    LevelEnemyWalkRight1 = pygame.transform.scale(LevelEnemyWalkRight1, (64, 64))
    LevelEnemyWalkRight2 = pygame.image.load("NinjaRightWalkLeftLegF.png")
    LevelEnemyWalkRight2 = pygame.transform.scale(LevelEnemyWalkRight2, (64, 64))
    LevelEnemyWalkLeft1 = pygame.image.load("NinjaLeftWalkRightLegF.png")
    LevelEnemyWalkLeft1 = pygame.transform.scale(LevelEnemyWalkLeft1, (64, 64))
    LevelEnemyWalkLeft2 = pygame.image.load("NinjaLeftWalkLeftLegF.png")
    LevelEnemyWalkLeft2 = pygame.transform.scale(LevelEnemyWalkLeft2, (64, 64))
    LevelEnemyRightAttack = pygame.image.load("NinjaRightAttack.png")
    LevelEnemyRightAttack = pygame.transform.scale(LevelEnemyRightAttack, (64, 64))
    LevelEnemyLeftAttack = pygame.image.load("NinjaLeftAttack.png")
    LevelEnemyLeftAttack = pygame.transform.scale(LevelEnemyLeftAttack, (64, 64))
    LevelEnemyRightBeat = pygame.image.load("NinjaRightBeat.png")
    LevelEnemyRightBeat = pygame.transform.scale(LevelEnemyRightBeat, (64, 64))
    LevelEnemyLeftBeat = pygame.image.load("NinjaLeftBeat.png")
    LevelEnemyKill = pygame.image.load("NinjaRightKill.png")
    LevelEnemyKill = pygame.transform.scale(LevelEnemyKill, (64, 64))
    LevelEnemyLeftBeat = pygame.transform.scale(LevelEnemyLeftBeat, (64, 64))
    LevelEnemyDead = pygame.transform.rotate(LevelEnemyKill, 90)
    Background = pygame.image.load("Lvl1Forest.png")
    Background = pygame.transform.scale(Background, (500, 300))
    heartEmpty = pygame.image.load("heartEmpty.png")
    heartEmpty = pygame.transform.scale(heartEmpty, (50, 50))
    heartHalf = pygame.image.load("heartHalf.png")
    heartHalf = pygame.transform.scale(heartHalf, (50, 50))
    heartFull = pygame.image.load("heartFull.png")
    heartFull = pygame.transform.scale(heartFull, (50, 50))
    startingscreen = pygame.image.load("startingscreen.png")
    startingscreen = pygame.transform.scale(startingscreen, (500, 200))
    flag = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag, (50, 50))
    EHBO = pygame.image.load("ehbo.png")
    EHBO = pygame.transform.scale(EHBO, (50, 50))
    dead = pygame.image.load("dead.png")
    attackposecounter = 0
    attackposedir = "Left"
    #Defining colors
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    #Setting basicfont
    BASICFONT = pygame.font.SysFont('Arial', 32)
    up_pressed = False
    right_pressed = False
    left_pressed = False
    costume = JamesRightLook
    jumping = False
    class LevelEnemy(): #Enemy LevelEnemy Class
        def __init__(self, xposition, yposition, levelheight):
            self.speed = 6
            self.jumpHeight = 100
            self.attackDamage = 10
            self.health = 30
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = LevelEnemyRightLook
            self.counterRight = 0
            self.counterLeft = 0
            self.direction = "left"
            self.alive = 1
            self.active = 0
            self.activeTimer = random.randint(1, 15) * 30
        def chase(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos > self.x:
                self.direction = "right"
                if self.costume != LevelEnemyWalkRight1:
                    if self.counterRight < 10:
                        self.counterRight += 1
                    elif self.counterRight >= 10:
                        self.costume = LevelEnemyWalkRight1
                        self.counterRight = 0
                elif self.costume == LevelEnemyWalkRight1:
                    self.costume = LevelEnemyWalkRight2
                    if self.counterRight < 10:
                        self.counterRight += 1
                    elif self.counterRight >= 10:
                        counterRight = 0
                jump = self.checknextpos(self.x, self.y, "right")
                if jump == True:
                    self.x += self.speed
                elif jump == False:
                        self.y -= self.jumpHeight
                        self.x += self.speed*10
            elif xpos < self.x:
                self.direction = "right"
                if self.costume != LevelEnemyWalkLeft1:
                    if self.counterLeft < 10:
                        self.counterLeft += 1
                    elif self.counterLeft >= 10:
                        self.costume = LevelEnemyWalkLeft1
                        self.counterLeft = 0
                elif self.costume == LevelEnemyWalkLeft1:
                    if self.counterLeft < 10:
                        self.counterLeft += 1
                    elif self.counterLeft >= 10:
                        self.costume = LevelEnemyWalkLeft2
                        counterLeft = 0
                jump = self.checknextpos(self.x, self.y, "left")
                if jump == True:
                    self.x -= self.speed
                elif jump == False:
                        self.y -= self.jumpHeight
                        self.x -= self.speed*10
            self.checkGravity(self.x, self.y)
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if ypos >= self.y:
                dify = ypos- self.y
            elif ypos < self.y:
                dify = self.y- ypos
            dify -= 30
            if difx < 10:
                if dify < 10:
                    return True
                elif dify > 10:
                    return False
            elif difx > 10:
                return False
        def attack(self, prevHealth):
            if self.direction == "left":
                self.costume = LevelEnemyLeftAttack
            elif self.direction == "right":
                self.costume = LevelEnemyRightAttack
            health = prevHealth - self.attackDamage
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(self.costume, (self.x -x, self.y-10))
        def checknextpos(self, x, y, direction):
            level1height = self.levelheight
            currentpos = x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            if direction == "up":
                if y >= currentheight:
                    return True
                elif y < currentheight:
                    return False
            if direction == "right":
                if currentpos < len(level1height)-1:
                    nextheight = 200 -level1height[currentpos+1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
                elif currentpos >= len(level1height)-1:
                    return False
            if direction == "left":
                if currentpos > 1:
                    nextheight = 200 -level1height[currentpos-1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getHealth(self):
            return self.health
        def setHealth(self, health):
            self.health = health
            if health > 0:
                self.alive = 1
            elif health <= 0:
                self.alive = 0
        def activate(self):
            if self.activeTimer > 0:
                self.activeTimer -= 1
            elif self.activeTimer <= 0:
                self.active = 1
        def getstate(self):
            return self.active

    class healthPack(): #For healing and stuff
        def __init__(self, xposition, yposition, levelheight):
            self.healingPower = 30
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = EHBO
            self.active = 1
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if difx < 10:
                return True
            elif difx > 10:
                return False
        def heal(self, prevHealth):
            health = prevHealth + self.healingPower
            self.active = 0
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(EHBO, (self.x -x, self.y-20))
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getstate(self):
            return self.active

    class Player(): #Player class
        def __init__(self):
            self.speed = 10
            self.jumpHeight = 100
            self.attackDamage = 30
            self.x = 150
            self.y = 100
            self.health = 50
            self.maxHealth = 100
            self.jumpy = 0
        def move(self, x, y, direction): #function for moving
            if direction == "up":
                if self.jumpy-self.y<self.jumpHeight:
                    y -= 25
                    self.y = y
                    return y
                else:
                    return False
            if direction == "right":
                x += self.speed
                self.x = x
                return x
            if direction == "left":
                x -= self.speed
                self.x = x
                return x
        def getxpos(self):
            return self.x
        def getypos(self):
            return self.y
        def gethealth(self):
            return self.health
        def setxpos(self, x):
            self.x = x
        def setypos(self, y):
            self.y = y
        def sethealth(self, health):
            self.health = health
        
    James = Player() #Creates the main player
    gameplay = True
    attackCounter = 0
    counterRight = 0
    counterLeft = 0
    intro = 1
    level = 1
    enemylist = []
    healthpacklist = []
    alive = 1
    def pause():
        gamepaused = 1
        while gamepaused:
            paused = BASICFONT.render("p to continue, o for menu, s to save", True, RED)
            DISPLAYSURF.blit(paused, (10, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        gamepaused = 0
                        return None
                    elif event.key == K_o:
                        return True
                    elif event.key == K_s:
                        with open('savefile.ccsf', 'wb') as f:
                            pickle.dump(currentlevel, f, protocol=2)
    if level == 1:
        for Enemies in range(0, 10):
            randx = random.randint(900, len(level1height) *50)
            enemylist.insert(0, LevelEnemy(randx, 300, level1height))
        for healthpacks in range(0, 3):
            randx = random.randint(900, len(level1height) *50)
            healthpacklist.insert(0, healthPack(randx, 50, level1height))
    while gameplay == True: #main game loop
        health = James.gethealth()
        health = int(health)
        if health <= 0:
            gameplay = False
            died = True
        x = James.getxpos()
        x = int(x)
        y = James.getypos()
        y = int(y)
        alive = 0
        for Enemy in enemylist:
            EHealth = Enemy.getHealth()
            if EHealth > 0:
                alive += 1
                Enemyactive = Enemy.getstate()
                if Enemyactive == 1:
                    Checkforplayer = Enemy.checkForPlayer(x, y)
                    if Checkforplayer == True:
                        if attackCounter < 5:
                            attackCounter += 1
                        elif attackCounter >= 5:
                            attackHealth = Enemy.attack(health)
                            James.sethealth(attackHealth)
                            costume = "JamesRightBeat"
                            attackCounter = 0
                    elif Checkforplayer == False:
                        Enemy.chase(x, y)
                elif Enemyactive == 0:
                    Enemy.activate()
            elif EHealth <= 0:
                Enemy.checkGravity(Enemy.x, Enemy.y)
        if alive <= 0:
            if x >= 3400:
                time.sleep(1)
                gameplay = False
                died = False
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                playernear = HealthPack.checkForPlayer(James.x, James.y)
                if playernear == True:
                    nexthealth = HealthPack.heal(James.health)
                    James.sethealth(nexthealth)
            HealthPack.checkGravity(HealthPack.x, HealthPack.y)
        currentpos = x/50
        if currentpos < len(level1height):
            currentheight = 200 -level1height[currentpos] * 50 -30
        if y < currentheight:
                y += 10
                James.setypos(y)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    up_pressed = True
                elif event.key == K_RIGHT:
                    right_pressed = True  
                elif event.key == K_LEFT:
                    left_pressed = True
                elif event.key == K_p:
                    pause_menu = pause()
                    if pause_menu:
                        return "menu"
            elif event.type == KEYUP:
                if event.key == K_UP:
                    up_pressed = False
                elif event.key == K_RIGHT:
                    right_pressed = False
                    costume = "JamesRightLook"
                elif event.key == K_LEFT:
                    left_pressed = False
                    costume = "JamesLeftLook"
                elif event.key == K_SPACE:
                    for Enemy in enemylist:
                        Checkforplayer = Enemy.checkForPlayer(x, y)
                        if Checkforplayer == True:
                            EnemyHealth = Enemy.getHealth()
                            EnemyHealth -= James.attackDamage
                            if EnemyHealth > 0:
                                Enemy.costume = LevelEnemyRightBeat
                            elif EnemyHealth <= 0:
                                Enemy.costume = LevelEnemyDead
                            Enemy.setHealth(EnemyHealth)
                            xpos = Enemy.x
                            ypos = Enemy.y
                            if xpos >= x:
                                costume = "JamesRightAttack"
                                attackposecounter = 15
                                attackposedir = "Right"
                            elif xpos < x:
                                costume = "JamesLeftAttack"
                                attackposecounter = 15
                                attackposedir = "Left"
                        elif Checkforplayer == False:
                            xpos = Enemy.x
                            ypos = Enemy.y
                            if xpos >= x:
                                costume = "JamesRightStand"
                            elif xpos < x:
                                costume = "JamesLeftStand"
        if attackposecounter > 0:
            if attackposedir == "Right":
                costume = "JamesRightAttack"
            elif attackposedir == "Left":
                costume = "JamesLeftAttack"
            attackposecounter -= 1                   
        if up_pressed == True:
            if y >= currentheight or jumping:
                if not jumping:
                    jumping = True
                    James.jumpy = y
                jumpy = James.move(x, y, "up")
                if jumpy != False:
                    y = jumpy
                else:
                    jumping = False
        if right_pressed == True:
            if currentpos < len(level1height)-1:
                nextheight = 200 -level1height[currentpos+1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "right")
            if costume != "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight1"
                    counterRight = 0
            elif costume == "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight2"
                    counterRight = 0
        if left_pressed == True:
            if currentpos > 1:
                nextheight = 200 -level1height[currentpos-1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "left")
            if costume != "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft1"
                    counterLeft = 0
            elif costume == "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft2"
                    counterLeft = 0
        xpos = BASICFONT.render(str(x), True, RED)
        ypos = BASICFONT.render(str(y), True, RED)
        alive = "Enemies: " + str(alive)
        EnemiesAlive = BASICFONT.render(alive, True, RED)
        DISPLAYSURF.fill(BLUE)
        bgs = [Background, Background, Background]
        for i in range(0,2):
            DISPLAYSURF.blit(bgs[i], (i*500-(x/10), 0))
        DISPLAYSURF.blit(xpos, (10, 10))
        DISPLAYSURF.blit(ypos, (100, 10))
        DISPLAYSURF.blit(EnemiesAlive, (300, 10))
        healthquotient = James.maxHealth/10
        healthhearts = health/healthquotient
        if healthhearts%2 == 0:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            for heartempty in range(0, 5-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280 -heartempty * 20, 20))
        else:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            DISPLAYSURF.blit(heartHalf, (healthhearts/2 *20 +200, 20))
            for heartempty in range(0, 4-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, ( 280-heartempty * 20, 20))
        if intro == 1:
            DISPLAYSURF.fill(BLACK)
            Presents = BASICFONT.render("Presents:", True, WHITE)
            DISPLAYSURF.blit(Heidesthai, (100, 75))
            DISPLAYSURF.blit(Presents, (100, 175))
            pygame.display.update()
            time.sleep(2.5)
            clock = pygame.time.Clock()
            movie = pygame.movie.Movie("closecry.mpg")
            movie_screen = pygame.Surface(movie.get_size()).convert()
            movie.set_display(movie_screen)
            movie.play()
            playing = True
            while playing:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            movie.stop()
                            playing = False
                if movie.get_busy() == False:
                    movie.stop()
                    playing = False
                DISPLAYSURF.blit(movie_screen,(25,25))
                pygame.display.update()
                clock.tick(FPS)
            time.sleep(1)
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(startingscreen, (0, 0))
            pygame.display.update()
            introkey = 0
            while introkey == 0:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            introkey = 1
            DISPLAYSURF.fill(BLACK)
            firstlevel = BASICFONT.render("Level 1", True, RED)
            DISPLAYSURF.blit(firstlevel, (50, 50))
            pygame.display.update()
            time.sleep(1)
            DISPLAYSURF.fill(BLACK)
            pygame.display.update()
            intro = 0
        for block in range(1, len(level1height)+1): #level constructor
            if level1type[block-1] == 1:
                blocktype = Grass
            elif level1type[block-1] == 2:
                blocktype = Dirt
            elif level1type[block-1] == 3:
                blocktype = flag
            if level1height[block-1] == 1:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 150))
            elif level1height[block-1] == 2:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                if blocktype == flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 125))
                elif blocktype != flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 100))
            elif level1height[block-1] == 3:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 100))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 50))
        for extrablock in range(len(level1height)+1,len(level1height)+11):
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 50))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 100))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 250))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 200))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 150))
        if costume == "JamesLeftLook":
            DISPLAYSURF.blit(JamesLeftLook, (25, y))
        elif costume == "JamesRightLook":
            DISPLAYSURF.blit(JamesRightLook, (25, y))
        elif costume == "JamesWalkLeft1":
            DISPLAYSURF.blit(JamesWalkLeft1, (25, y))
        elif costume == "JamesWalkLeft2":
            DISPLAYSURF.blit(JamesWalkLeft2, (25, y))
        elif costume == "JamesWalkRight1":
            DISPLAYSURF.blit(JamesWalkRight1, (25, y))
        elif costume == "JamesWalkRight2":
            DISPLAYSURF.blit(JamesWalkRight2, (25, y))
        elif costume == "JamesRightBeat":
            DISPLAYSURF.blit(JamesRightBeat, (25, y))
        elif costume == "JamesRightAttack":
            DISPLAYSURF.blit(JamesRightAttack, (25, y))
        elif costume == "JamesLeftAttack":
            DISPLAYSURF.blit(JamesLeftAttack, (25, y))
        elif costume == "JamesRightStand":
            DISPLAYSURF.blit(JamesRightStand, (25, y))
        elif costume == "JamesLeftStand":
            DISPLAYSURF.blit(JamesLeftStand, (25, y))
        for Enemy in enemylist:
            Enemy.blit()
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                HealthPack.blit()
        pygame.display.update()
        fpsClock.tick(FPS)
    if gameplay == 0:
        if died == True:
            pygame.display.set_caption('You Died')
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(dead, (0, 0))
            pygame.display.update()
            time.sleep(3)
            return False
        elif died == False:
            DISPLAYSURF.fill(BLACK)
            msg = BASICFONT.render("First level completed.", True, RED)
            DISPLAYSURF.blit(msg, (10, 100))
            pygame.display.update()
            time.sleep(3)
            return True
#---------------------------level2------------------------------------------
#---------------------------------------------------------------------------
def level2():
    currentlevel = 2
    FPS = 30
    level1height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2]
    level1type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 3]
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((500, 300))
    #loading the images
    Heidesthai = pygame.image.load("LogoHeidesthai.png")
    pygame.display.set_caption('Closecry: Ancient Warfare 1: Bad Puns')
    JamesLeftLook = pygame.image.load('JamesLeftLook.png')
    JamesLeftLook = pygame.transform.scale(JamesLeftLook, (64, 64))
    JamesRightLook = pygame.image.load('JamesRightLook.png')
    JamesRightLook = pygame.transform.scale(JamesRightLook, (64, 64))
    JamesWalkLeft1 = pygame.image.load('JamesLeftWalkLeftLeg.png')
    JamesWalkLeft1 = pygame.transform.scale(JamesWalkLeft1, (64, 64))
    JamesWalkLeft2 = pygame.image.load('JamesLeftWalkRightLeg.png')
    JamesWalkRight1 = pygame.image.load('JamesRightWalkLeftLeg.png')
    JamesWalkRight1 = pygame.transform.scale(JamesWalkRight1, (64, 64))
    JamesWalkRight2 = pygame.image.load('JamesRightWalkRightLeg.png')
    JamesWalkRight2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.flip(JamesWalkRight2, 1, 0)
    JamesRightBeat = pygame.image.load("JamesRightBeatUp.png")
    JamesRightBeat = pygame.transform.scale(JamesRightBeat, (64, 64))
    JamesLeftBeat = pygame.image.load("JamesLeftBeatUp.png")
    JamesLeftBeat = pygame.transform.scale(JamesLeftBeat, (64, 64))
    JamesRightStand = pygame.image.load("JamesRightStandingAttack.png")
    JamesRightStand = pygame.transform.scale(JamesRightStand, (64, 64))
    JamesLeftStand = pygame.image.load("JamesLeftStandingAttack.png")
    JamesLeftStand = pygame.transform.scale(JamesLeftStand, (64, 64))
    JamesRightAttack = pygame.image.load("JamesAttackRight.png")
    JamesRightAttack = pygame.transform.scale(JamesRightAttack, (64, 64))
    JamesLeftAttack = pygame.image.load("JamesAttackLeft.png")
    JamesLeftAttack = pygame.transform.scale(JamesLeftAttack, (64, 64))
    Grass = pygame.image.load("Grass_Block.png")
    Dirt = pygame.image.load("Dirt_Block.png")
    LevelEnemyRightLook = pygame.image.load("SamuraiRightLook.png")
    LevelEnemyRightLook = pygame.transform.scale(LevelEnemyRightLook, (64, 64))
    LevelEnemyWalkRight1 = pygame.image.load("SamuraiRightWalkRightLegF.png")
    LevelEnemyWalkRight1 = pygame.transform.scale(LevelEnemyWalkRight1, (64, 64))
    LevelEnemyWalkRight2 = pygame.image.load("SamuraiRightWalkLeftLegF.png")
    LevelEnemyWalkRight2 = pygame.transform.scale(LevelEnemyWalkRight2, (64, 64))
    LevelEnemyWalkLeft1 = pygame.image.load("SamuraiLeftWalkRightLegF.png")
    LevelEnemyWalkLeft1 = pygame.transform.scale(LevelEnemyWalkLeft1, (64, 64))
    LevelEnemyWalkLeft2 = pygame.image.load("SamuraiLeftWalkLeftLegF.png")
    LevelEnemyWalkLeft2 = pygame.transform.scale(LevelEnemyWalkLeft2, (64, 64))
    LevelEnemyRightAttack = pygame.image.load("SamuraiRightAttack.png")
    LevelEnemyRightAttack = pygame.transform.scale(LevelEnemyRightAttack, (64, 64))
    LevelEnemyLeftAttack = pygame.image.load("SamuraiLeftAttack.png")
    LevelEnemyLeftAttack = pygame.transform.scale(LevelEnemyLeftAttack, (64, 64))
    LevelEnemyRightBeat = pygame.image.load("SamuraiRightBeat.png")
    LevelEnemyRightBeat = pygame.transform.scale(LevelEnemyRightBeat, (64, 64))
    LevelEnemyLeftBeat = pygame.image.load("SamuraiLeftBeat.png")
    LevelEnemyKill = pygame.image.load("SamuraiRightKill.png")
    LevelEnemyKill = pygame.transform.scale(LevelEnemyKill, (64, 64))
    LevelEnemyLeftBeat = pygame.transform.scale(LevelEnemyLeftBeat, (64, 64))
    LevelEnemyDead = pygame.transform.rotate(LevelEnemyKill, 90)
    Background = pygame.image.load("Lvl2Hostil.png")
    Background = pygame.transform.scale(Background, (500, 300))
    heartEmpty = pygame.image.load("heartEmpty.png")
    heartEmpty = pygame.transform.scale(heartEmpty, (50, 50))
    heartHalf = pygame.image.load("heartHalf.png")
    heartHalf = pygame.transform.scale(heartHalf, (50, 50))
    heartFull = pygame.image.load("heartFull.png")
    heartFull = pygame.transform.scale(heartFull, (50, 50))
    startingscreen = pygame.image.load("startingscreen.png")
    startingscreen = pygame.transform.scale(startingscreen, (500, 200))
    flag = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag, (50, 50))
    EHBO = pygame.image.load("ehbo.png")
    EHBO = pygame.transform.scale(EHBO, (50, 50))
    dead = pygame.image.load("dead.png")
    #Defining colors
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    #Setting basicfont
    BASICFONT = pygame.font.SysFont('Arial', 32)
    up_pressed = False
    right_pressed = False
    left_pressed = False
    costume = JamesRightLook
    jumping = False
    attackposecounter = 0
    class LevelEnemy(): #Enemy LevelEnemy Class
        def __init__(self, xposition, yposition, levelheight):
            self.speed = 6
            self.jumpHeight = 100
            self.attackDamage = 30
            self.health = 100
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = LevelEnemyRightLook
            self.counterRight = 0
            self.counterLeft = 0
            self.direction = "left"
            self.alive = 1
            self.active = 0
            self.activeTimer = random.randint(1, 15) *100
        def chase(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos > self.x:
                self.direction = "right"
                if self.costume != "LevelEnemyWalkRight1":
                    if self.counterRight < 10:
                        self.counterRight += 1
                    elif self.counterRight >= 10:
                        self.costume = LevelEnemyWalkRight1
                        self.counterRight = 0
                elif self.costume == "LevelEnemyWalkRight1":
                    if self.counterRight < 10:
                        self.counterRight += 1
                    elif self.counterRight >= 10:
                        self.costume = LevelEnemyWalkRight2
                        counterRight = 0
                jump = self.checknextpos(self.x, self.y, "right")
                if jump == True:
                    self.x += self.speed
                elif jump == False:
                        self.y -= self.jumpHeight
                        self.x += self.speed*10
            elif xpos < self.x:
                self.direction = "right"
                if self.costume != "LevelEnemyWalkLeft1":
                    if self.counterLeft < 10:
                        self.counterLeft += 1
                    elif self.counterLeft >= 10:
                        self.costume = LevelEnemyWalkLeft1
                        self.counterLeft = 0
                elif self.costume == "LevelEnemyWalkLeft1":
                    if self.counterLeft < 10:
                        self.counterLeft += 1
                    elif self.counterLeft >= 10:
                        self.costume = LevelEnemyWalkLeft2
                        counterLeft = 0
                jump = self.checknextpos(self.x, self.y, "left")
                if jump == True:
                    self.x -= self.speed
                elif jump == False:
                        self.y -= self.jumpHeight
                        self.x -= self.speed*10
            self.checkGravity(self.x, self.y)
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if ypos >= self.y:
                dify = ypos- self.y
            elif ypos < self.y:
                dify = self.y- ypos
            dify -= 30
            if difx < 10:
                if dify < 10:
                    return True
                elif dify > 10:
                    return False
            elif difx > 10:
                return False
        def attack(self, prevHealth):
            if self.direction == "left":
                self.costume = LevelEnemyLeftAttack
            elif self.direction == "right":
                self.costume = LevelEnemyRightAttack
            health = prevHealth - self.attackDamage
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(self.costume, (self.x -x, self.y-20))
        def checknextpos(self, x, y, direction):
            level1height = self.levelheight
            currentpos = x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            if direction == "up":
                if y >= currentheight:
                    return True
                elif y < currentheight:
                    return False
            if direction == "right":
                if currentpos < len(level1height)-1:
                    nextheight = 200 -level1height[currentpos+1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
                elif currentpos >= len(level1height)-1:
                    return False
            if direction == "left":
                if currentpos > 1:
                    nextheight = 200 -level1height[currentpos-1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getHealth(self):
            return self.health
        def setHealth(self, health):
            self.health = health
            if health > 0:
                self.alive = 1
            elif health <= 0:
                self.alive = 0
        def activate(self):
            if self.activeTimer > 0:
                self.activeTimer -= 1
            elif self.activeTimer <= 0:
                self.active = 1
        def getstate(self):
            return self.active
    class healthPack(): #For healing and stuff
        def __init__(self, xposition, yposition, levelheight):
            self.healingPower = 30
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = EHBO
            self.active = 1
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if difx < 10:
                return True
            elif difx > 10:
                return False
        def heal(self, prevHealth):
            health = prevHealth + self.healingPower
            self.active = 0
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(EHBO, (self.x -x, self.y-20))
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getstate(self):
            return self.active

    class Player(): #Player class
        def __init__(self):
            self.speed = 15
            self.jumpHeight = 100
            self.attackDamage = 50
            self.x = 100
            self.y = 0
            self.health = 70
            self.maxHealth = 100
            self.jumpy = 0
        def move(self, x, y, direction): #function for moving
            if direction == "up":
                if self.jumpy-self.y<self.jumpHeight:
                    y -= 25
                    self.y = y
                    return y
                else:
                    return False
            if direction == "right":
                x += self.speed
                self.x = x
                return x
            if direction == "left":
                x -= self.speed
                self.x = x
                return x
        def getxpos(self):
            return self.x
        def getypos(self):
            return self.y
        def gethealth(self):
            return self.health
        def setxpos(self, x):
            self.x = x
        def setypos(self, y):
            self.y = y
        def sethealth(self, health):
            self.health = health
        
    James = Player() #Creates the main player
    gameplay = True
    attackCounter = 0
    counterRight = 0
    counterLeft = 0
    intro = 1
    level = 1
    enemylist = []
    healthpacklist = []
    alive = 1
    def pause():
        gamepaused = 1
        while gamepaused:
            paused = BASICFONT.render("p to continue, o for menu, s to save", True, RED)
            DISPLAYSURF.blit(paused, (10, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        gamepaused = 0
                        return None
                    elif event.key == K_o:
                        return True
                    elif event.key == K_s:
                        with open('savefile.ccsf', 'wb') as f:
                            pickle.dump(currentlevel, f, protocol=2)
    if level == 1:
        for Enemies in range(0, 15):
            randx = random.randint(900, len(level1height) *50)
            enemylist.insert(0, LevelEnemy(randx, 300, level1height))
        for healthpacks in range(0, 3):
            randx = random.randint(900, len(level1height) *50)
            healthpacklist.insert(0, healthPack(randx, 50, level1height))
    while gameplay == True: #main game loop
        health = James.gethealth()
        health = int(health)
        if health <= 0:
            gameplay = False
            died = True
        x = James.getxpos()
        x = int(x)
        y = James.getypos()
        y = int(y)
        alive = 0
        for Enemy in enemylist:
            EHealth = Enemy.getHealth()
            if EHealth > 0:
                alive += 1
                Enemyactive = Enemy.getstate()
                if Enemyactive == 1:
                    Checkforplayer = Enemy.checkForPlayer(x, y)
                    if Checkforplayer == True:
                        if attackCounter < 20:
                            attackCounter += 1
                        elif attackCounter >= 20:
                            attackHealth = Enemy.attack(health)
                            James.sethealth(attackHealth)
                            costume = "JamesRightBeat"
                            attackCounter = 0
                    elif Checkforplayer == False:
                        Enemy.chase(x, y)
                elif Enemyactive == 0:
                    Enemy.activate()
            elif EHealth <= 0:
                Enemy.checkGravity(Enemy.x, Enemy.y)
        if alive <= 0:
            if x >= 3100:
                time.sleep(1)
                gameplay = False
                died = False
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                player = HealthPack.checkForPlayer(x, y)
                if player == 1:
                    nexthealth = HealthPack.heal(James.health)
                    James.sethealth(nexthealth)
            HealthPack.checkGravity(HealthPack.x, HealthPack.y)
        currentpos = x/50
        if currentpos < len(level1height):
            currentheight = 200 -level1height[currentpos] * 50 -30
        if y < currentheight:
                y += 10
                James.setypos(y)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    up_pressed = True
                elif event.key == K_RIGHT:
                    right_pressed = True  
                elif event.key == K_LEFT:
                    left_pressed = True
                elif event.key == K_p:
                    pause_menu = pause()
                    if pause_menu:
                        return "menu"
            elif event.type == KEYUP:
                if event.key == K_UP:
                    up_pressed = False
                elif event.key == K_RIGHT:
                    right_pressed = False
                    costume = "JamesRightLook"
                elif event.key == K_LEFT:
                    left_pressed = False
                    costume = "JamesLeftLook"
                elif event.key == K_SPACE:
                    for Enemy in enemylist:
                        Checkforplayer = Enemy.checkForPlayer(x, y)
                        if Checkforplayer == True:
                            EnemyHealth = Enemy.getHealth()
                            EnemyHealth -= James.attackDamage
                            if EnemyHealth > 0:
                                Enemy.costume = LevelEnemyRightBeat
                            elif EnemyHealth <= 0:
                                Enemy.costume = LevelEnemyDead
                            Enemy.setHealth(EnemyHealth)
                            xpos = Enemy.x
                            ypos = Enemy.y
                            if xpos >= x:
                                Enemy.x += 50
                                costume = "JamesRightAttack"
                                attackposecounter = 15
                                attackposedir = "Right"
                            elif xpos < x:
                                Enemy.x -= 50
                                costume = "JamesLeftAttack"
                                attackposecounter = 15
                                attackposedir = "Left"
                        elif Checkforplayer == False:
                            xpos = Enemy.x
                            ypos = Enemy.y
                            if xpos >= x:
                                costume = "JamesRightStand"
                            elif xpos < x:
                                costume = "JamesLeftStand"
        if attackposecounter > 0:
            if attackposedir == "Right":
                costume = "JamesRightAttack"
            elif attackposedir == "Left":
                costume = "JamesLeftAttack"
            attackposecounter -= 1  
        if up_pressed == True:
            if y >= currentheight or jumping:
                if not jumping:
                    jumping = True
                    James.jumpy = y
                jumpy = James.move(x, y, "up")
                if jumpy != False:
                    y = jumpy
                else:
                    jumping = False
        if right_pressed == True:
            if currentpos < len(level1height)-1:
                nextheight = 200 -level1height[currentpos+1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "right")
            if costume != "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight1"
                    counterRight = 0
            elif costume == "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight2"
                    counterRight = 0
        if left_pressed == True:
            if currentpos > 1:
                nextheight = 200 -level1height[currentpos-1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "left")
            if costume != "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft1"
                    counterLeft = 0
            elif costume == "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft2"
                    counterLeft = 0
        xpos = BASICFONT.render(str(x), True, RED)
        ypos = BASICFONT.render(str(y), True, RED)
        alive = "Enemies: " + str(alive)
        EnemiesAlive = BASICFONT.render(alive, True, RED)
        DISPLAYSURF.fill(BLUE)
        bgs = [Background, Background, Background]
        for i in range(0,2):
            DISPLAYSURF.blit(bgs[i], (i*500-(x/10), 0))
        DISPLAYSURF.blit(xpos, (10, 10))
        DISPLAYSURF.blit(ypos, (100, 10))
        DISPLAYSURF.blit(EnemiesAlive, (300, 10))
        healthquotient = James.maxHealth/10
        healthhearts = health/healthquotient
        if healthhearts%2 == 0:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            for heartempty in range(0, 5-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280 -heartempty * 20, 20))
        else:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            DISPLAYSURF.blit(heartHalf, (healthhearts/2 *20 +200, 20))
            for heartempty in range(0, 4-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280-heartempty * 20, 20))
        for block in range(1, len(level1height)+1): #level constructor
            if level1type[block-1] == 1:
                blocktype = Grass
            elif level1type[block-1] == 2:
                blocktype = Dirt
            elif level1type[block-1] == 3:
                blocktype = flag
            if level1height[block-1] == 1:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 150))
            elif level1height[block-1] == 2:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                if blocktype == flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 125))
                elif blocktype != flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 100))
            elif level1height[block-1] == 3:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 100))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 50))
        for extrablock in range(len(level1height)+1,len(level1height)+11):
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 50))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 100))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 250))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 200))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 150))
        if costume == "JamesLeftLook":
            DISPLAYSURF.blit(JamesLeftLook, (25, y))
        elif costume == "JamesRightLook":
            DISPLAYSURF.blit(JamesRightLook, (25, y))
        elif costume == "JamesWalkLeft1":
            DISPLAYSURF.blit(JamesWalkLeft1, (25, y))
        elif costume == "JamesWalkLeft2":
            DISPLAYSURF.blit(JamesWalkLeft2, (25, y))
        elif costume == "JamesWalkRight1":
            DISPLAYSURF.blit(JamesWalkRight1, (25, y))
        elif costume == "JamesWalkRight2":
            DISPLAYSURF.blit(JamesWalkRight2, (25, y))
        elif costume == "JamesRightBeat":
            DISPLAYSURF.blit(JamesRightBeat, (25, y))
        elif costume == "JamesRightAttack":
            DISPLAYSURF.blit(JamesRightAttack, (25, y))
        elif costume == "JamesLeftAttack":
            DISPLAYSURF.blit(JamesLeftAttack, (25, y))
        elif costume == "JamesRightStand":
            DISPLAYSURF.blit(JamesRightStand, (25, y))
        elif costume == "JamesLeftStand":
            DISPLAYSURF.blit(JamesLeftStand, (25, y))
        for Enemy in enemylist:
            Enemy.blit()
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                HealthPack.blit()
        pygame.display.update()
        fpsClock.tick(FPS)
    if gameplay == 0:
        if died == True:
            pygame.display.set_caption('You Died')
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(dead, (0, 0))
            pygame.display.update()
            time.sleep(3)
            return False
        elif died == False:
            DISPLAYSURF.fill(BLACK)
            msg = BASICFONT.render("Second level completed.", True, RED)
            DISPLAYSURF.blit(msg, (10, 100))
            pygame.display.update()
            time.sleep(3)
            return True
#------------------------------------------LVL 3-------
#------------------------------------------------------

def level3():
    currentlevel = 3
    FPS = 30
    level1height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2]
    level1type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 3]
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((500, 300))
    #loading the images
    Heidesthai = pygame.image.load("LogoHeidesthai.png")
    pygame.display.set_caption('Closecry: Ancient Warfare 1: Bad Puns')
    JamesLeftLook = pygame.image.load('JamesLeftLook.png')
    JamesLeftLook = pygame.transform.scale(JamesLeftLook, (64, 64))
    JamesRightLook = pygame.image.load('JamesRightLook.png')
    JamesRightLook = pygame.transform.scale(JamesRightLook, (64, 64))
    JamesWalkLeft1 = pygame.image.load('JamesLeftWalkLeftLeg.png')
    JamesWalkLeft1 = pygame.transform.scale(JamesWalkLeft1, (64, 64))
    JamesWalkLeft2 = pygame.image.load('JamesLeftWalkRightLeg.png')
    JamesWalkRight1 = pygame.image.load('JamesRightWalkLeftLeg.png')
    JamesWalkRight1 = pygame.transform.scale(JamesWalkRight1, (64, 64))
    JamesWalkRight2 = pygame.image.load('JamesRightWalkRightLeg.png')
    JamesWalkRight2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.flip(JamesWalkRight2, 1, 0)
    JamesRightBeat = pygame.image.load("JamesRightBeatUp.png")
    JamesRightBeat = pygame.transform.scale(JamesRightBeat, (64, 64))
    JamesLeftBeat = pygame.image.load("JamesLeftBeatUp.png")
    JamesLeftBeat = pygame.transform.scale(JamesLeftBeat, (64, 64))
    JamesRightStand = pygame.image.load("JamesRightStandingAttack.png")
    JamesRightStand = pygame.transform.scale(JamesRightStand, (64, 64))
    JamesLeftStand = pygame.image.load("JamesLeftStandingAttack.png")
    JamesLeftStand = pygame.transform.scale(JamesLeftStand, (64, 64))
    JamesRightAttack = pygame.image.load("JamesAttackRight.png")
    JamesRightAttack = pygame.transform.scale(JamesRightAttack, (64, 64))
    JamesLeftAttack = pygame.image.load("JamesAttackLeft.png")
    JamesLeftAttack = pygame.transform.scale(JamesLeftAttack, (64, 64))
    Grass = pygame.image.load("Grass_Block.png")
    Dirt = pygame.image.load("Dirt_Block.png")
    AssaJumpRight = pygame.image.load("AssaJumpRight.png")
    AssaJumpRight = pygame.transform.scale(AssaJumpRight, (64, 64))
    AssaJumpLeft = pygame.image.load("AssaJumpLeft.png")
    AssaJumpLeft = pygame.transform.scale(AssaJumpLeft, (64, 64))
    AssaRunRightRightL = pygame.image.load("AssaRunRightRightL.png")
    AssaRunRightRightL = pygame.transform.scale(AssaRunRightRightL, (64, 64))
    AssaRunRightLeftL = pygame.image.load("AssaRunRightLeftL.png")
    AssaRunRightLeftL = pygame.transform.scale(AssaRunRightLeftL, (64, 64))
    AssaRunLeftRightL = pygame.image.load("AssaRunLeftRightL.png")
    AssaRunLeftRightL = pygame.transform.scale(AssaRunLeftRightL, (64, 64))
    AssaRunLeftLeftL = pygame.image.load("AssaRunLeftLeftL.png")
    AssaRunLeftLeftL = pygame.transform.scale(AssaRunLeftLeftL, (64, 64))
    AssaDead = pygame.image.load("AssaDead.png")
    AssaDead = pygame.transform.scale(AssaDead, (50, 50))
    Sign = pygame.image.load("sign.png")
    Sign = pygame.transform.scale(Sign, (50, 50))
    Background = pygame.image.load("Lvl2Hostil.png")
    Background = pygame.transform.scale(Background, (500, 300))
    heartEmpty = pygame.image.load("heartEmpty.png")
    heartEmpty = pygame.transform.scale(heartEmpty, (50, 50))
    heartHalf = pygame.image.load("heartHalf.png")
    heartHalf = pygame.transform.scale(heartHalf, (50, 50))
    heartFull = pygame.image.load("heartFull.png")
    heartFull = pygame.transform.scale(heartFull, (50, 50))
    startingscreen = pygame.image.load("startingscreen.png")
    startingscreen = pygame.transform.scale(startingscreen, (500, 200))
    flag = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag, (50, 50))
    EHBO = pygame.image.load("ehbo.png")
    EHBO = pygame.transform.scale(EHBO, (50, 50))
    dead = pygame.image.load("dead.png")
    #Defining colors
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    #Setting basicfont
    BASICFONT = pygame.font.SysFont('Arial', 32)
    up_pressed = False
    right_pressed = False
    left_pressed = False
    costume = JamesRightLook
    jumping = False
    attackposecounter = 0
    class LevelEnemy(): #Enemy LevelEnemy Class
        def __init__(self, xposition, yposition, levelheight):
            self.speed = 12
            self.jumpHeight = 100
            self.attackDamage = 80
            self.health = 20
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = AssaJumpRight
            self.alive = 1
            self.active = 0
            self.counterBeforeAttack = 0
            self.running = False
            self.attacking = False
            self.attacked = False
        def chase(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos > self.x:
                self.costume = AssaJumpRight
            elif xpos < self.x:
                self.costume = AssaJumpLeft
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if difx <= 30:
                return True
            elif difx > 30:
                return False
        def waitBeforeAttack(self):
            self.costume = Sign
            if self.counterBeforeAttack < 50:
                self.counterBeforeAttack += 1
                return False
            elif self.counterBeforeAttack >= 50:
                self.costume = AssaJumpRight
                return True
        def attack(self, prevHealth, xpos, ypos):
            if self.attacking == True:
                self.chase(xpos, ypos)
                if self.y < ypos:
                    self.y += 8
                    return False
                elif self.y >= ypos:
                    health = prevHealth - self.attackDamage
                    self.attacking = False
                    return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(self.costume, (self.x -x, self.y-20))
        def run(self):
            if self.x > 40:
                self.costume = AssaRunLeftLeftL
                jump = self.checknextpos(self.x, self.y, "left")
                if jump == True:
                    self.x -= self.speed
                if jump == False:
                    self.y -= self.jumpHeight
                    self.x -= self.speed
            if self.x <= 100:
                self.active = 0
                self.health = 0
                self.alive = 0
            self.checkGravity(self.x, self.y)
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def checknextpos(self, x, y, direction):
            level1height = self.levelheight
            currentpos = x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            if direction == "up":
                if y >= currentheight:
                    return True
                elif y < currentheight:
                    return False
            if direction == "right":
                if currentpos < len(level1height)-1:
                    nextheight = 200 -level1height[currentpos+1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
                elif currentpos >= len(level1height)-1:
                    return False
            if direction == "left":
                if currentpos > 1:
                    nextheight = 200 -level1height[currentpos-1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
        def getHealth(self):
            return self.health
        def setHealth(self, health):
            self.health = health
            if health > 0:
                self.alive = 1
            elif health <= 0:
                self.alive = 0
        def activate(self, xpos, ypos):
            playernear = self.checkForPlayer(xpos, ypos)
            if playernear == True:
                self.active = 1
        def getstate(self):
            return self.active
        def setAttacking(self):
            self.attacking = True

#-----------------------------------------------------------------------------------
    class healthPack(): #For healing and stuff
        def __init__(self, xposition, yposition, levelheight):
            self.healingPower = 30
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = EHBO
            self.active = 1
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if difx < 10:
                return True
            elif difx > 10:
                return False
        def heal(self, prevHealth):
            health = prevHealth + self.healingPower
            self.active = 0
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(EHBO, (self.x -x, self.y-20))
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getstate(self):
            return self.active

    class Player(): #Player class
        def __init__(self):
            self.speed = 15
            self.jumpHeight = 100
            self.attackDamage = 50
            self.x = 100
            self.y = 0
            self.health = 70
            self.maxHealth = 100
            self.jumpy = 0
        def move(self, x, y, direction): #function for moving
            if direction == "up":
                if self.jumpy-self.y<self.jumpHeight:
                    y -= 25
                    self.y = y
                    return y
                else:
                    return False
            if direction == "right":
                x += self.speed
                self.x = x
                return x
            if direction == "left":
                x -= self.speed
                self.x = x
                return x
        def getxpos(self):
            return self.x
        def getypos(self):
            return self.y
        def gethealth(self):
            return self.health
        def setxpos(self, x):
            self.x = x
        def setypos(self, y):
            self.y = y
        def sethealth(self, health):
            self.health = health
        
    James = Player() #Creates the main player
    gameplay = True
    attackCounter = 0
    counterRight = 0
    counterLeft = 0
    intro = 1
    level = 1
    enemylist = []
    healthpacklist = []
    alive = 1
    def pause():
        gamepaused = 1
        while gamepaused:
            paused = BASICFONT.render("p to continue, o for menu, s to save", True, RED)
            DISPLAYSURF.blit(paused, (10, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        gamepaused = 0
                        return None
                    elif event.key == K_o:
                        return True
                    elif event.key == K_s:
                        with open('savefile.ccsf', 'wb') as f:
                            pickle.dump(currentlevel, f, protocol=2)
    if level == 1:
        for Enemies in range(0, 8):
            randx = random.randint(900, len(level1height) *50)
            enemylist.insert(0, LevelEnemy(randx, 0, level1height))
        for healthpacks in range(0, 5):
            randx = random.randint(900, len(level1height) *50)
            healthpacklist.insert(0, healthPack(randx, 50, level1height))
    while gameplay == True: #main game loop
        health = James.gethealth()
        health = int(health)
        if health <= 0:
            gameplay = False
            died = True
        x = James.getxpos()
        x = int(x)
        y = James.getypos()
        y = int(y)
        alive = 0
        for Enemy in enemylist:
            EHealth = Enemy.getHealth()
            if EHealth > 0:
                alive += 1
                Enemyactive = Enemy.getstate()
                if Enemyactive == 1:
                    Checkforplayer = Enemy.checkForPlayer(x, y)
                    wait = Enemy.waitBeforeAttack()
                    if wait == True:
                        if Checkforplayer == True:
                            if Enemy.attacked == False:
                                Enemy.setAttacking()
                        if Enemy.attacking == True:
                            attackHealth = Enemy.attack(health, x, y)
                            if attackHealth != False:
                                James.sethealth(attackHealth)
                                costume = "JamesRightBeat"
                                Enemy.attacked = True
                                Enemy.running = True                        
                elif Enemyactive == 0:
                    Enemy.activate(x, y)
                if Enemy.running == True:
                    Enemy.run()
            elif EHealth <= 0:
                Enemy.checkGravity(Enemy.x, Enemy.y)
        if alive <= 0:
            if x >= 3100:
                time.sleep(1)
                gameplay = False
                died = False

        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                player = HealthPack.checkForPlayer(x, y)
                if player == 1:
                    nexthealth = HealthPack.heal(James.health)
                    James.sethealth(nexthealth)
            HealthPack.checkGravity(HealthPack.x, HealthPack.y)
        currentpos = x/50
        if currentpos < len(level1height):
            currentheight = 200 -level1height[currentpos] * 50 -30
        if y < currentheight:
                y += 10
                James.setypos(y)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    up_pressed = True
                elif event.key == K_RIGHT:
                    right_pressed = True  
                elif event.key == K_LEFT:
                    left_pressed = True
                elif event.key == K_p:
                    pause_menu = pause()
                    if pause_menu:
                        return "menu"
            elif event.type == KEYUP:
                if event.key == K_UP:
                    up_pressed = False
                elif event.key == K_RIGHT:
                    right_pressed = False
                    costume = "JamesRightLook"
                elif event.key == K_LEFT:
                    left_pressed = False
                    costume = "JamesLeftLook"
                elif event.key == K_SPACE or event.key == K_b:
                    for Enemy in enemylist:
                        Checkforplayer = Enemy.checkForPlayer(x, y)
                        if Checkforplayer == True:
                            if Enemy.active == True and Enemy.attacking == False:
                                EnemyHealth = Enemy.getHealth()
                                EnemyHealth -= James.attackDamage
                                if EnemyHealth <= 0:
                                    Enemy.costume = AssaDead #Nog geen poses, Simon...
                                Enemy.setHealth(EnemyHealth)
                                xpos = Enemy.x
                                ypos = Enemy.y
                                if xpos >= x:
                                    Enemy.x += 50
                                    costume = "JamesRightAttack"
                                    attackposecounter = 15
                                    attackposedir = "Right"
                                elif xpos < x:
                                    Enemy.x -= 50
                                    costume = "JamesLeftAttack"
                                    attackposecounter = 15
                                    attackposedir = "Left"
                            elif Checkforplayer == False:
                                xpos = Enemy.x
                                ypos = Enemy.y
                                if xpos >= x:
                                    costume = "JamesRightStand"
                                elif xpos < x:
                                    costume = "JamesLeftStand"
        if attackposecounter > 0:
            if attackposedir == "Right":
                costume = "JamesRightAttack"
            elif attackposedir == "Left":
                costume = "JamesLeftAttack"
            attackposecounter -= 1  
        if up_pressed == True:
            if y >= currentheight or jumping:
                if not jumping:
                    jumping = True
                    James.jumpy = y
                jumpy = James.move(x, y, "up")
                if jumpy != False:
                    y = jumpy
                else:
                    jumping = False
        if right_pressed == True:
            if currentpos < len(level1height)-1:
                nextheight = 200 -level1height[currentpos+1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "right")
            if costume != "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight1"
                    counterRight = 0
            elif costume == "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight2"
                    counterRight = 0
        if left_pressed == True:
            if currentpos > 1:
                nextheight = 200 -level1height[currentpos-1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "left")
            if costume != "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft1"
                    counterLeft = 0
            elif costume == "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft2"
                    counterLeft = 0
        xpos = BASICFONT.render(str(x), True, RED)
        ypos = BASICFONT.render(str(y), True, RED)
        alive = "Enemies: " + str(alive)
        EnemiesAlive = BASICFONT.render(alive, True, RED)
        DISPLAYSURF.fill(BLUE)
        bgs = [Background, Background, Background]
        for i in range(0,2):
            DISPLAYSURF.blit(bgs[i], (i*500-(x/10), 0))
        DISPLAYSURF.blit(xpos, (10, 10))
        DISPLAYSURF.blit(ypos, (100, 10))
        DISPLAYSURF.blit(EnemiesAlive, (300, 10))
        healthquotient = James.maxHealth/10
        healthhearts = health/healthquotient
        if healthhearts%2 == 0:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            for heartempty in range(0, 5-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280 -heartempty * 20, 20))
        else:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            DISPLAYSURF.blit(heartHalf, (healthhearts/2 *20 +200, 20))
            for heartempty in range(0, 4-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280-heartempty * 20, 20))
        for block in range(1, len(level1height)+1): #level constructor
            if level1type[block-1] == 1:
                blocktype = Grass
            elif level1type[block-1] == 2:
                blocktype = Dirt
            elif level1type[block-1] == 3:
                blocktype = flag
            if level1height[block-1] == 1:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 150))
            elif level1height[block-1] == 2:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                if blocktype == flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 125))
                elif blocktype != flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 100))
            elif level1height[block-1] == 3:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 100))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 50))
        for extrablock in range(len(level1height)+1,len(level1height)+11):
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 50))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 100))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 250))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 200))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 150))
        if costume == "JamesLeftLook":
            DISPLAYSURF.blit(JamesLeftLook, (25, y))
        elif costume == "JamesRightLook":
            DISPLAYSURF.blit(JamesRightLook, (25, y))
        elif costume == "JamesWalkLeft1":
            DISPLAYSURF.blit(JamesWalkLeft1, (25, y))
        elif costume == "JamesWalkLeft2":
            DISPLAYSURF.blit(JamesWalkLeft2, (25, y))
        elif costume == "JamesWalkRight1":
            DISPLAYSURF.blit(JamesWalkRight1, (25, y))
        elif costume == "JamesWalkRight2":
            DISPLAYSURF.blit(JamesWalkRight2, (25, y))
        elif costume == "JamesRightBeat":
            DISPLAYSURF.blit(JamesRightBeat, (25, y))
        elif costume == "JamesRightAttack":
            DISPLAYSURF.blit(JamesRightAttack, (25, y))
        elif costume == "JamesLeftAttack":
            DISPLAYSURF.blit(JamesLeftAttack, (25, y))
        elif costume == "JamesRightStand":
            DISPLAYSURF.blit(JamesRightStand, (25, y))
        elif costume == "JamesLeftStand":
            DISPLAYSURF.blit(JamesLeftStand, (25, y))
        for Enemy in enemylist:
            Enemy.blit()
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                HealthPack.blit()
        pygame.display.update()
        fpsClock.tick(FPS)
    if gameplay == 0:
        if died == True:
            DISPLAYSURF.fill(BLACK)
            clock = pygame.time.Clock()
            movie = pygame.movie.Movie("assassin_death.mpg")
            movie_screen = pygame.Surface((300, 500))
            movie.set_display(movie_screen)
            movie.play()
            playing = True
            while playing:
                if movie.get_busy() == False:
                    movie.stop()
                    playing = False
                DISPLAYSURF.blit(movie_screen,(25,25))
                pygame.display.update()
                clock.tick(FPS)
            pygame.display.set_caption('You Died')
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(dead, (0, 0))
            pygame.display.update()
            time.sleep(3)
            return False
        elif died == False:
            DISPLAYSURF.fill(BLACK)
            clock = pygame.time.Clock()
            movie = pygame.movie.Movie("assassin_kill.mpg")
            movie_screen = pygame.Surface(movie.get_size()).convert()
            movie.set_display(movie_screen)
            movie.play()
            playing = True
            while playing:
                if movie.get_busy() == False:
                    movie.stop()
                    playing = False
                DISPLAYSURF.blit(movie_screen,(25,25))
                pygame.display.update()
                clock.tick(FPS)
            msg = BASICFONT.render("Third level completed.", True, RED)
            DISPLAYSURF.blit(msg, (10, 100))
            pygame.display.update()
            time.sleep(3)
            return True
#-----------------------------------------------------------------LVL 4--------------------------------
        #--------------------------------------------
def level4():
    currentlevel = 4
    FPS = 30
    level1height = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2]
    level1type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 3]
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((500, 300))
    #loading the images
    Heidesthai = pygame.image.load("LogoHeidesthai.png")
    pygame.display.set_caption('Closecry: Ancient Warfare 1: Bad Puns')
    JamesLeftLook = pygame.image.load('JamesLeftLook.png')
    JamesLeftLook = pygame.transform.scale(JamesLeftLook, (64, 64))
    JamesRightLook = pygame.image.load('JamesRightLook.png')
    JamesRightLook = pygame.transform.scale(JamesRightLook, (64, 64))
    JamesWalkLeft1 = pygame.image.load('JamesLeftWalkLeftLeg.png')
    JamesWalkLeft1 = pygame.transform.scale(JamesWalkLeft1, (64, 64))
    JamesWalkLeft2 = pygame.image.load('JamesLeftWalkRightLeg.png')
    JamesWalkRight1 = pygame.image.load('JamesRightWalkLeftLeg.png')
    JamesWalkRight1 = pygame.transform.scale(JamesWalkRight1, (64, 64))
    JamesWalkRight2 = pygame.image.load('JamesRightWalkRightLeg.png')
    JamesWalkRight2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.scale(JamesWalkRight2, (64, 64))
    JamesWalkLeft2 = pygame.transform.flip(JamesWalkRight2, 1, 0)
    JamesRightBeat = pygame.image.load("JamesRightBeatUp.png")
    JamesRightBeat = pygame.transform.scale(JamesRightBeat, (64, 64))
    JamesLeftBeat = pygame.image.load("JamesLeftBeatUp.png")
    JamesLeftBeat = pygame.transform.scale(JamesLeftBeat, (64, 64))
    JamesRightStand = pygame.image.load("JamesRightStandingAttack.png")
    JamesRightStand = pygame.transform.scale(JamesRightStand, (64, 64))
    JamesLeftStand = pygame.image.load("JamesLeftStandingAttack.png")
    JamesLeftStand = pygame.transform.scale(JamesLeftStand, (64, 64))
    JamesRightAttack = pygame.image.load("JamesAttackRight.png")
    JamesRightAttack = pygame.transform.scale(JamesRightAttack, (64, 64))
    JamesLeftAttack = pygame.image.load("JamesAttackLeft.png")
    JamesLeftAttack = pygame.transform.scale(JamesLeftAttack, (64, 64))
    Grass = pygame.image.load("Grass_Block.png")
    Dirt = pygame.image.load("Dirt_Block.png")
    LevelEnemyRightLook = pygame.image.load("KnightLookRight.png")
    LevelEnemyRightLook = pygame.transform.scale(LevelEnemyRightLook, (64, 64))
    LevelEnemyWalkRight1 = pygame.image.load("KnightWalkRightRight.png")
    LevelEnemyWalkRight1 = pygame.transform.scale(LevelEnemyWalkRight1, (64, 64))
    LevelEnemyWalkRight2 = pygame.image.load("KnightWalkRightLeft.png")
    LevelEnemyWalkRight2 = pygame.transform.scale(LevelEnemyWalkRight2, (64, 64))
    LevelEnemyWalkLeft1 = pygame.image.load("KnightWalkLeftRight.png")
    LevelEnemyWalkLeft1 = pygame.transform.scale(LevelEnemyWalkLeft1, (64, 64))
    LevelEnemyWalkLeft2 = pygame.image.load("KnightWalkLeftLeft.png")
    LevelEnemyWalkLeft2 = pygame.transform.scale(LevelEnemyWalkLeft2, (64, 64))
    LevelEnemyRightAttack = pygame.image.load("KnightAttackRight.png")
    LevelEnemyRightAttack = pygame.transform.scale(LevelEnemyRightAttack, (64, 64))
    LevelEnemyLeftAttack = pygame.image.load("KnightAttackLeft.png")
    LevelEnemyLeftAttack = pygame.transform.scale(LevelEnemyLeftAttack, (64, 64))
    LevelEnemyRightBeat = pygame.image.load("SamuraiRightBeat.png")
    LevelEnemyRightBeat = pygame.transform.scale(LevelEnemyRightBeat, (64, 64))
    LevelEnemyLeftBeat = pygame.image.load("SamuraiLeftBeat.png")
    LevelEnemyKill = pygame.image.load("KnightDeadRight.png")
    LevelEnemyKill = pygame.transform.scale(LevelEnemyKill, (64, 64))
    LevelEnemyLeftBeat = pygame.transform.scale(LevelEnemyLeftBeat, (64, 64))
    LevelEnemyDead = LevelEnemyKill
    LevelEnemyBlock = pygame.transform.rotate(LevelEnemyKill, 180)
    Background = pygame.image.load("Lvl2Hostil.png")
    Background = pygame.transform.scale(Background, (500, 300))
    heartEmpty = pygame.image.load("heartEmpty.png")
    heartEmpty = pygame.transform.scale(heartEmpty, (50, 50))
    heartHalf = pygame.image.load("heartHalf.png")
    heartHalf = pygame.transform.scale(heartHalf, (50, 50))
    heartFull = pygame.image.load("heartFull.png")
    heartFull = pygame.transform.scale(heartFull, (50, 50))
    startingscreen = pygame.image.load("startingscreen.png")
    startingscreen = pygame.transform.scale(startingscreen, (500, 200))
    flag = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag, (50, 50))
    EHBO = pygame.image.load("ehbo.png")
    EHBO = pygame.transform.scale(EHBO, (50, 50))
    dead = pygame.image.load("dead.png")
    #Defining colors
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    #Setting basicfont
    BASICFONT = pygame.font.SysFont('Arial', 32)
    up_pressed = False
    right_pressed = False
    left_pressed = False
    costume = JamesRightLook
    jumping = False
    attackposecounter = 0
    class LevelEnemy(): #Enemy LevelEnemy Class
        def __init__(self, xposition, yposition, levelheight):
            self.speed = 4
            self.jumpHeight = 70
            self.attackDamage = 40
            self.health = 150
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = LevelEnemyRightLook
            self.counterRight = 0
            self.counterLeft = 0
            self.direction = "left"
            self.alive = 1
            self.active = 0
            self.activeTimer = random.randint(1, 15) *50
            self.turnSpeed = 20
            self.turnCounter = self.turnSpeed
        def chase(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos > self.x:
                if self.turnCounter <= 0 or self.direction == "left":
                    self.direction = "left"
                    if self.costume != "LevelEnemyWalkRight1":
                        if self.counterRight < 10:
                            self.counterRight += 1
                        elif self.counterRight >= 10:
                            self.costume = LevelEnemyWalkRight1
                            self.counterRight = 0
                    elif self.costume == "LevelEnemyWalkRight1":
                        if self.counterRight < 10:
                            self.counterRight += 1
                        elif self.counterRight >= 10:
                            self.costume = LevelEnemyWalkRight2
                            self.counterRight = 0
                    jump = self.checknextpos(self.x, self.y, "right")
                    if jump == True:
                        self.x += self.speed
                    elif jump == False:
                            self.y -= self.jumpHeight
                            self.x += self.speed*10
                else:
                    self.turnCounter -= 1
            elif xpos < self.x:
                if self.turnCounter <= 0 or self.direction == "right":
                    self.direction = "right"
                    if self.costume != "LevelEnemyWalkLeft1":
                        if self.counterLeft < 10:
                            self.counterLeft += 1
                        elif self.counterLeft >= 10:
                            self.costume = LevelEnemyWalkLeft1
                            self.counterLeft = 0
                    elif self.costume == "LevelEnemyWalkLeft1":
                        if self.counterLeft < 10:
                            self.counterLeft += 1
                        elif self.counterLeft >= 10:
                            self.costume = LevelEnemyWalkLeft2
                            self.counterLeft = 0
                    jump = self.checknextpos(self.x, self.y, "left")
                    if jump == True:
                        self.x -= self.speed
                    elif jump == False:
                            self.y -= self.jumpHeight
                            self.x -= self.speed*10
                    self.turnCounter = self.turnSpeed
                else:
                    self.turnCounter -= 1
            self.checkGravity(self.x, self.y)
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if ypos >= self.y:
                dify = ypos- self.y
            elif ypos < self.y:
                dify = self.y- ypos
            dify -= 30
            if difx < 10:
                if dify < 10:
                    return True
                elif dify > 10:
                    return False
            elif difx > 10:
                return False
        def checkForAttackPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            block = False
            if self.direction == "left":
                if xpos >= self.x:
                    difx = xpos -self.x
                else:
                    block = True
                    difx = self.x-xpos
            elif self.direction == "right":
                if xpos < self.x:
                    difx = self.x- xpos
                else:
                    block = True
                    difx = xpos -self.x
            if difx <= 30:
                if block == False:
                    return True
                elif block == True:
                    return "Attack"
            elif difx > 30:
                return False
        def attack(self, prevHealth):
            if self.direction == "left":
                self.costume = LevelEnemyLeftAttack
            elif self.direction == "right":
                self.costume = LevelEnemyRightAttack
            health = prevHealth - self.attackDamage
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(self.costume, (self.x -x, self.y-20))
        def checknextpos(self, x, y, direction):
            level1height = self.levelheight
            currentpos = x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            if direction == "up":
                if y >= currentheight:
                    return True
                elif y < currentheight:
                    return False
            if direction == "right":
                if currentpos < len(level1height)-1:
                    nextheight = 200 -level1height[currentpos+1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
                elif currentpos >= len(level1height)-1:
                    return False
            if direction == "left":
                if currentpos > 1:
                    nextheight = 200 -level1height[currentpos-1] * 50
                    if y <= nextheight:
                        return True
                    elif y > nextheight:
                        return False
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getHealth(self):
            return self.health
        def setHealth(self, health):
            self.health = health
            if health > 0:
                self.alive = 1
            elif health <= 0:
                self.alive = 0
        def activate(self):
            if self.activeTimer > 0:
                self.activeTimer -= 1
            elif self.activeTimer <= 0:
                self.active = 1
        def getstate(self):
            return self.active
        def block(self):
            self.costume = LevelEnemyBlock
    class healthPack(): #For healing and stuff
        def __init__(self, xposition, yposition, levelheight):
            self.healingPower = 30
            self.x = xposition
            self.y = yposition
            self.levelheight = levelheight
            self.costume = EHBO
            self.active = 1
        def checkForPlayer(self, xpos, ypos):
            self.x = int(self.x)
            self.y = int(self.y)
            xpos = int(xpos)
            ypos = int(ypos)
            if xpos >= self.x:
                difx = xpos -self.x
            elif xpos < self.x:
                difx = self.x- xpos
            if difx < 10:
                return True
            elif difx > 10:
                return False
        def heal(self, prevHealth):
            health = prevHealth + self.healingPower
            self.active = 0
            return health
        def blit(self):
            if self.active == 1:
                DISPLAYSURF.blit(EHBO, (self.x -x, self.y-20))
        def checkGravity(self, x, y):
            level1height = self.levelheight
            currentpos = self.x /50
            if currentpos < len(level1height):
                currentheight = 200 -level1height[currentpos] * 50
            elif currentpos >= len(level1height):
                currentheight = 200-level1height[len(level1height)-1]
            if self.y < currentheight:
                self.y += 10
        def getstate(self):
            return self.active

    class Player(): #Player class
        def __init__(self):
            self.speed = 15
            self.jumpHeight = 100
            self.attackDamage = 50
            self.x = 100
            self.y = 0
            self.health = 70
            self.maxHealth = 100
            self.jumpy = 0
        def move(self, x, y, direction): #function for moving
            if direction == "up":
                if self.jumpy-self.y<self.jumpHeight:
                    y -= 25
                    self.y = y
                    return y
                else:
                    return False
            if direction == "right":
                x += self.speed
                self.x = x
                return x
            if direction == "left":
                x -= self.speed
                self.x = x
                return x
        def getxpos(self):
            return self.x
        def getypos(self):
            return self.y
        def gethealth(self):
            return self.health
        def setxpos(self, x):
            self.x = x
        def setypos(self, y):
            self.y = y
        def sethealth(self, health):
            self.health = health
        
    James = Player() #Creates the main player
    gameplay = True
    attackCounter = 0
    counterRight = 0
    counterLeft = 0
    intro = 1
    level = 1
    enemylist = []
    healthpacklist = []
    alive = 1
    def pause():
        gamepaused = 1
        while gamepaused:
            paused = BASICFONT.render("p to continue, o for menu, s to save", True, RED)
            DISPLAYSURF.blit(paused, (10, 50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        gamepaused = 0
                        return None
                    elif event.key == K_o:
                        return True
                    elif event.key == K_s:
                        with open('savefile.ccsf', 'wb') as f:
                            pickle.dump(currentlevel, f, protocol=2)
    if level == 1:
        for Enemies in range(0, 4):
            randx = random.randint(900, len(level1height) *50)
            enemylist.insert(0, LevelEnemy(randx, 300, level1height))
        for healthpacks in range(0, 5):
            randx = random.randint(900, len(level1height) *50)
            healthpacklist.insert(0, healthPack(randx, 50, level1height))
    while gameplay == True: #main game loop
        health = James.gethealth()
        health = int(health)
        if health <= 0:
            gameplay = False
            died = True
        x = James.getxpos()
        x = int(x)
        y = James.getypos()
        y = int(y)
        alive = 0
        for Enemy in enemylist: #Enemy AI
            EHealth = Enemy.getHealth()
            if EHealth > 0:
                alive += 1
                Enemyactive = Enemy.getstate()
                if Enemyactive == 1:
                    Checkforplayer = Enemy.checkForPlayer(x, y)
                    if Checkforplayer == True:
                        if attackCounter < 20:
                            attackCounter += 1
                        elif attackCounter >= 20:
                            attackHealth = Enemy.attack(health)
                            James.sethealth(attackHealth)
                            costume = "JamesRightBeat"
                            attackCounter = 0
                    elif Checkforplayer == False:
                        Enemy.chase(x, y)
                elif Enemyactive == 0:
                    Enemy.activate()
            elif EHealth <= 0:
                Enemy.checkGravity(Enemy.x, Enemy.y)
        if alive <= 0:
            if x >= 3100:
                time.sleep(1)
                gameplay = False
                died = False
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                player = HealthPack.checkForPlayer(x, y)
                if player == 1:
                    nexthealth = HealthPack.heal(James.health)
                    James.sethealth(nexthealth)
            HealthPack.checkGravity(HealthPack.x, HealthPack.y)
        currentpos = x/50
        if currentpos < len(level1height):
            currentheight = 200 -level1height[currentpos] * 50 -30
        if y < currentheight:
                y += 10
                James.setypos(y)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    up_pressed = True
                elif event.key == K_RIGHT:
                    right_pressed = True  
                elif event.key == K_LEFT:
                    left_pressed = True
                elif event.key == K_p:
                    pause_menu = pause()
                    if pause_menu:
                        return "menu"
            elif event.type == KEYUP:
                if event.key == K_UP:
                    up_pressed = False
                elif event.key == K_RIGHT:
                    right_pressed = False
                    costume = "JamesRightLook"
                elif event.key == K_LEFT:
                    left_pressed = False
                    costume = "JamesLeftLook"
                elif event.key == K_SPACE: #kill
                    for Enemy in enemylist:
                        Checkforplayer = Enemy.checkForAttackPlayer(x, y)
                        if Checkforplayer == True:
                            EnemyHealth = Enemy.getHealth()
                            EnemyHealth -= James.attackDamage
                            if EnemyHealth > 0:
                                Enemy.costume = LevelEnemyRightBeat
                            elif EnemyHealth <= 0:
                                Enemy.costume = LevelEnemyDead
                            Enemy.setHealth(EnemyHealth)
                            xpos = Enemy.x
                            ypos = Enemy.y
                            if xpos >= x:
                                Enemy.x += 50
                                costume = "JamesRightAttack"
                                attackposecounter = 15
                                attackposedir = "Right"
                            elif xpos < x:
                                Enemy.x -= 50
                                costume = "JamesLeftAttack"
                                attackposecounter = 15
                                attackposedir = "Left"
                            ypos = Enemy.y
                            if xpos >= x:
                                costume = "JamesRightStand"
                            elif xpos < x:
                                costume = "JamesLeftStand"
                        elif Checkforplayer == "Attack":
                            James.health -= Enemy.attackDamage/2
                            Enemy.block()
                            James.costume = "JamesRightBeat"
        if attackposecounter > 0:
            if attackposedir == "Right":
                costume = "JamesRightAttack"
            elif attackposedir == "Left":
                costume = "JamesLeftAttack"
            attackposecounter -= 1  
        if up_pressed == True:
            if y >= currentheight or jumping:
                if not jumping:
                    jumping = True
                    James.jumpy = y
                jumpy = James.move(x, y, "up")
                if jumpy != False:
                    y = jumpy
                else:
                    jumping = False
        if right_pressed == True:
            if currentpos < len(level1height)-1:
                nextheight = 200 -level1height[currentpos+1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "right")
            if costume != "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight1"
                    counterRight = 0
            elif costume == "JamesWalkRight1":
                if counterRight < 10:
                    counterRight += 1
                elif counterRight >= 10:
                    costume = "JamesWalkRight2"
                    counterRight = 0
        if left_pressed == True:
            if currentpos > 1:
                nextheight = 200 -level1height[currentpos-1] * 50
                if y <= nextheight:
                    x = James.move(x, y, "left")
            if costume != "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft1"
                    counterLeft = 0
            elif costume == "JamesWalkLeft1":
                if counterLeft < 10:
                    counterLeft += 1
                elif counterLeft >= 10:
                    costume = "JamesWalkLeft2"
                    counterLeft = 0
        xpos = BASICFONT.render(str(x), True, RED)
        ypos = BASICFONT.render(str(y), True, RED)
        alive = "Enemies: " + str(alive)
        EnemiesAlive = BASICFONT.render(alive, True, RED)
        DISPLAYSURF.fill(BLUE)
        bgs = [Background, Background, Background]
        for i in range(0,2):
            DISPLAYSURF.blit(bgs[i], (i*500-(x/10), 0))
        DISPLAYSURF.blit(xpos, (10, 10))
        DISPLAYSURF.blit(ypos, (100, 10))
        DISPLAYSURF.blit(EnemiesAlive, (300, 10))
        healthquotient = James.maxHealth/10
        healthhearts = health/healthquotient
        if healthhearts%2 == 0: #draw hearts
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            for heartempty in range(0, 5-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280 -heartempty * 20, 20))
        else:
            for heart in range(0, healthhearts/2):
                DISPLAYSURF.blit(heartFull, (heart *20 +200, 20))
            DISPLAYSURF.blit(heartHalf, (healthhearts/2 *20 +200, 20))
            for heartempty in range(0, 4-healthhearts/2):
                DISPLAYSURF.blit(heartEmpty, (280-heartempty * 20, 20))
        for block in range(1, len(level1height)+1): #level constructor
            if level1type[block-1] == 1:
                blocktype = Grass
            elif level1type[block-1] == 2:
                blocktype = Dirt
            elif level1type[block-1] == 3:
                blocktype = flag
            if level1height[block-1] == 1:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 150))
            elif level1height[block-1] == 2:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                if blocktype == flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 125))
                elif blocktype != flag:
                    DISPLAYSURF.blit(blocktype, (block *50 -x, 100))
            elif level1height[block-1] == 3:
                DISPLAYSURF.blit(Dirt, (block *50 -x, 250))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 200))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 150))
                DISPLAYSURF.blit(Dirt, (block *50 -x, 100))
                DISPLAYSURF.blit(blocktype, (block *50 -x, 50))
        for extrablock in range(len(level1height)+1,len(level1height)+11):
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 50))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 100))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 250))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 200))
            DISPLAYSURF.blit(Dirt, (extrablock *50 -x, 150))
        if costume == "JamesLeftLook":
            DISPLAYSURF.blit(JamesLeftLook, (25, y))
        elif costume == "JamesRightLook":
            DISPLAYSURF.blit(JamesRightLook, (25, y))
        elif costume == "JamesWalkLeft1":
            DISPLAYSURF.blit(JamesWalkLeft1, (25, y))
        elif costume == "JamesWalkLeft2":
            DISPLAYSURF.blit(JamesWalkLeft2, (25, y))
        elif costume == "JamesWalkRight1":
            DISPLAYSURF.blit(JamesWalkRight1, (25, y))
        elif costume == "JamesWalkRight2":
            DISPLAYSURF.blit(JamesWalkRight2, (25, y))
        elif costume == "JamesRightBeat":
            DISPLAYSURF.blit(JamesRightBeat, (25, y))
        elif costume == "JamesRightAttack":
            DISPLAYSURF.blit(JamesRightAttack, (25, y))
        elif costume == "JamesLeftAttack":
            DISPLAYSURF.blit(JamesLeftAttack, (25, y))
        elif costume == "JamesRightStand":
            DISPLAYSURF.blit(JamesRightStand, (25, y))
        elif costume == "JamesLeftStand":
            DISPLAYSURF.blit(JamesLeftStand, (25, y))
        for Enemy in enemylist:
            Enemy.blit()
        for HealthPack in healthpacklist:
            active = HealthPack.getstate()
            if active == 1:
                HealthPack.blit()
        pygame.display.update()
        fpsClock.tick(FPS)
    if gameplay == 0:
        if died == True:
            pygame.display.set_caption('You Died')
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(dead, (0, 0))
            pygame.display.update()
            time.sleep(3)
            return False
        elif died == False:
            DISPLAYSURF.fill(BLACK)
            msg = BASICFONT.render("Fourth level completed.", True, RED)
            DISPLAYSURF.blit(msg, (10, 100))
            pygame.display.update()
            time.sleep(3)
            return True

if __name__ == "__main__":
    arrow = ( "xX                      ",
              "XOX                     ",
              "XOOX                    ",
              "XOOOX                   ",
              "XOOOOX                  ",
              "XOOOOOX                 ",
              "XOOOOOOX                ",
              "XOOOOOOOX               ",
              "XOO.....OX              ",
              "XO.OOOOOOOX             ",
              "XO.OOOOOOOOX            ",
              "XO.OOOOOOOOOX           ",
              "XOO.....OOOOOX          ",
              "XOOOOOOOOOOOOOX         ",
              "XOOOOOOOOOOOOOOX        ",
              "XOOOOOOXXXXXXOOOX       ",
              "XOOOXXX      XXXX       ",
              "XXXX                    ",
              "                        ",
              "                        ",
              "                        ",
              "                        ",
              "                        ",
              "                        ")
    def Cursor(arrow):
        hotspot = None
        for y in range(len(arrow)):
            for x in range(len(arrow[y])):
                if arrow[y][x] in ['x', ',', 'O']:
                    hotspot = x,y
                    break
            if hotspot != None:
                break
        if hotspot == None:
            raise Exception("No hotspot specified for cursor '%s'!" %
    cursorname)
        s2 = []
        for line in arrow:
            s2.append(line.replace('x', 'X').replace(',', '.').replace('O',
    'o'))
        cursor, mask = pygame.cursors.compile(s2, 'X', '.', 'o')
        size = len(arrow[0]), len(arrow)
        pygame.mouse.set_cursor(size, hotspot, cursor, mask)
        
    Cursor(arrow)

    currentlevel = menu("level1")
    while True:
        if currentlevel == "level1":
            lvl1 = level1()
            if lvl1 == True:
                currentlevel = "level2"
            elif lvl1 == "menu":
                currentlevel = menu("level1")
        elif currentlevel == "level2":
            lvl2 = level2()
            if lvl2 == True:
                currentlevel = "level3"
            elif lvl2 == "menu":
                currentlevel = menu("level2")
        elif currentlevel == "level3":
            lvl3 = level3()
            if lvl3 == True:
                currentlevel = "level4"
            elif lvl3 == "menu":
                currentlevel = menu("level3")
        elif currentlevel == "level4":
            lvl4 = level4()
            if lvl4 == True:
                currentlevel = "level5"
            elif lvl4 == "menu":
                currentlevel = menu("level4")
        else:
            currentlevel = "level1"
            pygame.quit()
#------------------------------------END OF SCRIPT-------------------------------------------------------#
