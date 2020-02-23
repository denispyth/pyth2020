from graph import *

	
	
def draw_background(height):
	""" делим экран на 2 части
	"""
	pass

	
def draw_house(х,y,height,width):
	""" Рисуем дом	"""
	pass

def draw_tree(х,y,height,radius):
	""" Рисуем дерево	"""
	pass

def draw_cloud(х,y,height,radius):
	""" Рисуем облако	"""
	pass	
	
def draw_sun(х,y,radius):
	""" Рисуем солнце	"""
	pass	
	

	
	
win_height = 400									#размер окна
win_width = 600

windowSize(win_width,win_height)

y = win_height/2									#фон

draw_background(y)


х = win_width/6								#нижняя левая точка дома
y = win_height*2/3
height = win_width/4							#высота и ширина дома
width = 1.5*win_width/4
	
draw_house(х,y,height,width)

х = 2/3*win_width								#нижняя левая точка дерева
y = 5/8*win_height
height = win_width/4							#высота дерева
radius = 20										#диаметр веток

draw_tree(х,y,height,radius)	

	
х = 2/3*win_width								#нижняя левая точка облака
y = 5/8*win_height
radius = 20										#диаметр части облака

draw_cloud(х,y,height,radius)	
	
х = 2/3*win_width								#нижняя левая точка солнца
y = 5/8*win_height
radius = 30										#диаметр солнца

draw_sun(х,y,radius)	
	
	
run()