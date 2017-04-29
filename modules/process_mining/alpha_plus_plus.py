import sys
from enum import Enum
import itertools
import pygame
import snakes.plugins
from learning.modules.process_mining.alpha_miner import AlphaMiner , Relations
from learning.modules.process_mining.alpha_plus import AlphaPlus
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *
################################################################
#   		(c) Copyright 2017 all right reserved   
#       Python Implementation of Alpha miner ++  algorithm           
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
__version__ = "0.0.1"
__email__ = "bahra.mehdi1@gmail.com"
__status__ = "Test"

class Relations_plus(Relations):
    SUCCESSIONS     = '>'
    RIGHT_CAUSALITY = '->'
    LEFT_CAUSALITY  = '<-'
    PARALLEL        = '||'
    CHOICES         = '#'
    XOR_JOIN 		=  '<|'
    XOR_SPLIT		= '|>'
    INDIRECTLY_FOLLOWED = '>>'


class AlphaPlusPlus(AlphaPlus):
	def __init__(self ,Traces):
        super().__init__(Traces)
        #traces within an event log
        self.traces = Traces
        # set of transitions that appear in loop of length one
        self.L1L = None
        # T' , traces minus L1L
        self.T_pr = None
        self.F_L1L = None
        self.Wm_L1L = SortedDict()
        self.alphaObject = None
    

    def extractRelations(self):
            #Extract non repetitive traces, alpha dont take care  about  frequencies !
        nnrep_traces = SortedSet()
        for trace in self.traces.values():
            nnrep_traces.add("".join(trace))
        print(nnrep_traces)
        #Extract relations between each transitions
        # generate Footprint
        for transition1 in self.transitions:
            self.relations[transition1] = SortedDict()
            for transition2 in self.transitions:
                concat = transition1+transition2
                concat_symetric_1 = transition1+transition2+transition1
                concat_symetric_2 = transition2+transition1+transition2

                print(concat)
                print(concat_symetric_1)
                print(concat_symetric_2)

                relation = None
                for trace in nnrep_traces:
                    
                    if relation == None :
                        if trace.find(concat) >= 0:
                            relation = Relations.RIGHT_CAUSALITY

                        elif trace.find(concat[::-1]) >= 0:
                            relation = Relations.LEFT_CAUSALITY
                    else:
                        if trace.find(concat) >= 0:
                            if relation == Relations.LEFT_CAUSALITY:
                                if trace.find(concat_symetric_1) <= 0 and trace.find(concat_symetric_2) <= 0:
                                    relation = Relations.PARALLEL
                        elif trace.find(concat[::-1]) >= 0:
                            if relation == Relations.RIGHT_CAUSALITY:
                                if trace.find(concat_symetric_1) <= 0 and trace.find(concat_symetric_2) <= 0:
                                    relation = Relations.PARALLEL  
                        elif                       

                if relation == None:
                    relation = Relations.CHOICES
                self.relations[transition1][transition2] = relation


        return self.relations

    def extract_L1L(self):
        #extract length one loop 
        self.L1L = SortedSet()
        super().getTransitions()
        #compute footprint and extract all transitions that have a causality relations with himself
        print(self.transitions)
        self.extractRelations()
        print(self.relations)
        for transition in self.transitions:
            if self.relations[transition][transition] == Relations.PARALLEL:
                self.L1L.add(transition)
        return self.L1L
    def extract_Tprime(self):
        # T' := T \ L1L
        self.T_pr = self.transitions.difference(self.L1L)
        return self.T_pr