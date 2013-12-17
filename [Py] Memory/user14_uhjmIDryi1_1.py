# implementation of card game - Memory
import simplegui
import random

# global variable
numbers = range(8)
numbers += numbers
deck_status = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0 }
interval = 8
click_count = 0
count = 0
temp1 = 10
temp2 = 10

# helper function to initialize globals
def init():
    global numbers, deck_status, count, click_count, temp1, temp2
    random.shuffle(numbers)
    for i in range(16):
        deck_status[i] = 0
    count = 0
    click_count = 0
    temp1 = 10
    temp2 = 10  
    pass

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global count, click_count, deck_status, temp1, temp2
    index = int(pos[0]/50)
    deck_status[index] = 1
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        global interval
        canvas.draw_text(str(numbers[i]), (interval, 65), 50, "White")
        if(deck_status[i] == 0):
            canvas.draw_polygon([[interval-8, 0], [interval+42, 0], [interval+42, 100], [interval-8,100]], 5, "White", "Blue")
        interval += 50
        interval %= 800
    pass

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)

# initialize global variables
init()

# register event handlers
label = frame.add_label("Moves = 0")
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# get things rolling
frame.start()

# Always remember to review the grading rubric