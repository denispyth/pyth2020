from graph import *

	
def change_color(c_line,c_bg, whight):
	penColor(c_line) 					# Цвет пера
	penSize(whight)  					# Толщина пера
	brushColor(c_bg)					# Цвет заливки


def main_circle(x,y, radius):
	change_color("Black","Yellow", 3)
	circle(x,y, radius)
	
	
def eye_circles(x,y, radius):
	brushColor("Red")	#fill
	circle(x,y, radius)
	brushColor("Black")	#fill
	circle(x,y, radius-(radius/3))
	
	


	
	
x = 200
y = 200
radius = 150
radius_eyes = 30
	
main_circle(x, y, radius) 								# x,y,radius - голова
eye_circles(x-radius/2, y-radius/5,radius_eyes) 		# x,y,radius - лев глаз
eye_circles(x+radius/2, y-radius/5,radius_eyes*0.7) 	# x,y,radius - прав глаз



polygon([(80,110), (70,120),							# лев бровь
         (220,300), (230,290)])

		 
polygon([(310,260), (390,130),							# прав бровь
         (400,140), (320,270)])
		 
		 
polygon([(140,400), (340,400),							# рот
         (340,420), (140,420)])
	
run()