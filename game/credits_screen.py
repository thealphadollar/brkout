# Credits scroll upwards
# Space bar pauses the credits
# Enter or Escape fastforwards

from global_funcs import *
from constants import *
import os
import pygame as pg


class Credits(pg.sprite.Sprite):
    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)
        self.x = scr_width/2
        self.y = scr_height + 120
        self.y1 = self.y + 170
        self.y2 = self.y1 + 100
        self.y3 = self.y2 + 100
        self.y4 = self.y3 + 100
        self.y5 = self.y4 + 100
        self.y6 = self.y5 + 100
        self.y7 = self.y6 + 100
        self.y8 = self.y7 + 100
        self.y9 = self.y8 + 100
        self.y10 = self.y9 + 100
        self.speed = -1
        self.dis = screen
        self.gamelogo = pygame.image.load(
            os.path.join(assets_directory, 'logo.png')).convert()
        self.rect = self.gamelogo.get_rect()
        self.rect.center = (self.x, self.y)
        self.color1 = blood_red
        self.color2 = wall_silver

    def update(self):
        keystate = pg.key.get_pressed()
        self.speed = -1
        if keystate[pg.K_RETURN] or keystate[pg.K_ESCAPE]:
            self.speed = -3
        if keystate[pg.K_SPACE]:
            self.speed = 0
        self.y += self.speed
        self.rect.center = (self.x, self.y)
        self.y1 = self.y + 170
        self.y2 = self.y1 + 130
        self.y3 = self.y2 + 60
        self.y4 = self.y3 + 100
        self.y5 = self.y4 + 60
        self.y6 = self.y5 + 100
        self.y7 = self.y6 + 60
        self.y8 = self.y7 + 60
        self.y9 = self.y8 + 100
        self.y10 = self.y9 + 60
        if self.y8 < 110:
            os._exit(0)

    def draw(self):
        self.dis.blit(self.gamelogo, self.rect)
        disp_text(self.dis, "Brk", (self.x - 85, self.y1),
                  game_title_text_large, orange)
        disp_text(self.dis, "OUT", (self.x + 85, self.y1),
                  game_title_text_small, white)
        disp_text(self.dis, "Leading and Mapping",
                  (self.x, self.y2), credits_name, self.color1)
        disp_text(self.dis, "Kousshik Raj", (self.x, self.y3),
                  credits_text, self.color2)
        disp_text(self.dis, "Planning and Forging Keys",
                  (self.x, self.y4), credits_name, self.color1)
        disp_text(self.dis, "Shivam Kumar Jha",
                  (self.x, self.y5), credits_text, self.color2)
        disp_text(self.dis, "Disguise And Distraction",
                  (self.x, self.y6), credits_name, self.color1)
        disp_text(self.dis, "www.zapsplat.com",
                  (self.x, self.y7), credits_text, self.color2)
        disp_text(self.dis, "opengameart.org",
                  (self.x, self.y8), credits_text, self.color2)
        disp_text(self.dis, "Special Thanks To",
                  (self.x, self.y9), credits_name, self.color1)
        disp_text(self.dis, "CODECLUB, IIT KGP", (self.x, self.y10),
                  credits_text, self.color2)


def credits_screen(screen, clock):
    cr = Credits(screen)
    while True:
        # Frames per second
        clock.tick(FPS)
        # If you want to close
        for event in pg.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                os._exit(0)
            if event.type == pg.QUIT:
                os._exit(0)

        cr.update()
        screen.fill(black)
        x = float(1)
        draw_walls(screen, post_brick_width, post_brick_height)
        while x <= scr_width:
            pg.draw.aaline(screen, wall_silver, (x, 0), (x, scr_height), 2)
            pg.draw.aaline(screen, wall_silver, (x+1, 0), (x, scr_height), 2)
            pg.draw.aaline(screen, wall_silver, (x+2, 0), (x, scr_height), 2)
            pg.draw.aaline(screen, wall_silver, (x+3, 0), (x, scr_height), 2)
            pg.draw.aaline(screen, wall_silver, (x, scr_height), (x, 0), 2)
            pg.draw.aaline(screen, wall_silver, (x+1, scr_height), (x, 0), 2)
            pg.draw.aaline(screen, wall_silver, (x+2, scr_height), (x, 0), 2)
            pg.draw.aaline(screen, wall_silver, (x+3, scr_height), (x, 0), 2)
            x += (float(scr_width-6)) / 9
        cr.draw()
        pg.display.update()
