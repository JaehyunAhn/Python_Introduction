# implementation of card game - Memory
import simplegui
import random

# global variable
numbers = range(8)
numbers += numbers
deck_status = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0 }
interval = 8
count = 0
temp1 = 16
temp2 = 16

# helper function to initialize globals
def init():
    global numbers, deck_status, count, temp1, temp2
    random.shuffle(numbers)
    for i in range(16):
        deck_status[i] = 0
    count = 0
    temp1 = 16
    temp2 = 16
    pass

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global count, deck_status, temp1, temp2, numbers
    index = int(pos[0]/50)
    if(temp1 == 16 and deck_status[index] == 0):
        temp1 = index
        deck_status[temp1] = 1
        count += 1
    if(temp2 == 16 and index != temp1 and deck_status[index] == 0):
        temp2 = index
        deck_status[temp2] = 1
    elif(index != temp1 and index != temp2 and deck_status[index] == 0):
        if( numbers[temp1] != numbers[temp2] ):
            deck_status[temp1] = 0
            deck_status[temp2] = 0
        deck_status[index] = 1
        temp1 = index
        temp2 = 16
        count += 1
    pass
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        global interval, count
        canvas.draw_text(str(numbers[i]), (interval, 65), 50, "White")
        if(deck_status[i] == 0):
            canvas.draw_polygon([[interval-8, 0], [interval+42, 0], [interval+42, 100], [interval-8,100]], 5, "White", "Blue")
        interval += 50
        interval %= 800
    label.set_text("Moved = "+str(count))
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