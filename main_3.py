import pygame
from pygame.locals import *
pygame.init()

# Window dimention
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Road parameters
ROAD_W = 400
ROADMARK_W = 10


# Set window size
screen = pygame.display.set_mode( SIZE )

# Set window title
pygame.display.set_caption("Car game in Pygame")

# Set icon
ICON = pygame.image.load("car-icon.png")
pygame.display.set_icon(ICON)

# Set background color
screen.fill((60, 0, 0))



pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

# Apply changes
pygame.display.update()

### P3.1 - Load car player image
car_player = pygame.image.load("car_player.png")
car_player_loc = car_player.get_rect()
car_player_loc.center = SCREEN_WIDTH/2 + ROAD_W/4, SCREEN_HEIGHT*0.9

### P3.4 - Load car enemy image
car_enemy = pygame.image.load("car_enemy.png")
car_enemy_loc = car_player.get_rect()
car_enemy_loc.center = SCREEN_WIDTH/2 - ROAD_W/4, SCREEN_HEIGHT*0.2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        #print( event )
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
            if event.key in [K_a, K_LEFT]:
                car_player_loc = car_player_loc.move(-ROAD_W/2, 0)

            if event.key in [K_d, K_RIGHT]:
                car_player_loc = car_player_loc.move(ROAD_W/2, 0)

        # Draw the road
    pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

    # Draw the roadmark
    pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

    # Draw the white lines
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

    ### P3.2 - Draw player car
    screen.blit(car_player, car_player_loc)
    
    ### P3.5 - Draw enemy car
    screen.blit(car_enemy, car_enemy_loc)
    
    ### P3.3 - Update the app
    pygame.display.update()
            
