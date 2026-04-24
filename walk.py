import pygame
width=600
heigh=600
gamescreen=pygame.display.set_mode((width,heigh))
px=0
py=550
player=pygame.image.load('walk up1.png')
road=pygame.image.load('Gemini_Generated_Image_9y28j99y28j99y28.png')
#traffic
car=pygame.Rect(100,200,50,20)
car2=pygame.Rect(100,200,50,20)
car3=pygame.Rect(100,200,50,20)
car4=pygame.Rect(100,300,50,20)
car5=pygame.Rect(100,300,50,20)
car6=pygame.Rect(100,300,50,20)
car7=pygame.Rect(100,100,50,20)
car8=pygame.Rect(100,100,50,20)
car9=pygame.Rect(100,100,50,20)
car10=pygame.Rect(100,400,50,20)
car11=pygame.Rect(100,400,50,20)
car12=pygame.Rect(100,400,50,20)
playerhitbox=pygame.Rect(px,py,20,20)
#forever  blok
while True :
    
    gamescreen.fill('black')
    pygame.draw.rect(gamescreen,'blue',playerhitbox)
    playerhitbox.topleft=(px+20,py+20)
    gamescreen.blit(road,(0,0,))
    gamescreen.blit(player,(px,py))
    
  #  ygame.draw.rect(gamescreen,'red',(px,py,50,50),)p
#draw tiffic

    pygame.draw.rect(gamescreen,'red',car)
    pygame.draw.rect(gamescreen,'red',car2)
    pygame.draw.rect(gamescreen,'red',car3)
    pygame.draw.rect(gamescreen,'red',car4)
    pygame.draw.rect(gamescreen,'red',car5)
    pygame.draw.rect(gamescreen,'red',car6)
    pygame.draw.rect(gamescreen,'red',car7)
    pygame.draw.rect(gamescreen,'red',car8)
    pygame.draw.rect(gamescreen,'red',car9)
    pygame.draw.rect(gamescreen,'red',car10)
    pygame.draw.rect(gamescreen,'red',car11)
    pygame.draw.rect(gamescreen,'red',car12)
    
    car.x+=4
    if car.x>600:
        car.x=0
    car2.x+=1
    if car2.x>600:
        car2.x=0
    car3.x+=1
    if car3.x>600:
        car3.x=0
    car4.x+=1
    if car4.x>600:
        car4.x=0
    car5.x+=5
    if car5.x>600:
        car5.x=0
    car6.x+=1
    if car6.x>600:
        car6.x=0
    car7.x+=4
    if car7.x>600:
        car7.x=0
    car8.x+=1
    if car8.x>600:
        car8.x=0
    car9.x+=1
    if car9.x>600:
        car9.x=0
    car10.x+=1
    if car10.x>600:
        car10.x=0
    car11.x+=5
    if car11.x>600:
        car11.x=0
    car12.x+=1
    if car12.x>600:
        car12.x=0
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
        print('right button pressed')
    if button[pygame.K_UP]:
        py-=5
        print('left button pressed')
    if button[pygame.K_DOWN]:
        py+=5 
    #chek collission
    for vehicle in[car,car2,car3,car4,car5,car6,car7,car8,car9,car10,car11,car12]:
        if playerhitbox.colliderect(vehicle):
            exit()