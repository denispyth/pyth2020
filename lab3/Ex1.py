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



polygon([(x-radius,y-radius), (x-radius+5,y-radius-5),							# лев бровь
         (x,y-radius_eyes/2), (x-10,y-radius_eyes/2+5)])

		 
polygon([(x+20,y-radius_eyes/3+5), (x+10,y-radius_eyes/3),							# прав бровь
         (x+radius,y-radius+20), (x+radius+5,y-radius+30)])
		 
		 
polygon([(x-x/2,y+radius_eyes), (x+x/2,y+radius_eyes),							# рот
         (x+x/2,y+20+radius_eyes), (x-x/2,y+20+radius_eyes)])
	
run()