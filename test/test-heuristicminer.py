import sys 
sys.path.append("/Users/mac/Desktop/project/")
import learning.modules.process_mining.alpha_miner as Alpha



with open("log3.csv","r") as my_file :
	traces = {}
	contenu = my_file.read()
	events =contenu.split("\n")
	for event in events:
		case_id,activity = event.split(',')
		if case_id not in traces:
			traces[case_id] = []

		traces[case_id].append(activity)
	print(traces)