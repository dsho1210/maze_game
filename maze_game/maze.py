# Import the module
import pygame as pg
# Create the window
WIDTH = 800
HEIGHT = 800
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Hello world!')
# Create a clock object
clock = pg.time.Clock()



class ImageSprite(pg.sprite.Sprite):
    def __init__(self, filename, position, size, speed=(0,0)):
        self.image = pg.image.load(filename)
        self.image = pg.transform.scale(self.image, size)
        self.rect = pg.Rect(position, size)
        self.speed = pg.Vector2(speed)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Enemy(ImageSprite):
    def set_limits(self, A, B):
        self.A = pg.Vector2(A)
        self.B = pg.Vector2(B)
        self.rect.topleft = self.A
    def update(self):
        if self.rect.top < self.A.y or self.rect.bottom > self.B.y:
            self.speed.y *= -1 
        if self.rect.left < self.A.x or self.rect.right > self.B.x:
            self.speed.x *= -1 
        self.rect.topleft += self.speed 

class Player(ImageSprite):
    def update(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x-=self.speed.x
        if keys[pg.K_d]:
            self.rect.x+=self.speed.x
        if keys[pg.K_w]:
            self.rect.y-=self.speed.y
        if keys[pg.K_s]:
            self.rect.y+=self.speed.y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    
    def __init__(self, filename, position, size, speed=(0,0) ):
        super().__init__(filename, position, size, speed)
        self.original_pos = position
    def reset(self):
        self.rect.topleft = self.original_pos

enemy = Enemy(filename='monster.png', position=(300,300), size=(80,80), speed=(8,8))
enemy.set_limits(A =(100,100), B=(600,500))
goal = ImageSprite(filename= '')
image = Player(filename="269974010_329444699185740_6542676387358284180_n.jpg", position=(400, 320), size=(80,80), speed = (10,10))



# Create the MAIN loop
while not pg.event.peek(pg.QUIT):
    window.fill('white')
    image.update()
    enemy.update()
    image.draw(window)
    enemy.draw(window)
    # update the screen
    pg.display.update()
    # tick the clock
    clock.tick(60)