#MTJ
#Monster Slayer
#Taha, MingJun, Jessica
#Fight through enemys, bosses, get through obsticles, and advance through levels to get to the final boss

from gamelib import* #import game library

#Objects and Setup
game=Game(800,600,"Monster Slayer")

ForestBg=Image("forest_bg.png",game)
ForestBg.resizeTo(game.width,game.height)
game.setBackground(ForestBg)

x = 400
y = 450
platforms = []
for index in range(1):
    platforms.append(Image("grassplatform.png",game))
    platforms[index].resizeBy(-65)
    platforms[index].moveTo(x,y)
    x+=300
    y-=20
spikes=[]
for index in range(6):
    spikes.append(Image("spike.gif",game))
    spikes[index].resizeBy(-75)
    spikes[index].moveTo(randint(900,2000),randint(310,510))
    spikes[index].setSpeed(6,90)

win=False

hero=Animation("hero.gif",1,game,270,222)
hero.resizeBy(-70)
hero.moveTo(game.width/2,game.height-95)
health=(100)
attack=Image("attacking.png",game)
attack.resizeBy(-20)
attack.visible = False

flag=Image("flag.png",game)
flag.moveTo(430,405)
flag.resizeBy(-85)

minion=Image("minion.gif",game)
minion.moveTo(752,game.height-95)
minion.resizeBy(-60)
directionSwitch=False
minion2=Image("minion.gif",game)
minion2.moveTo(385,400)
minion2.resizeBy(-60)

#Jump Variables
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

#platform
onPlatform=False

#title screen objects
titleSrnBg=Image("title screen.png",game)
title=Image("title image.png",game)
title.resizeBy(-25)
playbtn=Image("play image.png",game)
playbtn.resizeBy(-25)
howtoplay = Image("how to play.png",game)
f1 = Font (white,20, black, "Impact")

#end screen objects
ENDbg = Image("END.jpg",game)
ENDbg.resizeTo(game.width,game.height)
GAMEOVER = Image("Game Over.png",game)
wintext=Image("win text.png",game)

#Title Screen
while not game.over:
    game.processInput()
    titleSrnBg.draw()
    title.moveTo(game.width/2,game.height-500)
    title.draw()
    playbtn.moveTo(game.width/2,game.height-360)
    howtoplay.draw()
    howtoplay.moveTo(game.width/2,game.height-100)
    if mouse.collidedWith(playbtn,"rectangle") and mouse.LeftClick:
        game.over=True
    if mouse.collidedWith(howtoplay):
        game.drawText("^  : jump",game.width/2-149,game.height-30,f1)
        game.drawText("<  : move left",game.width/2-149,game.height-50,f1)
        game.drawText(">  : move right",game.width/2-149,game.height-70,f1)
        game.drawText("[      ] : attack",game.width/2-170,game.height-90,f1)

    game.update(30)

#Level 1
game.over=False
while not game.over:
    game.processInput()
    ForestBg.draw()
    for index in range(1):
        platforms[index].draw()
    hero.draw()
    minion.draw()
    minion2.draw()
    flag.draw()
    for index in range(6):
        spikes[index].draw()
        spikes[index].move()

    for index in range(6):
        if hero.collidedWith(spikes[index]):
            game.over=True
    if minion.collidedWith(hero,"rectangle") and minion.visible:
        game.over=True
    if minion2.collidedWith(hero,"rectangle") and minion2.visible:
        game.over=True

    if hero.collidedWith(flag):
        win=True
    if win is True:
        game.over=True

    #recycle screen
    if hero.isOffScreen("right"):
        hero.moveTo(game.width-775,hero.y)
    if hero.isOffScreen("left"):
        hero.moveTo(game.width-25,hero.y)
    for index in range(6):
        if spikes[index].isOffScreen("left"):
            spikes[index].moveTo(randint(900,2000),randint(310,510))
    #Horizontal Movement
    
    if keys.Pressed[K_RIGHT]:
        hero.x+=5               #Horizontal Movement
    if keys.Pressed[K_LEFT]:
       hero.x-=5
        
    #Jump

    if hero.y< game.height-95 and not onPlatform: #value of y is based on your object's y position
        landed = False#not landed

    else:
        landed = True
   
            
    if keys.Pressed[K_UP] and landed and not jumping:#if you have landed and are not jumping and press the UP bar then jump
        jumping = True

    if jumping:
   
        hero.y -=27*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        onPlatform=False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed: #is jumping
        hero.y +=10#adjust for the height of the jump - lower number higher jump
        
    #Platform Landing
    #1
    for index in range(len(platforms)):
        if hero.collidedWith(platforms[index],"rectangle") and hero.x>platforms[index].left and hero.x<platforms[index].right and hero.y<platforms[index].top+18:
            onPlatform=True

        if onPlatform and hero.x>platforms[index].right and not jumping:
            onPlatform=False
            hero.y+6
        if onPlatform and hero.x<platforms[index].left and not jumping:
            onPlatform=False
            hero.y+6

    #minion patrol   
    if directionSwitch is False:
        minion.x-=3
    if minion.x is 25 or minion.x<25: #25
        directionSwitch=True
    if directionSwitch:
        minion.x+=3
    if minion.x is 25 or minion.x>752: #752
        directionSwitch=False


    #attack
    attack.moveTo(hero.x+3, hero.y)
    if keys.Pressed[K_SPACE]:
        attack.visible = True
    else:
        attack.visible=False
    if attack.collidedWith(minion,"rectangle") and attack.visible is True:
        minion.visible = False
    if attack.collidedWith(minion2,"rectangle") and attack.visible is True:
        minion2.visible = False
    game.update(30)

#END
game.over=False
while not game.over:
    game.processInput()
    ENDbg.draw()
    if win is True:
        wintext.draw()
    else:
        GAMEOVER.resizeBy(-1)
        GAMEOVER.draw()
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.drawText("Press [SPACE] to Close the game", game.width/2-100,game.height-50)
    game.update(30)

