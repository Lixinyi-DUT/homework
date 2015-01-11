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
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    positive_vel_x = random.randrange(120, 240) / 60.0
    vel_y = random.randrange(60, 180) / 60.0
    if direction == LEFT:
        ball_vel=[-positive_vel_x, -vel_y]
    else:
        ball_vel=[positive_vel_x, -vel_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randrange(0,2)==0)
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1=0
    score2=0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1]- BALL_RADIUS <= 0 or ball_pos[1]+BALL_RADIUS >= HEIGHT-1:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0]- BALL_RADIUS <= PAD_WIDTH:
       if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and  ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
         ball_vel[0] = - ball_vel[0]
         ball_vel[0]*=1.1
         ball_vel[1]*=1.1
       else:
         spawn_ball(RIGHT)
         score2 += 1
    if ball_pos[0]+BALL_RADIUS >= WIDTH-PAD_WIDTH-1:
       if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and  ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
         ball_vel[0] = - ball_vel[0]
         ball_vel[0]*=1.1
         ball_vel[1]*=1.1
       else:
         spawn_ball(LEFT)
         score1 += 1
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos - HALF_PAD_HEIGHT >=0 or paddle1_vel>0) and (paddle1_pos + HALF_PAD_HEIGHT <= HEIGHT -1 or paddle1_vel<0):
        paddle1_pos += paddle1_vel
    if (paddle2_pos - HALF_PAD_HEIGHT >=0 or paddle2_vel>0) and (paddle2_pos + HALF_PAD_HEIGHT <= HEIGHT -1 or paddle2_vel<0):
        paddle2_pos += paddle2_vel  
    # draw paddles
    canvas.draw_line((PAD_WIDTH/2,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH/2,paddle1_pos+HALF_PAD_HEIGHT), PAD_WIDTH, 'white')
    canvas.draw_line((WIDTH-PAD_WIDTH/2,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH/2,paddle2_pos+HALF_PAD_HEIGHT), PAD_WIDTH, 'white')
    # draw scores
    canvas.draw_text(str(score1), (0.25*WIDTH, 50), 35, 'white')
    canvas.draw_text(str(score2), (0.75*WIDTH, 50), 35, 'white')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
      paddle1_vel =-4
    if key == simplegui.KEY_MAP['s']:
      paddle1_vel= 4
    if key == simplegui.KEY_MAP['up']:
      paddle2_vel =-4
    if key == simplegui.KEY_MAP['down']:
      paddle2_vel= 4

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
      paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
      paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
      paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
      paddle2_vel= 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game)


# start frame
new_game()
frame.start()
