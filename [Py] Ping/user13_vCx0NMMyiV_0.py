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
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    # update paddle's vertical position, keep paddle on the screen
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(0,0+paddle1_pos),(0,80+paddle1_pos),(8,80+paddle1_pos),(8,0+paddle1_pos)], 1, "White", "White")
    c.draw_polygon([(592,0+paddle2_pos),(592,80+paddle2_pos),(600,80+paddle2_pos),(600,0+paddle2_pos)], 1, "White", "White")
    
    # update ball
    if(paddle1_vel == 'up'):
        paddle1_pos -= 4
    if(paddle1_vel == 'down'):
        paddle1_pos += 4
        
    if(paddle2_vel == 'up'):
        paddle2_pos -= 4
    if(paddle2_vel == 'down'):
        paddle2_pos += 4

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
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
    paddle1_vel = 'nothing'
    paddle2_vel = 'nothing'


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
