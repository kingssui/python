import pygame
width=800
heigh=400
gamescreen=pygame.display.set_mode((width,heigh))
player=pygame.Rect(100,100,50,50)
pltform=pygame.Rect(100,340,50,20)
px=0
py=350
jumptime=0
isjump=False
#forevor blocf
while True :
    player.x=px
    
    gamescreen.fill('black')
    pygame.draw.rect(gamescreen,'red',player)
    pygame.draw.rect(gamescreen,'blue',pltform)
    pygame.display.flip()
    buttons=pygame.event.get()
    for button in buttons:
        if button.type==pygame.QUIT:
            exit()
   
    button=pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        px-=5
        print('left button pressed')
    if button[pygame.K_RIGHT]:
        px+=5
    if button[pygame.K_UP]:
        #jump 
        isjump=True
    if isjump==True:
        jumptime+=0.1
        print(jumptime)
    if jumptime>5:
        jumptime=0
        isjump=False
    if isjump==True:
        speed=3*(1-(jumptime/5))
        player.y-=speed
    #falliny clown
    if isjump==False and player.y<350:
        player.y+=5
    #check if we the pltform
    if player.colliderect(pltform):
        print('pltform')
        isjump=False