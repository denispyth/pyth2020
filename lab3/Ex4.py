from tkinter import *
from random import randrange as rnd, choice
import time


class Ball:
	def __init__(self):
		colors = ['red', 'orange', 'yellow', 'green', 'blue']
		self.x = rnd(100, 700)
		self.y = rnd(100, 500)
		self.r = rnd(30, 50)
		self.dx, self.dy = (+ 2, + 3)
		self.ball_id = canv.create_oval(self.x - self.r, self.y - self.r, 
									self.x + self.r, self.y + self.r, fill = choice(colors), width=0)
		
	def ball_move(self):
		self.x += self.dx
		self.y += self.dy
		if self.x + self.r > width or self.x - self.r <= 0:
			self.dx = -self.dx
			
		if self.y + self.r > hight or self.y - self.r <= 0:
			self.dy = -self.dy
		
	def ball_show(self):
		canv.move(self.ball_id, self.dx, self.dy)
		
	def ball_dell(self):
		canv.create_text(self.x, self.y, font="Purisa",
            text="BOOM!!!")
		canv.delete(self.ball_id)
	

def tick():
	for ball in balls:
		ball.ball_move()
		ball.ball_show()
	l_score['text'] = "Очки: " + str(score)
	root.after(50,tick)
		
	
def click(event):
	global score
	
	for ball in balls:
		if ball.x-ball.r <= event.x <= ball.x + ball.r and ball.y-ball.r <= event.y <= ball.y + ball.r:
			ball.ball_dell()
			score += 1
			

def generate_balls(event):
	global balls
	
	balls = [Ball() for i in range(rnd(1,10))]
	tick()
	
	
def main():
	global canv, width, hight, root, score, l_score
	
	score = 0 
	width = 800
	hight = 600
	root = Tk()
	root.geometry(str(width)+'x'+str(hight))
	canv = Canvas(root,bg='white')
	canv.pack(fill=BOTH,expand=1)
	l_score = Label(root, bg='black', fg='white', width=50, text="Push right-button! And touch balls left-button!")
	l_score.pack()
	canv.bind('<Button-1>', click)
	canv.bind('<Button-3>', generate_balls)
	
	mainloop()



if __name__ == "__main__":
	main()