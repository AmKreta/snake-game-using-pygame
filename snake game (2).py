import pygame
import random
import math

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

pygame.init()

display_width=800
display_height=600
game_display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('AMK OS')
clock=pygame.time.Clock()
FPS=30

class snake:
      def draw(self,color):
           pygame.draw.circle(game_display,color,[self.x,self.y],10)

      def update(self,snake_obj):
           self.x=snake_obj.x 
           self.y=snake_obj.y     
            
  
     
class snake_head(snake):            
      def __init__(self):  
          self.x=random.randrange(display_height)
          self.y=random.randrange(display_height)
          self.temp_x=20
          self.temp_y=0

      def set_dir(self,temp_x,temp_y):
            self.temp_x=temp_x
            self.temp_y=temp_y    

      def update(self):
          self.x+=self.temp_x
          self.y+=self.temp_y
          if self.x<0:
                self.x=display_width
          elif self.x>display_width:
                self.x=0
          elif self.y<0:
                self.y=display_height
          elif self.y>display_width:
                self.y=0

                
class snake_ai(snake):
      def __init__(self):
          self.x=random.randrange(display_width)
          self.y=random.randrange(display_height)
          self.temp_x=20
          self.temp_y=0

      def update(self,food_obj):
          self.x+=self.temp_x
          self.y+=self.temp_y

          if abs(self.x-food_obj.x)<=15 and self.temp_x!=0:
             if self.y-food_obj.y<0:
                self.temp_y=20
             else:
                self.temp_y=-20
             self.temp_x=0

          elif abs(self.y-food_obj.y)<=15 and self.temp_y!=0:
             if self.x-food_obj.x<0:
                self.temp_x=20
             else:
                self.temp_x=-20
             self.temp_y=0

          if self.x<0:
                self.x=display_width
          elif self.x>display_width:
                self.x=0
          elif self.y<0:
                self.y=display_height
          elif self.y>display_width:
                self.y=0   

class food:
      def __init__(self):
            self.r=10
            self.x=random.randrange(5,display_width-5)
            self.y=random.randrange(5,display_height+5)

      def draw(self):
            pygame.draw.circle(game_display,red,[self.x,self.y],5)

      def collision_detect(self,snake_obj):
           if math.sqrt((self.x-snake_obj.x)**2+(self.y-snake_obj.y)**2)<=15:
              self.x=random.randrange(display_width)
              self.y=random.randrange(display_height)
              return True
           return False 
                
            

player=[snake_head()]
ai=[snake_ai()]
f=food()


game_exit='false'
            
while game_exit!=True:

    clock.tick(FPS)
    game_display.fill(white)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN:
              if event.key==pygame.K_LEFT:
                  player[0].set_dir(-20,0)
              elif event.key==pygame.K_RIGHT:
                  player[0].set_dir(20,0)
              elif event.key==pygame.K_UP:
                 player[0].set_dir(0,-20)
              elif event.key==pygame.K_DOWN:
                 player[0].set_dir(0,20)
              else :
                 print(event.type)   

    player[0].draw(green)#movement of player
    player[0].update()
    ai[0].draw(blue)
    ai[0].update(f)#movement of ai 
    f.draw()

   
          
    if f.collision_detect(player[0]):#collision detection with player
       player.append(snake())    

    if f.collision_detect(ai[0]):#collision detection with ai
       ai.append(snake())
       
    i=len(player)-1 
    while i>=1:#draw player
        player[i].update(player[i-1])
        player[i].draw(green)
        i-=1

    i=len(ai)-1
    while i>=1:#draw ai    
        ai[i].update(ai[i-1])
        ai[i].draw(blue)
        i-=1
              

    pygame.display.flip()

pygame.quit()

    
