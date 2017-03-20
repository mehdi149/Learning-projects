import os
import pygame



class PetriNet:
	WINDOW_W = 640
	WINDOW_H = 480
	ITEM_DISTANCE = 60
	TRANSITION_W = 40
	TRANSITION_H = 40
	PLACE_R = 20
	PLACE_T = 0

	def __init__(self,initial_transition,final_transitions,transitions,places,arcs):
		self.positionX = 20
		self.positionY =  WINDOW_H/2
		self.initial_transition = []
		self.final_transitions = []
		self.transitions =[]
		self.places=[]
		self.tokens=[]
	def draw(self):
		pygame.draw.circle(screen, WHITE, self.position, PLACE_R,PLACE_T)
		self.positionX += ITEM_DISTANCE
		positionAvant = (self.positionX,self.positionY)
		for transition in self.initial_transition:
			if self.positionY > WINDOW_H:
				self.positionY = positionAvant
				self.positionY
			pygame.draw.rect(screen, WHITE, (self.positionX, self.positionY, TRANSITION_H, TRANSITION_W))
			self.positionY +=ITEM_DISTANCE





	def replay():
		pass
