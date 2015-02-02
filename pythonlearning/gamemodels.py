

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id, 245, 100)
        #print ("hello world")

    def draw(self):
        self.canvas.move(self.id, 0, -1)
