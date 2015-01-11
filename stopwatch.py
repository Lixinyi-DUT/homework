# template for "Stopwatch: The Game"
import simplegui
# define global variables
time_num = 0
attempts=0
success=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    millisecond = t % 10
    seconds = t // 10
    s_digit = seconds % 60
    m_digit = seconds //60
    if s_digit<10:
       return str(m_digit)+':0'+str(s_digit)+'.'+str(millisecond)
    else:
       return str(m_digit)+':'+str(s_digit)+'.'+str(millisecond)   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler() :
    timer.start()

def stop_button_handler() :
    global attempts
    global success
    timer.stop()
    if time_num > 0 :
       attempts += 1
       if time_num % 10 == 0:
         success += 1

def reset_button_handler() :
    timer.stop()
    global time_num, attempts, success
    time_num = 0
    attempts=0
    success=0


# define event handler for timer with 0.1 sec interval
def timer_handler() :
    global time_num
    time_num += 1

# define draw handler
def draw_handler(canvas) :
    global time_num
    global success
    global attempts
    canvas.draw_text(format(time_num), [40 ,100], 50,'white')
    canvas.draw_text(str(success) + '/' + str(attempts), [180 ,30], 20,'white')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 240, 170)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_button_handler, 100)
frame.add_button("Stop", stop_button_handler, 100)
frame.add_button("Reset", reset_button_handler, 100)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
# Please remember to review the grading rubric
