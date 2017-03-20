import sys 
sys.path.append("/Users/mac/Desktop/project/")
import learning.modules.process_mining.alpha_miner as Alpha



with open("log6.csv","r") as my_file :
	traces = {}
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
print(Alph.show(model = "petrinet"))





