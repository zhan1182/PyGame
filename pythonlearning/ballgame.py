from tkinter import *
import time
import random
#from goto import label, goto
#from gamemodels import Ball

## Game Models
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height() ## height of window of the canvas
        self.canvas_width = self.canvas.winfo_width() ## width of window of the canvas

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) ## coordinates of the paddle
        if self.x > 0:
            if pos[2] >= (paddle_pos[0] - 5) and pos[2] <= (paddle_pos[2] + 5):
                if self.y > 0:
                    if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                        return True
                else:
                    if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                        return True
        else:
            if pos[0] >= (paddle_pos[0] - 5) and pos[0] <= (paddle_pos[2] + 5):
                if self.y > 0:
                    if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                        return True
                else:
                    if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                        return True
        return False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) ## get coordinates of the ball. Return a list,
            ## as [x1, y1, x2, y2], x1,y1 means left upper, x2, y2 means right lower
        if pos[1] <= 0:   ## get the y1, if y1 hit the top of the window
            self.y = 3
        if pos[3] >= self.canvas_height:  ## get the y2, if y2 hit the bottom of the window
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -self.y
        if pos[0] <= 0:  ## get the x1, if x1 hit the left side
            self.x = 3
        if pos[2] >= self.canvas_width: ## get the x2, if x2 hit the right side
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.stop = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        ## Bind the event "KeyPress-Left" to the function "turn_left"
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        ## Bind the event "KeyPress-Right" to the function "turn_right"
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        #self.x = 0
        #self.y = 0
        self.pos = self.canvas.coords(self.id)
        if self.pos[0] <= 0:
            self.x = 0
            self.stop = 1  ## hit left side
        if self.pos[2] >= self.canvas_width:
            self.x = 0
            self.stop = 2  ## hit right side
        if self.pos[1] <= 0:
            self.y = 0
            self.stop = 3  ## hit the top
        if self.pos[3] >= self.canvas_height:
            self.y = 0
            self.stop = 4  ## hit the bottom
            
    def turn_left(self, evt):
        if self.stop != 1:
            if self.stop == 3 or self.stop == 4:
                if self.pos[0] > 0:
                    self.x = -2
                    self.y = 0
                    self.stop = 0
            else:                
                self.x = -2
                self.y = 0
                self.stop = 0
    def turn_right(self, evt):
        if self.stop != 2:
            if self.stop == 3 or self.stop == 4:
                if self.pos[2] < self.canvas_width:
                    self.x = 2
                    self.y = 0
                    self.stop = 0
            else:
                self.x = 2
                self.y = 0
                self.stop = 0
    def turn_up(self, evt):
        if self.stop != 3:
            self.y = -2
            self.x = 0
            self.stop = 0
    def turn_down(self, evt):
        if self.stop != 4:
            self.y = 2
            self.x = 0
            self.stop = 0

class Text:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_text(0,0, text = "Game Over", fill = color)
        self.canvas.move(self.id, 245, 100)


## Initialization
tk = Tk()
tk.title("Game")   ## add a title to the window
tk.resizable(0,0)  ## make the size of window unchangable
tk.wm_attributes("-topmost", 1)  ## make the window as topmost
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

time1 = time.time()

## Main loop
#label .start
while 1:
    #print ("in")
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    time2 = time.time()
    if time2 - time1 >= 10:
        break

text = Text(canvas, 'red')
time.sleep(2)
#goto .start





