import pygame
width=800
heigh=400
gamescreen=pygame.display.set_mode((width,heigh))
player=pygame.Rect(100,100,50,50)
pltform=pygame.Rect(100,340,50,20)
enemey=pygame.Rect(400,350,50,50)
pltform2=pygame.Rect(300,340,50,20)
direction='right'
px=0
py=350
jumptime=0
isjump=False
isfalling=True
gravity=0.64
canjump=False
#forevor blocf
while True :
    player.x=px
    if player.colliderect(pltform)or player.y>=350 or player.colliderect(pltform2):
        canjump=True
    else:
        canjump=False
    gamescreen.fill('black')
    pygame.draw.rect(gamescreen,'red',player)
    pygame.draw.rect(gamescreen,'blue',pltform)
    pygame.draw.rect(gamescreen,'green',enemey)
    pygame.draw.rect(gamescreen,'blue',pltform2)
    pygame.display.flip()
    buttons=pygame.event.get()
    for button in buttons:
        if button.type==pygame.QUIT:
            exit()
   
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        px-=2 
        print('left button pressed')
    if button[pygame.K_RIGHT]:
        px+=2
    if button[pygame.K_UP]and canjump==True:
        #jump 
        isjump=True
    if isjump==True:
        jumptime+=0.1
        print(jumptime)
    if jumptime>5:
        jumptime=0
        isjump=False
    if isjump==True:
        speed=3*(1-(jumptime/15))
        player.y-=speed
    #falliny clown
    if isjump==False and player.y<350 and isfalling==True:
        fallspeed = gravity * 0.64
        player.y+=0.64
    #check if we the pltform
    if player.colliderect(pltform):
        print('pltform')
        isfalling=False
    else:
        isfalling=True
        #pltfrom2
    if player.colliderect(pltform2):
        print('pltform2')
        isfalling=False
    else:
        isfalling=True
    #move the enemy
    if direction=="right":
        enemey.x+=1
    if enemey.x>600:
        direction="left"
    if direction=="left":
        enemey.x-=1 
    if enemey.x<400:
        direction="right"
        #