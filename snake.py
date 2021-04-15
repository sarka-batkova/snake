import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
dis_width = 800
dis_height = 600 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Sarka')

snake_block = 10
snake_speed = 3
 
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameLoop():
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0       
    y1_change = 0
    score = 0

    game_over = False
    # game_close = False

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10

 
    while not game_over:

        # while game_close == True:
        #     dis.fill(white)
        #     message("You Lost! Press Q-Quit or C-Play Again", red)
        #     pygame.display.update()
 
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_q:
        #                 game_over = True
        #                 game_close = False
        #             if event.key == pygame.K_c:
        #                 gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

    
        x1 += x1_change
        y1 += y1_change

        if x1 >= dis_width: x1 = 0
        if x1 < 0: x1 = dis_width 
        if y1 >= dis_height: y1 = 0
        if y1 < 0: y1 = dis_height 
        

        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            score += 1
            message("score", red)
    
        clock.tick(snake_speed)

 
    pygame.quit()
    quit()

gameLoop()
