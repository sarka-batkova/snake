import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
 
display_width = 600
display_height = 400
 
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Sarka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 20)
 

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y]) 
 
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def draw_food(dimension):
    return round(random.randrange(0, dimension - snake_block) / 10.0) * 10.0

 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = display_width / 2
    y1 = display_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_list = []
    length_of_snake = 1
 
    foodx = draw_food(display_width)
    foody = draw_food(display_height)
 
    while not game_over:
 
        while game_close == True:
            display.fill(white)
            message("You Lost! Press P to Play Again or Q to Quit", red, display_width/4, display_height/4)
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
        display.fill(white)

        if x1 >= display_width: x1 = 0
        if x1 < 0: x1 = display_width 
        if y1 >= display_height: y1 = 0
        if y1 < 0: y1 = display_height 

        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
 
        for x in snake_list[:-1]:
            if x == snake_head:
               game_close = True
 
        draw_snake(snake_block, snake_list)
        message("Your score: " + str(length_of_snake-1), red, 20, 0)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = draw_food(display_width)
            foody = draw_food(display_height)
            length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()