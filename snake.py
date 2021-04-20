import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Sarka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 20)
 

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y]) 

 
 
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_list = []
    length_of_snake = 1

    draw_foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    draw_foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    foodx = draw_foodx
    foody = draw_foody
 
    while not game_over:
 
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press P to Play Again or Q to Quit", red, dis_width/4, dis_height/4)
            message("Your score: " + str(length_of_snake-1), red, 20, 0)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
 
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
 
        #if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #    game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        if x1 >= dis_width: x1 = 0
        if x1 < 0: x1 = dis_width 
        if y1 >= dis_height: y1 = 0
        if y1 < 0: y1 = dis_height 

        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
 
        for x in snake_list[:-1]:
            if x == snake_Head:
               game_close = True
 
        draw_snake(snake_block, snake_list)
        message("Your score: " + str(length_of_snake-1), red, 20, 0)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = draw_foodx
            foody = draw_foody
            length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()