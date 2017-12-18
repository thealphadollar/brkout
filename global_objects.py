from constants import *
import random
import math


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = ball_radius
        self.mass = ball_mass
        self.menu_speed = menu_ball_speed
        self.speed = main_ball_speed
        self.angle = random.uniform(-math.pi, math.pi)

    def menu_screen_move(self, delta_time):
        self.x += math.sin(self.angle) * self.menu_speed * delta_time
        self.y += math.cos(self.angle) * self.menu_speed * delta_time

    def main_screen_move(self, delta_time):
        self.x += math.sin(self.angle) * self.speed * delta_time
        self.y += math.cos(self.angle) * self.speed * delta_time
        if self.speed > 0:
            self.speed -= (friction * delta_time)
        else:
            self.speed = 0

    # function to check collision with menu wall
    def check_collide_wall(self):
        if self.x < wall_brick_height + self.radius:
            self.x = wall_brick_height + self.radius
            self.angle = -self.angle

        if self.x > scr_width - wall_brick_height - self.radius:
            self.x = scr_width - wall_brick_height - self.radius
            self.angle = -self.angle

        if self.y < wall_brick_height + self.radius:
            self.y = wall_brick_height + self.radius
            self.angle = math.pi - self.angle

        if self.y > scr_height - wall_brick_height - self.radius:
            self.y = scr_height - wall_brick_height - self.radius
            self.angle = math.pi - self.angle

    # function to check collision with color palette
    def check_collide_palette(self):
        if (self.y < scr_height/2 + 140 + self.radius) and (self.y > scr_height/2 + 40 - self.radius):
            if (self.x < scr_width/2 + 200 + self.radius) and (self.x > scr_width/2 + 200 + self.radius - 15):
                self.x = scr_width/2 + 200 + self.radius
                self.angle = -self.angle
            elif (self.x > scr_width/2 - 200 - self.radius) and (self.x < scr_width/2 - 200 - self.radius + 15):
                self.x = scr_width/2 - 200 - self.radius
                self.angle = -self.angle

        if (self.x < scr_width/2 + 200 + self.radius) and (self.x > scr_width/2 - 200 - self.radius):
            if (self.y < scr_height/2 + 140 + self.radius) and (self.y > scr_height/2 + 140 + self.radius - 15):
                self.y = scr_height/2 + 140 + self.radius
                self.angle = math.pi - self.angle
            elif (self.y > scr_height/2 + 40 - self.radius) and (self.y < scr_height/2 + 40 - self.radius + 15):
                self.y = scr_height/2 + 40 - self.radius
                self.angle = math.pi - self.angle

    # checks collision with game boundary
    def check_escape(self):
        # right side
        if self.x >= scr_width - 100:
            self.angle = -self.angle
            #return True
        # left side
        elif self.x <= 100:
            self.angle = -self.angle
            #return True
        # bottom
        if self.y >= scr_height:
            self.angle = math.pi - self.angle
            #return True
        elif self.y <= 40:
            self.angle = math.pi - self.angle
            #return True
        #return False

    # check collision with brick

    # horizontal brick
    def collision_horizontal_brick(self, horizontal_brick):
        # lower side
        # returns true if collision takes place
        did_collide = False
        x, y = horizontal_brick.get_pos()
        if (self.x > x - self.radius) and (self.x < x + horizontal_brick_width + self.radius):
            if (self.y < y + horizontal_brick_height + self.radius) and (self.y > y + horizontal_brick_height):
                self.y = y + horizontal_brick_height + self.radius
                self.angle = math.pi - self.angle
                did_collide = True
        # upper side
        elif (self.x > x - self.radius) and (self.x < x + horizontal_brick_width + self.radius):
            if (self.y > y - self.radius) and (self.y < y):
                self.y = y - self.radius
                self.angle = math.pi - self.angle
                did_collide = True
        # left side
        if (self.y < y + horizontal_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x > x - self.radius) and (self.x < x):
                self.x = x - self.radius
                self. angle = -self.angle
                did_collide = True
        # right side
        elif (self.y < y + horizontal_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x < x + horizontal_brick_width + self.radius) and (self.x > x + horizontal_brick_width):
                self.x = x + horizontal_brick_width + self.radius
                self.angle = -self.angle
                did_collide = True
        return did_collide

    # vertical brick
    def collision_vertical_brick(self, vertical_brick):
        # lower side
        # returns true is collision takes place
        did_collide = False
        x, y = vertical_brick.get_pos()
        if (self.x > x - self.radius) and (self.x < x + vertical_brick_width + self.radius):
            if (self.y < y + vertical_brick_height + self.radius) and (self.y > y + vertical_brick_height):
                self.y = y + vertical_brick_height + self.radius
                self.angle = math.pi - self.angle
                did_collide = True
        # upper side
        elif (self.x > x - self.radius) and (self.x < x + vertical_brick_width + self.radius):
            if (self.y > y - self.radius) and (self.y < y):
                self.y = y - self.radius
                self.angle = math.pi - self.angle
                did_collide = True
        # left side
        if (self.y < y + vertical_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x > x - self.radius) and (self.x < x):
                self.x = x - self.radius
                self. angle = -self.angle
                did_collide = True
        # right side
        elif (self.y < y + vertical_brick_height + self.radius) and (self.y > y - self.radius):
            if (self.x < x + vertical_brick_width + self.radius) and (self.x > x + vertical_brick_width):
                self.x = x + vertical_brick_width + self.radius
                self.angle = -self.angle
                did_collide = True
        return did_collide

    # define collision with striker
    def collision_striker(self, striker):

        # distance between striker and ball
        dx = self.x - striker.x
        dy = self.y - striker.y
        distance = math.hypot(dx, dy)

        # if not colliding return
        if distance > striker.radius + self.radius:
            return

        # using elastic collision
        approach_angle = math.atan(dx/dy)
        ball_velocity_along_line = math.cos(approach_angle - self.angle) * self.speed
        ball_velocity_perp_line = math.sin(approach_angle - self.angle) * self.speed
        striker_velocity_along_line = (striker.x_velocity * math.sin(approach_angle)) + (striker.y_velocity * math.cos(approach_angle))
        striker_velocity_x_perp_line = striker.x_velocity * math.cos(approach_angle)
        striker_velocity_y_perp_line = striker.y_velocity * math.sin(approach_angle)
        # now this is a case of head on collision
        # setting before collision variables
        M = striker.mass
        m = self.mass
        U = striker_velocity_along_line
        u = ball_velocity_along_line
        # velocities after elastic collision
        striker_velocity_along_line = (((M-m) * U) + (2 * m * u)) / (M + m)
        ball_velocity_along_line = U - u + striker_velocity_along_line
        # setting values after collision
        striker.x_velocity = math.hypot(striker_velocity_along_line, striker_velocity_x_perp_line)
        striker.y_velocity = math.hypot(striker_velocity_along_line, striker_velocity_y_perp_line)
        self.speed = math.hypot(ball_velocity_along_line, ball_velocity_perp_line)
        ball_x_velocity = ball_velocity_along_line * math.sin(approach_angle) - ball_velocity_perp_line * math.cos(approach_angle)
        ball_y_velocity = ball_velocity_along_line * math.cos(approach_angle) + ball_velocity_perp_line * math.sin(approach_angle)
        self.angle = math.atan(ball_x_velocity / ball_y_velocity)

        if self.speed > MAX_BALL_SPEED:
            self.speed = MAX_BALL_SPEED
        if abs(striker.x_velocity) > MAX_STRIKER_SPEED:
            striker.x_velocity = MAX_STRIKER_SPEED * (striker.x_velocity / abs(striker.x_velocity))
        if abs(striker.y_velocity) > MAX_STRIKER_SPEED:
            striker.y_velocity = MAX_STRIKER_SPEED * (striker.y_velocity / abs(striker.y_velocity))


    def draw(self, screen):
        pygame.draw.circle(screen, yellow, (int(self.x), int(self.y)), self.radius)


# striker class
class Striker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.radius = striker_radius
        self.mass = striker_mass

    def update(self, delta_time):
        self.x += self.x_velocity * delta_time
        self.y += self.y_velocity * delta_time
        if self.x_velocity > 0:
            self.x_velocity -= striker_friction * delta_time
            if self.x_velocity < 0:
                self.x_velocity = 0
        elif self.x_velocity < 0:
            self.x_velocity += striker_friction * delta_time
            if self.x_velocity > 0:
                self.x_velocity = 0
        if self.y_velocity > 0:
            self.y_velocity -= striker_friction * delta_time
            if self.y_velocity < 0:
                self.y_velocity = 0
        elif self.y_velocity < 0:
            self.y_velocity += striker_friction * delta_time
            if self.y_velocity > 0:
                self.y_velocity = 0

    def check_bound(self):
        dx = self.x - main_game_middle_x
        dy = self.y - main_game_middle_y
        distance = math.hypot(dx, dy)
        if distance < strike_bound_radius - self.radius:
            return

        self.x_velocity = -self.x_velocity
        self.y_velocity = -self.y_velocity

        angle = math.atan(dx/dy)
        self.x = (strike_bound_radius - self.radius) * math.sin(angle)
        self.y = (strike_bound_radius - self.radius) * math.cos(angle)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, black, (self.x, self.y), self.radius, 1)
        pygame.draw.circle(screen, black, (self.x, self.y), self.radius - 10, 1)
        pygame.draw.circle(screen, black, (self.x, self.y), self.radius - 30, 1)