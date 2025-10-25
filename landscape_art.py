
# <-------------------------- CREATING AN ANIMATED SUNSET LANDSCAPE WITH PYGAME 🌅 -------------------------------->

# Import the pygame and random modules
import pygame
from random import randrange

# Give the drawing positions
pygame.init()
WIDTH = 640
HEIGHT = 360
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# <------------------- INITIALIZE GLOBAL VARIABLES 🌎 ------------------------>

frames = 0  # Counter variable
daytime = True # Keeps track of day and night
position1 = True # Makes objects appear move a little

# Star colours
stars_r = 2
star_colour_1 = "white"
star_colour_2 = "#fcdf00"

# Moving clouds
cloud1_x = randrange(-500, 101)
cloud1_y = randrange(29, 113)
cloud1_r = randrange(30, 37)
cloud1_speed = randrange(2, 4)

cloud2_x = randrange(-500, 101)
cloud2_y = randrange(29, 113)
cloud2_r = randrange(30, 37)
cloud2_speed = randrange(2, 4)

cloud3_x = randrange(-500, 101)
cloud3_y = randrange(29, 113)
cloud3_r = randrange(30, 37)
cloud3_speed = randrange(2, 4)

# Sun & birds :)
sun_x = 300
sun_y = 100
sun_colour = (255, 218, 69)
birds_x = 168

# Some landscape features

# River
river_colour_r = 183
river_colour_g = 203
river_colour_b = 255

# Trees
tree1_x = 100
tree1_y = 270
tree2_x = 200
tree2_y = 170
trees12_rect_colours = (152, 123, 72)
trees12_colours = (64, 198, 68)
trees12_shades = (36, 172, 41)

tree3_x = 525
tree3_y = 270
tree4_x = 400
tree4_y = 170
trees34_rect_colours = (124, 100, 58)
trees34_colours = (108, 198, 111)
trees34_shades = (93, 171, 96)

trees13_w = 20
trees13_h = 80
trees13_r = 30

trees24_w = 4
trees24_h = 16
trees24_r = 15

# <---------------------------------------- WHILE LOOP 🔄 --------------------------------------------->

running = True
while running:

    # <-------------------- EVENT HANDLING ⁉️ ------------------------>

    # Used to catch mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # This block of code makes the stars, birds, and river look animated
    if frames <= 10: # This code runs while "frames" is less than or equal to '10'
        position1 = True
    elif frames <= 20: # If "frames" is instead greater than 10 but less than or equal to '20', "position1" will be set to 'False'
        position1 = False
    else: # The only other case is that if "frames" is larger than '20', we set it back to '0' so "position1" could switch back to being 'True'
        frames = 0

    if daytime: # This block executes when it is daytime
        cloud_colours = (255, 255, 255)
        sun_colour = (255, 218, 69)
        sky_bottom_colour = pygame.Color(175, 255, 235)
        sky_top_colour = pygame.Color(130, 185, 245)
        grass_colour = pygame.Color(198, 252, 126)
        river_colour_r += 0.5
        river_colour_g += 0.25

    else: # This block executes when it is nighttime
        cloud_colours = (0, 0, 0)
        sun_colour = (224, 224, 224)
        sky_top_colour = pygame.Color(15, 50, 92)
        sky_bottom_colour = pygame.Color(26, 15, 92)
        grass_colour = pygame.Color(160, 200, 150)
        river_colour_r -= 0.5
        river_colour_g -= 0.25

    if daytime and sun_x >= 675: # This block checks to see if the Sun has reached the end of its daytime trajectory, and sets "daytime" to 'False' and changes the Sun's position
        daytime = False
        sun_x = -100
        sun_y = 200

    if not daytime and sun_x >= 675: # This is the opposite of the block above and switches the time frame back to "daytime"
        daytime = True
        sun_x = -100
        sun_y = 200

    # Resets the cloud & bird locations when it reaches the edge and further randomizes its value
    if cloud1_x >= 700:
        cloud1_x = randrange(-500, -101)
        cloud1_y = randrange(29, 113)
        cloud1_r = randrange(30, 37)
        cloud1_speed = randrange(2, 4)

    if cloud2_x >= 700:
        cloud2_x = randrange(-500, -101)
        cloud2_y = randrange(29, 113)
        cloud2_r = randrange(30, 37)
        cloud2_speed = randrange(2, 4)

    if cloud3_x >= 700:
        cloud3_x = randrange(-500, -101)
        cloud3_y = randrange(29, 113)
        cloud3_r = randrange(30, 37)
        cloud3_speed = randrange(2, 4)

    if birds_x >= 800:
        birds_x = randrange(-800, -301)

    # Evaluates to see if the trees touches the bottom of the screen, and if so, resets their positions
    if tree1_y >= HEIGHT + 10 or tree3_y >= HEIGHT + 10:
        tree1_x = 200
        tree1_y = 170
        tree3_x = 400
        tree3_y = 170
        trees13_r = 26
        trees13_w = 4
        trees13_h = 16

    if tree2_y >= HEIGHT + 10 or tree4_y >= HEIGHT + 10:
        tree2_x = 200
        tree2_y = 170
        tree4_x = 400
        tree4_y = 170
        trees24_r = 15
        trees24_w = 4
        trees24_h = 16

    # <--------------------------- GAME STATE UPDATES 🔄 --------------------------------->

    # 👇 All game math and comparisons happen here
    frames += 1

    sun_x += 4
    if sun_x <= 300: # Runs if the Sun is on its way to the peak
        sun_y -= 1
    else:
        sun_y += 1.5

    birds_x += 4.5

    cloud1_x += cloud1_speed
    cloud2_x += cloud2_speed
    cloud3_x += cloud3_speed

    # Change the trees locations and increases their sizes to create an illusion of them moving closer
    tree1_x -= 4
    tree1_y += 4
    tree2_x -= 4
    tree2_y += 4
    tree3_x += 5
    tree3_y += 4
    tree4_x += 5
    tree4_y += 4

    trees13_w += 0.64
    trees13_h += 2.56
    trees24_w += 0.64
    trees24_h += 2.56
    trees13_r += 0.92
    trees24_r += 0.92

    # <-------------------------------------- DRAWING 🎨 -------------------------------------------->

    # Background 🌆
    rectangle_height = 7  # The smaller this value, the more mixed the background gradient is

    for n in range(0, HEIGHT // 2, rectangle_height):  # This is a loop that draws each rectangle gradient in the sky
        bg_colour = sky_top_colour.lerp(sky_bottom_colour, n / HEIGHT * 2)  # Here, I did an interpolation between the two RGB values of the sky in order to mix them and create a nice-looking gradient
        screen.fill(bg_colour, (0, n, WIDTH, rectangle_height))

    # Stars - position 1 (only appear at nighttime)
    if not daytime and position1:
        pygame.draw.circle(screen, star_colour_1, (48, 47), stars_r)
        pygame.draw.circle(screen, star_colour_1, (48, 100), stars_r)
        pygame.draw.circle(screen, star_colour_1, (229, 99), stars_r)
        pygame.draw.circle(screen, star_colour_1, (165, 50), stars_r)
        pygame.draw.circle(screen, star_colour_1, (142, 158), stars_r)
        pygame.draw.circle(screen, star_colour_1, (357, 158), stars_r)
        pygame.draw.circle(screen, star_colour_1, (358, 59), stars_r)
        pygame.draw.circle(screen, star_colour_1, (519, 60), stars_r)
        pygame.draw.circle(screen, star_colour_1, (530, 138), stars_r)
        pygame.draw.circle(screen, star_colour_1, (453, 106), stars_r)
        pygame.draw.circle(screen, star_colour_1, (575, 58), stars_r)
        pygame.draw.circle(screen, star_colour_1, (580, 151), stars_r)
        pygame.draw.circle(screen, star_colour_1, (416, 25), stars_r)
        pygame.draw.circle(screen, star_colour_2, (303, 24), stars_r)
        pygame.draw.circle(screen, star_colour_2, (319, 172), stars_r)
        pygame.draw.circle(screen, star_colour_2, (604, 144), stars_r)
        pygame.draw.circle(screen, star_colour_2, (600, 56), stars_r)
        pygame.draw.circle(screen, star_colour_2, (101, 64), stars_r)
        pygame.draw.circle(screen, star_colour_2, (252, 54), stars_r)
        pygame.draw.circle(screen, star_colour_2, (309, 125), stars_r)
        pygame.draw.circle(screen, star_colour_2, (399, 65), stars_r)
        pygame.draw.circle(screen, star_colour_2, (299, 61), stars_r)
        pygame.draw.circle(screen, star_colour_2, (125, 86), stars_r)
        pygame.draw.circle(screen, star_colour_2, (337, 146), stars_r)
        pygame.draw.circle(screen, star_colour_2, (543, 147), stars_r)
        pygame.draw.circle(screen, star_colour_2, (22, 168), stars_r)

    # Stars - position 2
    if not daytime and not position1:
        pygame.draw.circle(screen, star_colour_1, (119, 147), stars_r)
        pygame.draw.circle(screen, star_colour_1, (115, 118), stars_r)
        pygame.draw.circle(screen, star_colour_1, (125, 30), stars_r)
        pygame.draw.circle(screen, star_colour_1, (66, 19), stars_r)
        pygame.draw.circle(screen, star_colour_1, (70, 148), stars_r)
        pygame.draw.circle(screen, star_colour_1, (236, 156), stars_r)
        pygame.draw.circle(screen, star_colour_1, (437, 123), stars_r)
        pygame.draw.circle(screen, star_colour_1, (472, 175), stars_r)
        pygame.draw.circle(screen, star_colour_1, (568, 112), stars_r)
        pygame.draw.circle(screen, star_colour_1, (417, 96), stars_r)
        pygame.draw.circle(screen, star_colour_1, (450, 28), stars_r)
        pygame.draw.circle(screen, star_colour_1, (509, 25), stars_r)
        pygame.draw.circle(screen, star_colour_1, (589, 26), stars_r)
        pygame.draw.circle(screen, star_colour_2, (600, 171), stars_r)
        pygame.draw.circle(screen, star_colour_2, (343, 54), stars_r)
        pygame.draw.circle(screen, star_colour_2, (235, 25), stars_r)
        pygame.draw.circle(screen, star_colour_2, (303, 96), stars_r)
        pygame.draw.circle(screen, star_colour_2, (418, 27), stars_r)
        pygame.draw.circle(screen, star_colour_2, (342, 166), stars_r)
        pygame.draw.circle(screen, star_colour_2, (252, 159), stars_r)
        pygame.draw.circle(screen, star_colour_2, (280, 95), stars_r)
        pygame.draw.circle(screen, star_colour_2, (217, 18), stars_r)
        pygame.draw.circle(screen, star_colour_2, (436, 157), stars_r)
        pygame.draw.circle(screen, star_colour_2, (105, 23), stars_r)
        pygame.draw.circle(screen, star_colour_2, (473, 14), stars_r)
        pygame.draw.circle(screen, star_colour_2, (582, 102), stars_r)


    # Clouds BEHIND the Sun 🌤️
    # Cloud 1
    pygame.draw.circle(screen, cloud_colours, (cloud1_x, cloud1_y), cloud1_r)
    pygame.draw.circle(screen, cloud_colours, (cloud1_x + 40, cloud1_y - 33), cloud1_r)
    pygame.draw.circle(screen, cloud_colours, (cloud1_x + 40, cloud1_y + 2), cloud1_r)
    pygame.draw.circle(screen, cloud_colours, (cloud1_x + 70, cloud1_y - 11), cloud1_r)

    # Cloud 2
    pygame.draw.circle(screen, cloud_colours, (cloud2_x, cloud2_y), cloud2_r)
    pygame.draw.circle(screen, cloud_colours, (cloud2_x + 40, cloud2_y - 33), cloud2_r)
    pygame.draw.circle(screen, cloud_colours, (cloud2_x + 40, cloud2_y + 2), cloud2_r)
    pygame.draw.circle(screen, cloud_colours, (cloud2_x + 70, cloud2_y - 11), cloud2_r)

    # Sun/Moon
    sun_radius = 80
    pygame.draw.circle(screen, sun_colour, (sun_x, sun_y), sun_radius)

    if not daytime:
        # These moondots are the rough surfaces on the moon
        moondot_colours = (192, 192, 192)
        moondot1_pts = [(sun_x - 25, sun_y - 64), (sun_x - 29, sun_y - 61), (sun_x - 35, sun_y - 55),
                        (sun_x - 41, sun_y - 50), (sun_x - 46, sun_y - 44), (sun_x - 51, sun_y - 38),
                        (sun_x - 58, sun_y - 28), (sun_x - 60, sun_y - 17), (sun_x - 55, sun_y - 14),
                        (sun_x - 49, sun_y - 17), (sun_x - 44, sun_y - 21), (sun_x - 39, sun_y - 25),
                        (sun_x - 33, sun_y - 32), (sun_x - 28, sun_y - 38), (sun_x - 21, sun_y - 43),
                        (sun_x - 13, sun_y - 49), (sun_x - 7, sun_y - 55), (sun_x - 6, sun_y - 60),
                        (sun_x - 9, sun_y - 64),
                        (sun_x - 17, sun_y - 66)]
        moondot2_r = 20
        moondot3_r = 35
        pygame.draw.polygon(screen, moondot_colours, moondot1_pts)
        pygame.draw.circle(screen, moondot_colours, (sun_x + 39, sun_y - 28), moondot2_r)
        pygame.draw.circle(screen, moondot_colours, (sun_x - 15, sun_y + 21), moondot3_r)

    # Clouds IN FRONT of the Sun 🌥️ (I made two layers of clouds to make the landscape look 3D)
    # Cloud 3
    pygame.draw.circle(screen, cloud_colours, (cloud3_x, cloud3_y), cloud3_r)
    pygame.draw.circle(screen, cloud_colours, (cloud3_x + 40, cloud3_y - 33), cloud3_r)
    pygame.draw.circle(screen, cloud_colours, (cloud3_x + 40, cloud3_y + 2), cloud3_r)
    pygame.draw.circle(screen, cloud_colours, (cloud3_x + 70, cloud3_y - 11), cloud3_r)

    # Birds - position 1
    if position1:
        bird1_pts = [(birds_x, 78), (birds_x + 11, 85), (birds_x - 1, 93), (birds_x + 4, 87)]
        bird2_pts = [(birds_x - 33, 54), (birds_x - 28, 60), (birds_x - 35, 69), (birds_x - 31, 62)]
        bird3_pts = [(birds_x - 64, 32), (birds_x - 58, 39), (birds_x - 66, 49), (birds_x - 62, 42)]
        bird4_pts = [(birds_x - 7, 114), (birds_x - 13, 106), (birds_x - 11, 114), (birds_x - 15, 124)]
        bird5_pts = [(birds_x - 43, 123), (birds_x - 35, 130), (birds_x - 40, 136), (birds_x - 38, 131)]
        bird6_pts = [(birds_x - 70, 135), (birds_x - 65, 143), (birds_x - 71, 150), (birds_x - 68, 144)]
        bird7_pts = [(birds_x + 23, 100), (birds_x + 32, 109), (birds_x + 22, 117), (birds_x + 28, 108)]
        pygame.draw.polygon(screen, "black", bird1_pts)
        pygame.draw.polygon(screen, "black", bird2_pts)
        pygame.draw.polygon(screen, "black", bird3_pts)
        pygame.draw.polygon(screen, "black", bird4_pts)
        pygame.draw.polygon(screen, "black", bird5_pts)
        pygame.draw.polygon(screen, "black", bird6_pts)
        pygame.draw.polygon(screen, "black", bird7_pts)

    # Birds - position 2
    else:
        bird1_pts = [(birds_x + 8, 85), (birds_x + 1, 79), (birds_x + 4, 85), (birds_x + 1, 92)]
        bird2_pts = [(birds_x - 28, 60), (birds_x - 34, 54), (birds_x - 31, 61), (birds_x - 33, 68)]
        bird3_pts = [(birds_x - 58, 39), (birds_x - 65, 32), (birds_x - 62, 39), (birds_x - 64, 48)]
        bird4_pts = [(birds_x - 7, 115), (birds_x - 5, 106), (birds_x - 11, 115), (birds_x - 15, 122)]
        bird5_pts = [(birds_x - 35, 130), (birds_x - 43, 123), (birds_x - 40, 131), (birds_x - 41, 138)]
        bird6_pts = [(birds_x - 64, 143), (birds_x - 72, 135), (birds_x - 69, 144), (birds_x - 69, 150)]
        bird7_pts = [(birds_x + 31, 109), (birds_x + 22, 99), (birds_x + 26, 109), (birds_x + 24, 118)]
        pygame.draw.polygon(screen, "black", bird1_pts)
        pygame.draw.polygon(screen, "black", bird2_pts)
        pygame.draw.polygon(screen, "black", bird3_pts)
        pygame.draw.polygon(screen, "black", bird4_pts)
        pygame.draw.polygon(screen, "black", bird5_pts)
        pygame.draw.polygon(screen, "black", bird6_pts)
        pygame.draw.polygon(screen, "black", bird7_pts)

    # Rectangle foreground
    foreground = pygame.Rect(0, HEIGHT / 2, WIDTH, HEIGHT / 2)
    screen.fill(grass_colour, foreground)

    # River - position 1
    if position1:
        river1_pts = [(275, HEIGHT / 2), (266, 189), (256, 198), (245, 209), (238, 220), (235, 233), (243, 249), (236, 230),
                    (239, 241), (243, 247), (248, 254), (253, 264), (252, 272), (249, 280), (241, 290), (234, 298),
                    (224, 310), (215, 318), (207, 325), (197, 334), (185, 345), (174, 354), (168, 359), (395, 359),
                    (403, 351), (408, 344), (412, 337), (413, 329), (413, 319), (410, 310), (406, 302), (402, 295),
                    (397, 286), (393, 281), (391, 278), (397, 287), (394, 282), (391, 280), (389, 272), (389, 267),
                    (390, 258), (392, 250), (396, 241), (396, 229), (393, 224), (389, 216), (384, 208), (380, 204),
                    (376, 197), (372, 191), (370, 186), (368, 182), (367, HEIGHT / 2)]
        pygame.draw.polygon(screen, (river_colour_r, river_colour_g, river_colour_b), river1_pts)

    # River - position 2
    else:
        river2_pts = [(270, HEIGHT / 2), (267, 184), (263, 189), (259, 196), (255, 200), (253, 204), (247, 208), (244, 212),
                    (241, 218), (240, 222), (239, 229), (241, 237), (244, 243), (247, 249), (249, 255), (249, 264),
                    (246, 273), (244, 278), (240, 285), (235, 293), (229, 297), (226, 301), (220, 307), (215, 314),
                    (207, 320), (201, 326), (194, 332), (185, 341), (177, 346), (168, 354), (163, 365), (400, 365),
                    (404, 353), (407, 348), (409, 342), (410, 335), (410, 330), (410, 324), (409, 315), (406, 309),
                    (404, 304), (400, 297), (397, 290), (394, 285), (393, 282), (393, 276), (393, 270), (394, 265),
                    (395, 260), (396, 255), (397, 251), (397, 247), (396, 240), (395, 235), (393, 228), (389, 221),
                    (385, 215), (384, 209), (378, 200), (373, 194), (370, 186), (368, HEIGHT / 2)]
        pygame.draw.polygon(screen, (river_colour_r, river_colour_g, river_colour_b), river2_pts)

    # Trees - compound shapes
    trees12_rect_colours = (152, 123, 72)
    trees12_colours = (64, 198, 68)
    trees12_shades = (36, 172, 41)

    # Trees - position 1
    if position1:
        # Tree 1
        pygame.draw.circle(screen, trees12_shades, (tree1_x + 10, tree1_y + 5), trees13_r)
        pygame.draw.rect(screen, trees12_rect_colours, (tree1_x, tree1_y, trees13_w, trees13_h))
        pygame.draw.circle(screen, trees12_colours, (tree1_x - 17, tree1_y - 12), trees13_r)
        pygame.draw.circle(screen, trees12_colours, (tree1_x + 8, tree1_y - 45), trees13_r)
        pygame.draw.circle(screen, trees12_colours, (tree1_x + 35, tree1_y - 10), trees13_r)

        # Tree 2
        pygame.draw.circle(screen, trees12_shades, (tree2_x + 2, tree2_y), trees24_r)
        pygame.draw.rect(screen, trees12_rect_colours, (tree2_x, tree2_y, trees24_w, trees24_h))
        pygame.draw.circle(screen, trees12_colours, (tree2_x - 5, tree2_y - 3), trees24_r)
        pygame.draw.circle(screen, trees12_colours, (tree2_x + 1, tree2_y - 9), trees24_r)
        pygame.draw.circle(screen, trees12_colours, (tree2_x + 8, tree2_y - 3), trees24_r)

        # Tree 3
        pygame.draw.circle(screen, trees34_shades, (tree3_x + 9, tree3_y + 5), trees13_r)
        pygame.draw.rect(screen, trees34_rect_colours, (tree3_x, tree3_y, trees13_w, trees13_h))
        pygame.draw.circle(screen, trees34_colours, (tree3_x - 20, tree3_y - 8), trees13_r)
        pygame.draw.circle(screen, trees34_colours, (tree3_x + 5, tree3_y - 34), trees13_r)
        pygame.draw.circle(screen, trees34_colours, (tree3_x + 34, tree3_y - 6), trees13_r)

        # Tree 4
        pygame.draw.circle(screen, trees34_shades, (tree4_x + 1, tree4_y + 2), trees24_r)
        pygame.draw.rect(screen, trees34_rect_colours, (tree4_x, tree4_y, trees24_w, trees24_h))
        pygame.draw.circle(screen, trees34_colours, (tree4_x - 5, tree4_y - 1), trees24_r)
        pygame.draw.circle(screen, trees34_colours, (tree4_x, tree4_y - 8), trees24_r)
        pygame.draw.circle(screen, trees34_colours, (tree4_x + 6, tree4_y - 1), trees24_r)

    # Trees - position 2
    else:
        # Tree 1
        pygame.draw.circle(screen, trees12_shades, (tree1_x + 9, tree1_y + 6), trees13_r)
        pygame.draw.rect(screen, trees12_rect_colours, (tree1_x, tree1_y, trees13_w, trees13_h))
        pygame.draw.circle(screen, trees12_colours, (tree1_x - 18, tree1_y - 13), trees13_r)
        pygame.draw.circle(screen, trees12_colours, (tree1_x + 7, tree1_y - 44), trees13_r)
        pygame.draw.circle(screen, trees12_colours, (tree1_x + 36, tree1_y - 11), trees13_r)

        # Tree 2
        pygame.draw.circle(screen, trees12_shades, (tree2_x + 1, tree2_y), trees24_r)
        pygame.draw.rect(screen, trees12_rect_colours, (tree2_x, tree2_y, trees24_w, trees24_h))
        pygame.draw.circle(screen, trees12_colours, (tree2_x - 4, tree2_y - 3), trees24_r)
        pygame.draw.circle(screen, trees12_colours, (tree2_x + 2, tree2_y - 10), trees24_r)
        pygame.draw.circle(screen, trees12_colours, (tree2_x + 9, tree2_y - 3), trees24_r)

        # Tree 3
        pygame.draw.circle(screen, trees34_shades, (tree3_x + 10, tree3_y + 6), trees13_r)
        pygame.draw.rect(screen, trees34_rect_colours, (tree3_x, tree3_y, trees13_w, trees13_h))
        pygame.draw.circle(screen, trees34_colours, (tree3_x - 19, tree3_y - 9), trees13_r)
        pygame.draw.circle(screen, trees34_colours, (tree3_x + 6, tree3_y - 33), trees13_r)
        pygame.draw.circle(screen, trees34_colours, (tree3_x + 34, tree3_y - 7), trees13_r)

        # Tree 4
        pygame.draw.circle(screen, trees34_shades, (tree4_x + 2, tree4_y + 2), trees24_r)
        pygame.draw.rect(screen, trees34_rect_colours, (tree4_x, tree4_y, trees24_w, trees24_h))
        pygame.draw.circle(screen, trees34_colours, (tree4_x - 6, tree4_y - 1), trees24_r)
        pygame.draw.circle(screen, trees34_colours, (tree4_x + 1, tree4_y - 9), trees24_r)
        pygame.draw.circle(screen, trees34_colours, (tree4_x + 5, tree4_y - 1), trees24_r)

    # Flips the timer
    pygame.display.flip()
    clock.tick(30)

    # <----------------------------------------------------------------------------------------------------------->

pygame.quit()
