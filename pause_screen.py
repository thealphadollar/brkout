from start_screen import *
from global_funcs import *
from global_objects import *
from constants import *
import pygame
import os

def pause_game(screen,clock):
    oldtime = pygame.time.get_ticks()
    pause_ball = Ball(130,140) # Initializing pause_ball
    option = 0
    # Giving a delay of 200 ms
    while pygame.time.get_ticks() - oldtime < 200:
        pass
        
    oldtime = pygame.time.get_ticks()
    while True:
        clock.tick(FPS)
        
        newtime = pygame.time.get_ticks()
        delta_time = (newtime - oldtime)/10
        oldtime = newtime
        
        # checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                os._exit(0)
            
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE):
                return 
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                option += 3
                option %= 4
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                option += 1
                option %= 4
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if option == 0:
                    return 0
                if option == 1:
                    return 1
                if option == 2:
                    return 2
                if option == 3:
                    os._exit(0)
        
        # ball updation
        pause_ball.menu_screen_move(delta_time)
        pause_ball.check_collide_wall()
        pause_ball.check_collide_options()
       
        # display update
        screen.fill(black)
        draw_walls(screen, 100, 30)
        
        # displaying highlighted options
        if option == 0:
            disp_text(screen, "RESUME",(scr_width / 2, scr_height/2 - 120), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "RESUME",(scr_width / 2, scr_height/2 - 120), pause_text, pause_col)
        if option == 1:
            disp_text(screen, "RESTART",(scr_width / 2, scr_height/2 - 40), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "RESTART",(scr_width / 2, scr_height/2 - 40), pause_text, pause_col)
        if option == 2:
            disp_text(screen, "MAIN MENU",(scr_width / 2, scr_height/2 + 40), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "MAIN MENU",(scr_width / 2, scr_height/2 + 40), pause_text, pause_col)
        if option == 3:
            disp_text(screen, "QUIT",(scr_width / 2, scr_height/2 + 120), pause_text_s, pause_sel_col)
        else:
            disp_text(screen, "QUIT",(scr_width / 2, scr_height/2 + 120), pause_text, pause_col)
        
        # drawing a box
        pygame.draw.rect(screen, white, (scr_width/2 - 150, scr_height/2 - 180, 300, 360), 2)
        pygame.draw.rect(screen, white, (scr_width/2 - 158, scr_height/2 - 188, 316, 376), 3)
        pygame.draw.aaline(screen, white, (scr_width/2 - 158, scr_height/2 - 188), (scr_width/2 + 158, scr_height/2 - 188), 1)
        pygame.draw.aaline(screen, white, (scr_width/2 - 158, scr_height/2 - 188), (scr_width/2 - 158, scr_height/2 + 188), 1)
        pygame.draw.aaline(screen, white, (scr_width/2 + 158, scr_height/2 + 188), (scr_width/2 - 158, scr_height/2 + 188), 1)
        pygame.draw.aaline(screen, white, (scr_width/2 + 158, scr_height/2 + 188), (scr_width/2 + 158, scr_height/2 - 188), 1)
        
        #draw ball
        pause_ball.draw(screen)
        pygame.display.update()