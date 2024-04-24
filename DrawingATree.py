import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tree")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
# Colors
white = (255, 255, 255)
brown = (82, 29, 0)
dark_green = (15, 82, 0)

# ---------------------------

# ---------------------------
# Functions

def draw_tree(x:int, y: int):
    '''
	This function draws a tree.

	Args:
		x (int): x-position for the tip of the tree
		y (int): y-position for the tip of the tree
	'''
    # Trunk
    pygame.draw.rect(screen, brown, [x-25, y+180, 50, 100])

    # Pines (top to bottom) x was 350 y was 120
    pygame.draw.polygon(screen, dark_green, [[x, y], [x-50, y+80], [x+50, y+80]])
    pygame.draw.polygon(screen, dark_green, [[x, y+30], [x-70, y+140], [x+70, y+140]])
    pygame.draw.polygon(screen, dark_green, [[x, y+70], [x-90, y+200], [x+90, y+200]])

# ---------------------------


# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here

    # ----- DRAWING -----
    screen.fill(white)  # always the first drawing command

    # draw a tree
    draw_tree(150, 60)

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
