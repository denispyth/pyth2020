from graph import *
import turtle



def draw_circles(x, y, radius, n, kuchnost, horizont):	# Рисуем кроны или облака
	if horizont == False:				# Рисуем крону дерева (снизу вверх)
		y_os = - 3 / 4 * radius
		for i in range(n):
			circle(x - kuchnost, y + 9/10*y_os , radius)
			circle(x + 9/10*kuchnost, y + y_os, radius)
			circle(x, y - 3 / 4 * radius + y_os, radius)
			y_os -= 5 / 3 * radius
	else:
		x_os = 0
		circle(x + x_os, y + kuchnost, radius) # Рисуем облако
		for i in range(n):
			x_os +=  radius
			circle(x + x_os, y - kuchnost, radius)
			circle(x + x_os, y + kuchnost, radius)
			
		circle(x + radius + x_os, y + kuchnost , radius)
		

def change_color(c_line,c_bg, width):	# Меняем цвет пера, цвет заливки и толщину пера
	penColor(c_line) 					# Цвет пера
	brushColor(c_bg)					# Цвет заливки
	penSize(width)  					# Толщина пера
	
def draw_background(width, height):
	""" делим экран на 2 части	"""
	
	change_color("#D4E8FC","#D4E8FC", 1)	
	polygon ([	(0,0), (width,0),
				(width,height/2), (0,height/2)])
	change_color("#0E9325","#0E9325", 1)	
	polygon ([	(0,height/2), (width,height/2),
				(width,height), (0,height)])

	
def draw_house(x, y, height, width):
	""" Рисуем дом	"""
	
	change_color("Black","#FC730B", 1)	 	#Стены
	polygon ([	(x, y - height / 2), (x + width, y - height / 2),
				(x + width, y), (x, y)])
				
	
	change_color("#FC7F36","#2B7FFC", 1)	#Окно
	polygon ([	(x + width / 3, y - 2 / 5 * height), (x + 2 / 3 * width, y - 2 / 5 * height),
				(x + 2 / 3 * width, y - 1 / 5 * height), (x + width / 3, y - 1 / 5 * height)])
	
	
	change_color("Black","#EB2F44", 1)	 	#Крыша
	polygon ([	(x, y - height / 2), (x + width,y - height / 2),
				(x + width / 2, y - height), (x, y - height / 2)])

def draw_tree(x, y, height, radius):
	""" Рисуем дерево	"""
	
	change_color("Black","#402407", 2)	 	#Ствол
	polygon ([	(x, y - height / 2), (x + height/10, y - height / 2),
				(x + height/10, y), (x, y)])
				
	change_color("Black","#0F530E", 2)	 	#Крона
	y -= height/2
	x += height/20							#Центр ствола
	n = 2									#Количество веток
	kuchnost = 9/10*radius						#Кучность (отклонение от оси)
	horizont = False						#Вертикально или горизонтально 
	draw_circles(x, y, radius, n, kuchnost, horizont)
	

def draw_cloud(x, y, radius):
	""" Рисуем облако	"""
	change_color("Black","White", 2)	 	#Облако
	n = 2									#Количество повторных элементов облака
	kuchnost = 1 / 3 * radius					#Кучность (отклонение от оси)
	horizont = True
	draw_circles(x, y, radius, n, kuchnost, horizont)	
	
def draw_sun(x, y, radius):
	""" Рисуем солнце	"""
	change_color("Black","Yellow", 2)
	circle(x, y, radius)
	
		
def draw_house_and_tree(win_width,win_height, plus_x, minus_y, k):
			
	x = k * (win_width / 10)	+ plus_x							#нижняя левая точка дома
	y = k * (win_height * 4 / 5)+ minus_y
	height = k * win_width / 4							#высота и ширина дома
	width = k * win_width / 5
		
	draw_house(x, y, height, width)

	x = k * 1 / 3 * win_width + plus_x								#нижняя левая точка дерева
	y = k * 3 / 4 * win_height + minus_y
	height = k * win_width / 4							#высота дерева
	radius = k * 24										#диаметр веток

	draw_tree(x, y, height, radius)	
	
def draw_clouds(win_width,win_height, plus_x, minus_y, k):
	x =   1 / 3 * win_width + plus_x								#нижняя левая точка облака
	y =  1 / 6 * win_height + minus_y
	radius = k * 20										#диаметр части облака

	draw_cloud(x, y, radius)	
	
	
win_height = 400									#размер окна
win_width = 600

windowSize(win_width,win_height)

draw_background(win_width,win_height)			#фон

plus_x = 0 			#Смещение координат
minus_y = 0
k = 1 				#Коэффицент уменьшения по размеру
draw_house_and_tree(win_width,win_height, plus_x, minus_y, k)

plus_x = 3 / 8 * win_width  
minus_y = win_height / 7
k = 0.7 				#Коэффицент уменьшения по размеру
draw_house_and_tree(win_width,win_height, plus_x, minus_y, k)
	
	
plus_x = - 1 / 12 * win_width   
minus_y = - win_height / 12
k = 0.9 				
draw_clouds(win_width,win_height, plus_x, minus_y, k)

plus_x =  1 / 4 * win_width  
minus_y =  0
k = 1.1 				
draw_clouds(win_width,win_height, plus_x, minus_y, k)

plus_x = 1 / 12 * win_width 
minus_y = 0
k = 0.7 				
draw_clouds(win_width,win_height, plus_x, minus_y, k)
	
x = 1 / 10 * win_width								#нижняя левая точка солнца
y = 1 / 7 * win_height
radius = 30										#диаметр солнца

draw_sun(x, y, radius)	
	
	
run()