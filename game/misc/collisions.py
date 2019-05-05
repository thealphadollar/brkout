###############################################
# Collision system
# normals returned in collison check functions
# are w.r.t to the first collider
################################################
from enum import Enum
import math


class Collider_Type(Enum):
    Circle = 1
    Rectangle = 2
    Point = 3


class Collider(object):
    def __init__(self, type):
        self.type = type


class Circle_Collider(Collider):
    def __init__(self, x, y, radius):
        super(Circle_Collider, self).__init__(Collider_Type.Circle)
        self.x = x
        self.y = y
        self.radius = radius


class Rect_Collider(Collider):
    def __init__(self, x, y, width, height):
        super(Rect_Collider, self).__init__(Collider_Type.Rectangle)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.topleft = math.atan2(-height / 2, -width / 2)
        self.topright = math.atan2(-height / 2, width / 2)
        self.bottomright = math.atan2(height / 2, width / 2)
        self.bottomleft = math.atan2(height / 2, -width / 2)


class Collision(object):
    def __init__(self):
        pass

    @staticmethod
    def check(collider1, collider2):
        if collider1.type is Collider_Type.Circle and collider2.type is Collider_Type.Rectangle:
            result = Collision.check_circle_rect(collider1, collider2)
            return result

        if collider1.type is Collider_Type.Circle and collider2.type is Collider_Type.Circle:
            result = Collision.check_circle_circle(collider1, collider2)
            return result

    @staticmethod
    def check_circle_rect(circle, rect):
        distance_x = circle.x - rect.x
        distance_y = circle.y - rect.y

        if abs(distance_x) > rect.width / 2 + circle.radius:
            return (0, 0)

        if abs(distance_y) > rect.height / 2 + circle.radius:
            return (0, 0)

        angle = math.atan2(distance_y, distance_x)

        if angle >= rect.topleft and angle <= rect.topright:
            return (0, -1)

        elif angle >= rect.topright and angle <= rect.bottomright:
            return (1, 0)

        elif angle >= rect.bottomright and angle < rect.bottomleft:
            return (0, 1)

        else:
            return (-1, 0)

    @staticmethod
    def check_circle_rects(circle_collider, rect_colliders):
        for rect_collider in rect_colliders:
            result = Collision.check_circle_rect(
                circle_collider, rect_collider)
            if result == (0, 0):
                continue
            else:
                return result

        return (0, 0)

    @staticmethod
    def check_circle_circle(collider_one, collider_two):
        distance_x = collider_one.x - collider_two.x
        distance_y = collider_one.y - collider_two.y

        distance = math.hypot(distance_x, distance_y)

        if distance > collider_one.radius + collider_two.radius:
            return (0, 0)
        else:
            return (distance_x / distance, distance_y / distance)
