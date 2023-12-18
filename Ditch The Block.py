from OpenGL.GL import *
from OpenGL.GLUT import *
from random import randint
from time import sleep
import random
import math

class MidpointLine:
    def __init__(self):
        self.__midpoint_points = []

    def find_zone(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            if dx >= 0 and dy >= 0:
                return 0
            elif dx <= 0 and dy >= 0:
                return 3
            elif dx <= 0 and dy <= 0:
                return 4
            elif dx >= 0 and dy <= 0:
                return 7
        else:
            if dx >= 0 and dy >= 0:
                return 1
            elif dx <= 0 and dy >= 0:
                return 2
            elif dx <= 0 and dy <= 0:
                return 5
            elif dx >= 0 and dy <= 0:
                return 6

    def convert_to_zone0(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return y1, -x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return -y1, x1
        elif zone == 7:
            return x1, -y1

    def convert_to_original_zone(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return -y1, x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return y1, -x1
        elif zone == 7:
            return x1, -y1

    def midpoint(self, x1, y1, x2, y2):
        glBegin(GL_POINTS)

        zone = self.find_zone(x1, y1, x2, y2)

        x1_to_z0, y1_to_z0 = self.convert_to_zone0(x1, y1, zone)
        x2_to_z0, y2_to_z0 = self.convert_to_zone0(x2, y2, zone)

        dy = y2_to_z0 - y1_to_z0
        dx = x2_to_z0 - x1_to_z0
        d = 2 * dy - dx
        d_E = 2 * dy
        d_NE = 2 * (dy - dx)

        x = x1_to_z0
        y = y1_to_z0

        original_x, original_y = self.convert_to_original_zone(x, y, zone)
        glVertex2f(original_x, original_y)

        while x <= x2_to_z0:
            self.__midpoint_points.append((original_x, original_y))

            if d < 0:
                x = x + 1
                d = d + d_E
            else:
                x = x + 1
                y = y + 1
                d = d + d_NE

            original_x, original_y = self.convert_to_original_zone(x, y, zone)
            glVertex2f(original_x, original_y)

        glEnd()

class MidpointCircle:
    def __init__(self):
        self.__radius = None
        self.__center_x = None
        self.__center_y = None
        self.__midpoint_points = []

    def set_circle_values(self, radius, center_x=0, center_y=0):
        self.__radius = radius
        self.__center_x = center_x
        self.__center_y = center_y

    def convert_to_other_zone(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return -y1, x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return y1, -x1
        elif zone == 7:
            return x1, -y1

    def ball(self, radius, center_x=0, center_y=0, angle=0.0):
        glPushMatrix()
        glTranslatef(center_x, center_y, 0.0)
        glRotatef(angle, 0.0, 0.0, 1.0)

        glBegin(GL_QUADS)
        glColor3f(255, 255, 0)

        glEnd()

        self.draw_circle(radius)

        glPopMatrix()

    def draw_circle(self, radius):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255, 255, 0)

        for i in range(360):
            angle = math.radians(i)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex2f(x, y)

        glEnd()

class Digits:
    def __init__(self):

        self.__midpoint_points = []

    def find_zone(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            if dx >= 0 and dy >= 0:
                return 0
            elif dx <= 0 and dy >= 0:
                return 3
            elif dx <= 0 and dy <= 0:
                return 4
            elif dx >= 0 and dy <= 0:
                return 7
        else:
            if dx >= 0 and dy >= 0:
                return 1
            elif dx <= 0 and dy >= 0:
                return 2
            elif dx <= 0 and dy <= 0:
                return 5
            elif dx >= 0 and dy <= 0:
                return 6

    def convert_to_zone0(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return y1, -x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return -y1, x1
        elif zone == 7:
            return x1, -y1

    def convert_to_original_zone(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return -y1, x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return y1, -x1
        elif zone == 7:
            return x1, -y1

    def midpoint(self, x1, y1, x2, y2):
        glBegin(GL_POINTS)

        zone = self.find_zone(x1, y1, x2, y2)

        x1_to_z0, y1_to_z0 = self.convert_to_zone0(x1, y1, zone)
        x2_to_z0, y2_to_z0 = self.convert_to_zone0(x2, y2, zone)

        dy = y2_to_z0 - y1_to_z0
        dx = x2_to_z0 - x1_to_z0
        d = 2 * dy - dx
        d_E = 2 * dy
        d_NE = 2 * (dy - dx)

        x = x1_to_z0
        y = y1_to_z0

        original_x, original_y = self.convert_to_original_zone(x, y, zone)
        glVertex2f(original_x, original_y)

        while x <= x2_to_z0:
            self.__midpoint_points.append((original_x, original_y))

            if d < 0:
                x = x + 1
                d = d + d_E
            else:
                x = x + 1
                y = y + 1
                d = d + d_NE

            original_x, original_y = self.convert_to_original_zone(x, y, zone)
            glVertex2f(original_x, original_y)

        glEnd()

    def draw_digit(self, digit, offset_x=0, offset_y=0, digit_position_x=0):
        digit_lights = {
            0: [self.l_t, self.l_b, self.b, self.r_b, self.r_t, self.t],
            1: [self.r_b, self.r_t],
            2: [self.l_b, self.b, self.r_t, self.t, self.m],
            3: [self.b, self.r_b, self.r_t, self.t, self.m],
            4: [self.l_t, self.r_b, self.r_t, self.m],
            5: [self.l_t, self.b, self.r_b, self.t, self.m],
            6: [self.l_t, self.l_b, self.b, self.r_b, self.t, self.m],
            7: [self.r_b, self.r_t, self.t],
            8: [self.l_t, self.l_b, self.b, self.r_b, self.t, self.r_t, self.m],
            9: [self.l_t, self.b, self.r_b, self.t, self.r_t, self.m]
        }

        if digit == "00":
            show_digits = "00"
        else:
            show_digits = digit

        first_digit = int(show_digits[0])
        if int(digit) > 9:
            second_digit = int(show_digits[1])

        if int(digit) <= 9:
            first_digit = 0
            second_digit = int(show_digits[0])

        for i in digit_lights[first_digit]:
            i(x=digit_position_x + offset_x, y=250 + offset_y)

        for i in digit_lights[second_digit]:
            i(x=digit_position_x + offset_x, y=250 + offset_y, adjust=250)

    def get_midpoint_points(self):
        return self.__midpoint_points

    def r_t(self, adjust=0, x=0, y=0):
        # Right Top
        self.midpoint(400 + adjust + x, 400 + y, 400 + adjust + x, 600 + y)

    def r_b(self, adjust=0, x=0, y=0):
        # Right Bottom
        self.midpoint(400 + adjust + x, 200 + y, 400 + adjust + x, 400 + y)

    def l_t(self, adjust=0, x=0, y=0):
        # Left Top
        self.midpoint(200 + adjust + x, 400 + y, 200 + adjust + x, 600 + y)

    def l_b(self, adjust=0, x=0, y=0):
        # Left Bottom
        self.midpoint(200 + adjust + x, 200 + y, 200 + adjust + x, 400 + y)

    def b(self, adjust=0, x=0, y=0):
        # Bottom
        self.midpoint(200 + adjust + x, 200 + y, 400 + adjust + x, 200 + y)

    def t(self, adjust=0, x=0, y=0):
        # Top
        self.midpoint(200 + adjust + x, 600 + y, 400 + adjust + x, 600 + y)

    def m(self, adjust=0, x=0, y=0):
        # Middle
        self.midpoint(200 + adjust + x, 400 + y, 400 + adjust + x, 400 + y)


class text_display:
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0, title="Ditch The Block", pixel_size=15):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.title = title
        self.pixel_size = pixel_size

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(self.title)
        glClearColor(0, 0, 0, 0),
        glutDisplayFunc(self.show_screen)

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(25)
        glLoadIdentity()

    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)

        self.text()

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def game_over_text(self, x=0, y=0):
        self.g(adjust=0, x=10 + x, y=10 + y)
        self.a(adjust=150, x=10 + x, y=10 + y)
        self.m(adjust=300, x=10 + x, y=10 + y)
        self.e(adjust=450, x=10 + x, y=10 + y)
        self.o(adjust=750, x=10 + x, y=10 + y)
        self.v(adjust=900, x=10 + x, y=10 + y)
        self.e(adjust=1050, x=10 + x, y=10 + y)
        self.r(adjust=1200, x=10 + x, y=10 + y)

    def health_text(self, x=5, y=10):
        self.h(adjust=50, x=10 + x, y=10 + y)
        self.e(adjust=180, x=10 + x, y=10 + y)
        self.a(adjust=310, x=10 + x, y=10 + y)
        self.l(adjust=440, x=10 + x, y=10 + y)
        self.t(adjust=570, x=10 + x, y=10 + y)
        self.h(adjust=700, x=10 + x, y=10 + y)

    def score_text(self, x=0, y=0):
        self.s(adjust=50, x=10 + x, y=10 + y)
        self.c(adjust=180, x=10 + x, y=10 + y)
        self.o(adjust=310, x=10 + x, y=10 + y)
        self.r(adjust=440, x=10 + x, y=10 + y)
        self.e(adjust=570, x=10 + x, y=10 + y)

    def g(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 80 + adjust, y + 0)  # Bottom
        line.midpoint(x + 20 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle


    def a(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right
        line.midpoint(x + 0 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle

    def m(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 45 + adjust, y + 10 + 80, x + 80 + adjust, y + 60 + 80)
        line.midpoint(x + 40 + adjust, y + 10 + 80, x + 0 + adjust, y + 60 + 80)

    def e(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 0 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        line.midpoint(x + 0 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def o(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 00, x + 80 + adjust, y + 150)  # Right
        line.midpoint(x + 0 + adjust, y + 0, x + 80 + adjust, y + 0)  # Bottom

    def v(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 150, x + 45 + adjust, y + 0)  # Left
        line.midpoint(x + 45 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right

    def r(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 70, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 0 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle
        line.midpoint(x + 80 + adjust, y + 0, x + 30 + adjust, y + 65)  # Bottom Left Corner

    def h(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right
        line.midpoint(x + 0 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle,

    def l(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 80 + adjust, y + 0)  # Bottom

    def t(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 35 + adjust, y + 0, x + 35 + adjust, y + 150)  # Left

    def s(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 70, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 0 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 70 + adjust, y + 0, x + 70 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        line.midpoint(x + 0 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def c(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 0 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom


scale_radius = 0
score = 0
health = 99

line = MidpointLine()
circle = MidpointCircle()
digits = Digits()
display_text = text_display()
colors = 0, 0, 0


ball_x = 0
ball_y = -600
ball_radius = 80

obj1_x = randint(-600, 600)
obj1_y = 900
obj1_speed = 10

obj2_x = randint(-600, 600)
obj2_y = 900
obj2_speed = 12

obj3_x = randint(-600, 600)
obj3_y = 900
obj3_speed = 20

obj4_x = randint(-600, 600)
obj4_y = 900
obj4_speed = 14

obj5_x = randint(-600, 600)
obj5_y = 900
obj5_speed = 22

obj6_x = randint(-600, 600)
obj6_y = 900
obj6_speed = 10

obj7_x = randint(-600, 600)
obj7_y = 900
obj7_speed = 8

obj8_x = randint(-600, 600)
obj8_y = 900
obj8_speed = 14

obj9_x = randint(-600, 600)
obj9_y = 900
obj9_speed = 20

obj10_x = randint(-600, 600)
obj10_y = 900
OBJECT10_SPEED = 12


inc_speed = 2

game_over = False


def player_health_system():
    global ball_radius, health, game_over

    health -= 1
    if health <= 0:
        health = 0
        game_over = True

from pynput.keyboard import Key, Controller
auto_key_press = Controller()


def update():
    global scale_radius, colors, obj1_y, obj1_x, obj2_y, obj2_x, obj3_y, obj3_x, obj4_y, obj4_x, obj5_y, obj5_x, obj1_speed, obj2_speed, obj3_speed, obj4_speed, obj5_speed, obj6_y, obj6_x, obj7_y, obj7_x, obj8_y, obj8_x, obj9_y, obj9_x, obj10_y, obj10_x, obj6_speed, obj7_speed, obj8_speed, obj9_speed, OBJECT10_SPEED, ball_y, ball_x, inc_speed, game_over

    while True:
        inc_speed += 0.0001
        colors = 1, 1, 1
        auto_key_press.press(",")
        sleep(0.1)

        if game_over:
            break

        obj1_y += - obj1_speed * inc_speed
        if obj1_y < - 900:
            obj1_y = 900
            obj1_x = randint(-600, 600)

        obj2_y += - obj2_speed * inc_speed
        if obj2_y < - 900:
            obj2_y = 900
            obj2_x = randint(-600, 600)

        obj3_y += - obj3_speed * inc_speed
        if obj3_y < - 900:
            obj3_y = 900
            obj3_x = randint(-600, 600)

        obj4_y += - obj4_speed * inc_speed
        if obj4_y < - 900:
            obj4_y = 900
            obj4_x = randint(-600, 600)

        obj5_y += - obj5_speed * inc_speed
        if obj5_y < - 900:
            obj5_y = 900
            obj5_x = randint(-600, 600)

        obj6_y += - obj6_speed * inc_speed
        if obj6_y < - 900:
            obj6_y = 900
            obj6_x = randint(-600, 600)

        obj7_y += - obj7_speed * inc_speed
        if obj7_y < - 900:
            obj7_y = 900
            obj7_x = randint(-600, 600)

        obj8_y += - obj8_speed * inc_speed
        if obj8_y < - 900:
            obj8_y = 900
            obj8_x = randint(-600, 600)

        obj9_y += - obj9_speed * inc_speed
        if obj9_y < - 900:
            obj9_y = 900
            obj9_x = randint(-600, 600)

        obj10_y += - obj5_speed * inc_speed
        if obj10_y < - 900:
            obj10_y = 900
            obj10_x = randint(-600, 600)

    
        glutPostRedisplay()


def score_increase():
    global score
    while True:
        sleep(1)
        glutPostRedisplay()
        score += 1
        if game_over:
            break


def restart():
    global y, scale_radius, colors, obj1_y, obj1_x, obj2_y, obj2_x, obj3_y, obj3_x, obj4_y, obj4_x, obj5_y, obj5_x, obj1_speed, obj2_speed, obj3_speed, obj4_speed, obj5_speed, inc_speed, ball_x, ball_y, ball_radius, score, obj6_y, obj6_x, obj7_y, obj7_x, obj8_y, obj8_x, obj9_y, obj9_x, obj10_y, obj10_x, obj6_speed, obj7_speed, obj8_speed, obj9_speed, OBJECT10_SPEED

    ball_x = 0
    ball_y = - 600
    ball_radius = 65

    score = 0

    obj1_x = randint(-600, 600)  # - 600 => 600
    obj1_y = 900
    obj1_speed = 10

    obj2_x = randint(-600, 600)
    obj2_y = 900
    obj2_speed = 12

    obj3_x = randint(-600, 600)
    obj3_y = 900
    obj3_speed = 20

    obj4_x = randint(-600, 600)
    obj4_y = 900
    obj4_speed = 14

    obj5_x = randint(-600, 600)
    obj5_y = 900
    obj5_speed = 22

    obj6_x = randint(-600, 600)
    obj6_y = 900
    obj6_speed = 10

    obj7_x = randint(-600, 600)
    obj7_y = 900
    obj7_speed = 8

    obj8_x = randint(-600, 600)
    obj8_y = 900
    obj8_speed = 14

    obj9_x = randint(-600, 600)
    obj9_y = 900
    obj9_speed = 20

    obj10_x = randint(-600, 600)
    obj10_y = 900
    OBJECT10_SPEED = 12

    inc_speed = 2

def block(x, y):
    num_points = 100
    radius = 5
    glPointSize(60)
    glBegin(GL_POINTS)
    glColor3f(255, 255, 255)

    for _ in range(num_points):
        dx = random.uniform(-radius, radius)
        dy = random.uniform(-radius, radius)

        if dx**2 + dy**2 <= radius**2:
            glVertex2f(x + dx, y + dy)

    glEnd()

from threading import Thread

class ditch_the_block:
    def __init__(self, window_x=500, window_y=500, win_pos_x=0, win_pos_y=0, pixel=1):
        self.win_size_x = window_x
        self.win_size_y = window_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.pixel_size = pixel
    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(b'Ditch The Block')
        glClearColor(0, 0, 0, 0)
        glutDisplayFunc(self.show_screen)

        glutKeyboardFunc(self.buttons)
        

        animation_thread = Thread(target=update)
        animation_thread.start()

        global score_thread
        score_thread = Thread(target=score_increase)
        score_thread.start()

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    def buttons(self, key, x, y):
        global ball_y, ball_x, ball_radius, game_over, health, score

        move = 50

        if key == b"w":
            ball_y += move
        if key == b"a" and ball_x > - 600:
            ball_x -= move
        if key == b"s":
            ball_y -= move
        if key == b"d" and ball_x < 600:
            ball_x += move

        
        if key == b"r":
            game_over = False
            ball_radius = 65
            health = 99

            restart = Thread(target=update)
            restart.start()

            score = 0
            restart_score = Thread(target=score_increase)
            restart_score.start()


        if key ==b"e":
            self.exit_game()

        if ball_y < - self.win_size_y:
            ball_y = self.win_size_y

        if ball_x < - self.win_size_x:
            ball_x = self.win_size_x

        if ball_y > self.win_size_y:
            ball_y = - self.win_size_y

        if ball_x > self.win_size_x:
            ball_x = - self.win_size_x


        if ball_y - ball_radius <= obj1_y <= ball_y + ball_radius and ball_x - ball_radius <= obj1_x <= ball_x + ball_radius:
            print("Collision with Object 1")
            player_health_system()
        if ball_y - ball_radius <= obj2_y <= ball_y + ball_radius and ball_x - ball_radius <= obj2_x <= ball_x + ball_radius:
            print("Collision with Object 2")
            player_health_system()
        if ball_y - ball_radius <= obj3_y <= ball_y + ball_radius and ball_x - ball_radius <= obj3_x <= ball_x + ball_radius:
            print("Collision with Object 3")
            player_health_system()
        if ball_y - ball_radius <= obj4_y <= ball_y + ball_radius and ball_x - ball_radius <= obj4_x <= ball_x + ball_radius:
            print("Collision with Object 4")
            player_health_system()
        if ball_y - ball_radius <= obj5_y <= ball_y + ball_radius and ball_x - ball_radius <= obj5_x <= ball_x + ball_radius:
            print("Collision with Object 5")
            player_health_system()
        if ball_y - ball_radius <= obj6_y <= ball_y + ball_radius and ball_x - ball_radius <= obj6_x <= ball_x + ball_radius:
            print("Collision with Object 6")
            player_health_system()
        if ball_y - ball_radius <= obj7_y <= ball_y + ball_radius and ball_x - ball_radius <= obj7_x <= ball_x + ball_radius:
            print("Collision with Object 7")
            player_health_system()
        if ball_y - ball_radius <= obj8_y <= ball_y + ball_radius and ball_x - ball_radius <= obj8_x <= ball_x + ball_radius:
            print("Collision with Object 8")
            player_health_system()
        if ball_y - ball_radius <= obj9_y <= ball_y + ball_radius and ball_x - ball_radius <= obj9_x <= ball_x + ball_radius:
            print("Collision with Object 9")
            player_health_system()
        if ball_y - ball_radius <= obj10_y <= ball_y + ball_radius and ball_x - ball_radius <= obj10_x <= ball_x + ball_radius:
            print("Collision with Object 10")
            player_health_system()

        glutPostRedisplay()


    def exit_game(self):
        glutLeaveMainLoop()

    
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        display_text.health_text(-1800, 600)
        display_text.score_text(950, 600)

        glPointSize(2)
        self.obstacle(obj1_x, obj1_y)
        self.obstacle(obj2_x, obj2_y)
        self.obstacle(obj3_x, obj3_y)
        self.obstacle(obj4_x, obj4_y)
        self.obstacle(obj5_x, obj5_y)
        self.obstacle(obj6_x, obj6_y)
        self.obstacle(obj7_x, obj7_y)
        self.obstacle(obj8_x, obj8_y)
        self.obstacle(obj9_x, obj9_y)
        self.obstacle(obj10_x, obj10_y)

        glColor3f(1, 1, 1)
        circle.ball(ball_radius, ball_x, ball_y)
       
        glPointSize(5)

        
        score_and_health_text = Digits()

        glColor3f(colors[0], colors[1], colors[2])
        score_and_health_text.draw_digit(f"{score}", offset_x=10, offset_y=-350 + 10, digit_position_x= 850)

        glColor3f(colors[2], colors[1], colors[0])
        score_and_health_text.draw_digit(f"{health}", digit_position_x=-1900 + 10, offset_x=10, offset_y=-300)
        
        
        if game_over:
            glColor3f(0, 0, 1)
            glColor3f(1, 0, 0)
            display_text.game_over_text(-650, 0)

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def obstacle(self, obstacle_x, obstacle_y):
        if randint(0, 1) == 0:
            block(obstacle_x, obstacle_y)
        else:
            block(obstacle_x, obstacle_y)


ball_survive = ditch_the_block(window_x=1920, window_y=900, pixel=1)

ball_survive.initialize()
ball_survive.start_main_loop()