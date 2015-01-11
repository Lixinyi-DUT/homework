# implementation of card game - Memory

import simplegui
import random
# helper function to initialize globals
def new_game():
    global l,exposed,state,counter,label,counter
    counter=0
    label.set_text("Turns = "+str(counter))
    state=0
    exposed=[]
    l=range(0,8)
    l.extend(range(0,8))
    random.shuffle(l)
    for num in l:
      exposed.append(False)

# define event handlers
def mouseclick(pos):
    global l,exposed,state,pre,cur,counter,label
    index=pos[0]//50
    if exposed[index]==False:
                exposed[index]=True
                if state == 0:
                  pre=index
                  state = 1
                elif state == 1:
                  cur=index
                  state = 2
                  counter+=1
                  label.set_text("Turns = "+str(counter))
                else:
                 if l[cur]!=l[pre]:
                        exposed[cur]=False
                        exposed[pre]=False
                 pre=index           
                 state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global l,exposed,counter
    for i in range(0,16):
        if exposed[i]==True:
          canvas.draw_text(str(l[i]),(16+50*i,50),35,'white')
        else:
          canvas.draw_polygon([(i*50, 0), (i*50+49, 0), (i*50+49, 100),(i*50,100)], 1, 'Black','Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
