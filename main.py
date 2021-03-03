import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.clock import Clock

class Game(Widget):
	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		self.speed = 5
		self.moving = False
		self.direction_x = "Right"
		self.direction_y = "Up"
		self.const_x, self.const_y = 200, 300
		
		#background
		with self.canvas:
			Color(rgb=(0, 0.7, 1))
			self.background = Rectangle(size=(1500, 800), pos=(0, 0))
			
		#health
		self.health = 200
		self.decrease = 0.10
		with self.canvas:
			Label(text="Health: ", pos=(30, 625), font_size=40, color=(0, 1, 0, 1))
			Color(rgb=(0, 1, 0))
			self.health_bar = Rectangle(size=(self.health, 50), pos=(150, 650))
			
		#the shark
		self.x, self.y = 200, 300
		with self.canvas:
			Color(rgb=(0, .9, 1))
			self.s1 = Rectangle(size=(200, 100), pos=(self.x, self.y))
			self.s2 = Ellipse(size=(100, 100), pos=(self.x+150, self.y), angle_start=-360, angle_end=-180)
			self.s3 = Triangle(points=[self.x, self.y, self.x, self.y+100,self.x-50 , self.y+50])
			self.s4 = Triangle(points=[self.x-100, self.y, self.x-100, self.y+100, self.x-50 , self.y+50])
			self.s5 = Triangle(points=[self.x + 125, self.y+100, self.x+125, self.y+150, self.x+175 , self.y+100])
			
			Color(rgb=(0, 0, 0))
			self.s6 = Line(points=[self.x+190, self.y+20, self.x+190, self.y+80], width=0.5)
			self.s7 = Ellipse(size=(10, 10), pos=(self.x+210, self.y+50))
			self.s8 = Line(points=[self.x+200, self.y+70, self.x+225, self.y+60], width=2)
			self.s9 = Line(points=[self.x+120, self.y+70, self.x+120, self.y+30], width=1)
			self.s10 = Line(points=[self.x+140, self.y+70, self.x+140, self.y+30], width=1)
			self.s11 = Line(points=[self.x+160, self.y+70, self.x+160, self.y+30], width=1)
			
			Color(rgb=(1, 1, 1))
			self.s12 = Ellipse(size=(30, 40), pos=(self.x+210, self.y+10), angle_start=90, angle_end=270)
			
			Color(rgb=(0, 0, 0))
			self.s13 = Line(points=[self.x+215, self.y+15, self.x+215, self.y+30], width=1)
			self.s14 = Line(points=[self.x+225, self.y+10, self.x+225, self.y+30], width=1)
			self.s15 = Line(points=[self.x+235, self.y+15, self.x+235, self.y+30], width=1)
			
			#game over
			self.game_over = False
			self.game_over_label = Label(text="", pos=(700, 300), font_size=70, color=(1, 0, 0, 1))
			self.add_widget(self.game_over_label)
			
			Clock.schedule_interval(self.play, 0)
			
	def play(self, dt):
		#update health
		if self.health > 0:
			self.health -= self.decrease
		self.health_bar.size = (self.health, 50)
		
		#check game over
		if self.health <= 0:
			self.game_over = True
			self.speed = 0
			self.game_over_label.text = "Game Over"
		
		#moving
		if self.moving == True:
			if self.direction_x == "Right":
				self.x += self.speed
			elif self.direction_x == "Left":
				self.x -= self.speed
			if self.direction_y == "Up":
				self.y += self.speed
			elif self.direction_y == "Down":
				self.y -= self.speed
		
		#update shark position
		self.s1.pos = (self.x, self.y)
		self.s2.pos = (self.x+150, self.y)
		self.s3.points = [self.x, self.y, self.x, self.y+100,self.x-50 , self.y+50]
		self.s4.points = [self.x-100, self.y, self.x-100, self.y+100, self.x-50 , self.y+50]
		self.s5.points = [self.x + 125, self.y+100, self.x+125, self.y+150, self.x+175 , self.y+100]
		self.s6.points = [self.x+190, self.y+20, self.x+190, self.y+80]
		self.s7.pos = (self.x+210, self.y+50)
		self.s8.points = [self.x+200, self.y+70, self.x+225, self.y+60]
		self.s9.points = [self.x+120, self.y+70, self.x+120, self.y+30]
		self.s10.points = [self.x+140, self.y+70, self.x+140, self.y+30]
		self.s11.points = [self.x+160, self.y+70, self.x+160, self.y+30]
		self.s12.pos = (self.x+210, self.y+10)
		self.s13.points = [self.x+215, self.y+15, self.x+215, self.y+30]
		self.s14.points = [self.x+225, self.y+10, self.x+225, self.y+30]
		self.s15.points = [self.x+235, self.y+15, self.x+235, self.y+30]
		
	def on_touch_down(self, touch):
		self.const_x, self.const_y = touch.pos[0], touch.pos[1]
		if self.game_over == True:
			self.game_over = False
			self.health = 200
			self.speed = 5
			self.game_over_label.text = ""
		
	def on_touch_move(self, touch):
		self.moving = True
		if touch.pos[0] - self.const_x > 0:
			self.direction_x = "Right"
		elif touch.pos[0] - self.const_x < 0:
			self.direction_x = "Left"
		if touch.pos[1] - self.const_y > 0:
			self.direction_y = "Up"
		elif touch.pos[1] - self.const_y < 0:
			self.direction_y = "Down"
		#self.const_x, self.const_y = touch.pos[0], touch.pos[1]
			
	def on_touch_up(self, touch):
		self.moving = False

class MyApp(App):
	def build(self):
		return Game()
		
if __name__ == "__main__":
	MyApp().run()
