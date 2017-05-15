import sys 
sys.path.append("/Users/mac/Desktop/project/")
import learning.modules.process_mining.alpha_miner as Alpha
from sortedcontainers import SortedList, SortedSet, SortedDict



with open("log3.csv","r") as my_file :
	traces = SortedDict()
	contenu = my_file.read()
	events =contenu.split("\n")
	for event in events:
		case_id,activity = event.split(',')
		if case_id not in traces:
			traces[case_id] = []

		traces[case_id].append(activity)
	print(traces)


Alph = Alpha.AlphaMiner(traces)

print(Alph.getInitialTransitions())
print(Alph.getFinalTransitions())
print(Alph.getTransitions())
print(Alph.extractRelations())
print(Alph.computePairs())
print(Alph.extract_maximal_pairs())
print(Alph.add_places())
Alph.extract_PetriNet()
print(Alph.show(model = "petrinet"))





