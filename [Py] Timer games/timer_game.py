# template for "Stopwatch: The Game"
import simplegui


# define global variables
time = 0
mil_second = 0
second = 0
minute = 0
success_s = 0
total_s = 0

stop_flag = False

def setup_time(time):
    # define helper function format that converts time
    # in tenths of seconds into formatted string A:BC.D
    global mil_second
    global second
    global minute
    mil_second = time%10
    second = ((time - mil_second)/10)%60
    minute = int(time/600)

def timer_handler():
    # define event handler for timer with 0.1 sec interval
    global time
    time += 1
    setup_time(time)    
timer = simplegui.create_timer(100,timer_handler)

# define draw handler
def start_handler():
    global stop_flag
    stop_flag = False
    return timer.start()

def stop_handler():
    global success_s
    global total_s
    global time
    global stop_flag
    if (time != 0) and (stop_flag == False):
        if time%10 == 0:
            success_s += 1
        total_s += 1
        stop_flag = True
    return timer.stop()

def reset_handler():
    global time
    global success_s
    global total_s
    time = 0
    success_s = 0
    total_s = 0
    setup_time(time)
    return timer.stop()

# create frame
frame = simplegui.create_frame("Stopwatch: The Game",170,170)

# define event handlers for buttons; "Start", "Stop", "Reset"
start_button = frame.add_button("start", start_handler, 100)
stop_button = frame.add_button("stop", stop_handler, 100)
reset_button = frame.add_button("reset", reset_handler, 100)

# register event handlers
def draw(canvas):
    #draw timer
    canvas.draw_text("."+str(mil_second), (100, 100), 30, "white")
    if int(second/10) == 0:
        canvas.draw_text("0"+str(second), (67, 100), 30, "white")
    else:
        canvas.draw_text(str(second), (67, 100), 30, "white")
    if time >= 6000:
        canvas.draw_text(str(minute)+":", (20, 100), 30, "white")
    else:
        canvas.draw_text(str(minute)+":", (40, 100), 30, "white")
    #draw game score
    canvas.draw_text(str(success_s)+"/"+str(total_s), (100, 30), 20, "green")


# start frame
frame.set_draw_handler(draw)
frame.start()

# Please remember to review the grading rubric
