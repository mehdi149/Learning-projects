import sys
from enum import Enum
import itertools
import pygame
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
################################################################
#   		(c) Copyright 2017 all right reserved   
#       Python Implementation of Heuristic miner algorithm           
#		This implementation is inspired by the book 
#	"Process Mining Data science in action by WILL VAN DER AALST"
#													
#
#
#
#
#################################################################

__author__ = "Bahra Mehdi"
__copyright__ = "Copyright 2017, The learning Project"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "bahra.mehdi1@gmail.com"
__status__ = "Test"



class HeuristicMiner:


	def __init__(self,Traces,params={'frequency'= None ,'window_width'= None}):

		#frequency of causality relation between two transitions 
		self.frequency = frequency
		# traces within an event log
		self.traces = traces
		# window width to extract logical pattern between events 
		self.window_width = self.params['window_width']
		self.frequency = self.params['frequency']
		# set of transitions 
		self.transitions = set()

	def count_frequencies(self):
		for trace in self.traces:
			for event1 in trace:
				for event2 in trace:
					pass

		pass

	def extract_DependencyGraph(self):
		pass
	def heuristic_window(self):
		pass

	def extract_Cnets(self):
		pass
	def show(self):
		passs
