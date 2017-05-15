import sys 
sys.path.append("/Users/mac/Desktop/project/")
import learning.modules.process_mining.alpha_plus as Alpha

from sortedcontainers import SortedList, SortedSet, SortedDict



with open("test_alphaplus2.csv","r") as my_file :
	traces = SortedDict()
	contenu = my_file.read()
	events =contenu.split("\n")
	for event in events:
		case_id,activity = event.split(',')
		if case_id not in traces:
			traces[case_id] = []

		traces[case_id].append(activity)
	print(traces)
	
Alph_plus = Alpha.Alpha_plus(traces)

print("L1L ",Alph_plus.extract_L1L())
print("TPRIME ",Alph_plus.extract_Tprime())
print(Alph_plus.extract_FL1L())
print(Alph_plus.extract_WmL1L())
Alph_plus.run_alphaMiner()
Alph_plus.extract_PetriNet()
Alph_plus.show(model='petrinet')
