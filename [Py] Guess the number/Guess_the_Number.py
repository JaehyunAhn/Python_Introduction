# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
num_range	= 100
count		= 10

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, count
    num_range = random.randrange(0,100)
    count = 7
    print "New game. Range is from 0 to 100."
    print "Number of remaining guesses is",count
    print ""

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, count
    num_range = random.randrange(0,1000)
    count = 10
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is",count
    print ""
    
def get_input(guess):
    # main game logic goes here	
    global num_range, count
    print ""
    if count <= 0:
        print "Game Over!"
        return -1
    print "Guess was",guess
    count -= 1
    print "Number of remaining guesses is",count
    if num_range > int(guess) :
        print "Higher!"
        return 0
    elif num_range < int(guess) :
        print "Lower!"
        return 0
    elif num_range == int(guess) :
        print "Correct!"
        return 1

    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 400)

# register event handlers for control elements
button1 = frame.add_button("Range is [0, 100)", range100, 200)
button2 = frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()
range100()

# always remember to check your completed program against the grading rubric
