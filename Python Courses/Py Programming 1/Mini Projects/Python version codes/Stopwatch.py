#Stopwatch Program
#Enjoy the game :)
#Yours, D'Cypher
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math

#=====Global timer
count_sec = 0
count_min = 0
count_hr = 0
score_count = 0
stop_count = 0
score_click = 0
stop_click = 0
tracker = str(0) + " / " + str(0) 


def increment():
    global count_sec
    global count_min
    global count_hr
    count_sec += 0.1
    count_min = math.floor(count_sec / 60)
    count_hr = math.floor(count_min / 60)

#=====Number to string converter
def convert_str(count_sec):
    conv_milsec = str((count_sec))[-1]
    conv_sec = str(int(math.floor(count_sec)%60))
    conv_min = str(int((math.floor(count_sec / 60)%60)))    
    
    single_sec = (len(conv_sec) == 1)
    single_min = (len(conv_min) == 1)
    
    if (single_min and single_sec):
        return ("0" + conv_min + ":" + 
                "0" + conv_sec + "." + conv_milsec)
    elif (single_min == True and single_sec == False):
        return ("0" + conv_min + ":" + 
                conv_sec + "." + conv_milsec)
    elif (single_min == False and single_sec == True):
        return (conv_min + ":" + 
                "0" + conv_sec + "." + conv_milsec)
    else:
        return (conv_min + ":" + conv_sec + "." + conv_milsec)

def time_display(count_hr):
    if count_hr >= 1:
        return str(int(count_hr)) + ":" + str(convert_str(count_sec))
    else:
        return str(convert_str(count_sec))

#=====Score Keeping
def score_add():
    global score_count
    global score_click
    mil_zero = (int(str(count_sec)[-1]) == 0)
    
    if ((mil_zero == True) and (score_click == 1)): 
        score_count += 1
        score_click = 0
        return (score_count)
    else:
        score_click = 0
        return (score_count)

def stop_add():
    global stop_count
    global stop_click
    if (stop_click == 1):
        stop_count += 1
        stop_click = 0
        return (stop_count)
    else:
        stop_click = 0
        return (stop_count)

#=====Timer Controls Handlers
def tick():
    increment()

def button_start():
    timer.start()
    global score_click
    global stop_click
    score_click = 1
    stop_click = 1
    
def button_stop():
    timer.stop()
    global tracker
    tracker = (str(score_add()) + " / " + str(str(stop_add())))
    
def button_reset():
    timer.stop()
    global count_sec
    global count_min
    global count_hr
    global score_count
    global stop_count
    global score_click
    global stop_click
    global tracker
    count_sec = 0
    count_min = 0
    count_hr = 0
    score_count = 0
    stop_count = 0
    score_click = 0
    stop_click = 0
    tracker = str(0) + " / " + str(0) 

#=====Draw handler
def draw(canvas):
    canvas.draw_text(str(time_display(count_hr))
                     , [95, 120], 40, "White")
    canvas.draw_text(tracker, [230, 40], 30, "Green")
    
#=====Create a frame and register handler
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_label("Enjoy the game! :)")
frame.add_label(" ")
frame.add_button("Start", button_start, 200)
frame.add_button("Stop", button_stop, 200)
frame.add_label(" ")
frame.add_button("Reset", button_reset, 200)

#Start frame and timer
frame.start()
timer.start()

