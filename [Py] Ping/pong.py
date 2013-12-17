# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [300,200]
ball_vel = [0,0]
paddle1_pos = 160
paddle2_pos = 160
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
NEW_GAME = True

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300,200]
    ball_vel[1] = random.randrange(1, 3)
    ball_vel[0] = random.randrange(2, 4)
    if(right == True):
        ball_vel[1] *= -1
    else:
        ball_vel[0] *= -1
        ball_vel[1] *= -1

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  # these are floats
    global score1, score2, NEW_GAME  # these are ints
    paddle1_pos = 160
    paddle2_pos = 160
    score1 = 0
    score2 = 0
    ball_pos = [300,200]
    NEW_GAME = True

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel, NEW_GAME
    
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_vel == 'up'):
        if(paddle1_pos-8) >= 0:
            paddle1_pos -= 8
    if(paddle1_vel == 'down'):
        if(paddle1_pos+80+8) <= HEIGHT:
            paddle1_pos += 8  
    if(paddle2_vel == 'up'):
        if(paddle2_pos-8) >= 0:
            paddle2_pos -= 8
    if(paddle2_vel == 'down'):
        if(paddle2_pos+80+8) <= HEIGHT:
            paddle2_pos += 8
            
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(0,0+paddle1_pos),(0,80+paddle1_pos),(8,80+paddle1_pos),(8,0+paddle1_pos)], 1, "White", "White")
    c.draw_polygon([(592,0+paddle2_pos),(592,80+paddle2_pos),(600,80+paddle2_pos),(600,0+paddle2_pos)], 1, "White", "White")
            
    # update ball
    if(NEW_GAME == False):
        if(ball_pos[0]+20 > 600-8) and (ball_pos[1] > paddle2_pos) and (ball_pos[1] < paddle2_pos+80):
            ball_vel[0] *= -1.1
        elif (ball_pos[0]+20 > 600-8):
            score1 += 1
            ball_init(False)
        if(ball_pos[0]-20 < 8) and (ball_pos[1] > paddle1_pos) and (ball_pos[1] < paddle1_pos+80):
            ball_vel[0] *= -1.1
        elif (ball_pos[0]-20 < 8):
            score2 += 1
            ball_init(True)
        if(ball_pos[1]+20 > 400):
            ball_vel[1] *= -1
        if(ball_pos[1]-20 < 0):
            ball_vel[1] *= -1
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), [130,80], 40, "White")
    c.draw_text(str(score2), [430,80], 40, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, NEW_GAME
    if (NEW_GAME == True):
        NEW_GAME = False
        ball_init(True)
    # 40: down arrow 38: up arrow
    if key == 40:
        paddle2_vel = 'down'
    if key == 38:
        paddle2_vel = 'up'
    # 87: w key 83: s key
    if key == 83:
        paddle1_vel = 'down'
    if key == 87:
        paddle1_vel = 'up'
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == 83) or (key == 87):
        paddle1_vel = 'nothing'
    if(key == 38) or (key == 40):
        paddle2_vel = 'nothing'

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
frame.start()