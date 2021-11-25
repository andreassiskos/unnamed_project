import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
from data_parser import ripe_atlas_data
import tkinter as tk







#28550687
#28696550
#28698880
#28697665


def plot_RIPE_traceroute(msm_id):

	traceroute_data = ripe_atlas_data.get_data_for_cyto(msm_id)
	G = nx.DiGraph()
	labels={}
	c = 0


	for probe_data in traceroute_data:
		print(probe_data)
		
		
		try:
			G.add_node(probe_data["data"]["id"])
			labels[probe_data["data"]["id"]] = probe_data["data"]["label"]
		except :
			G.add_edge(probe_data["data"]["source"], probe_data["data"]["target"])

	# same layout using matplotlib with no labels
	G.remove_edges_from(list(nx.selfloop_edges(G)))
	print("topological_sort")
	print(list(nx.topological_sort(G)))
	
	topo_sort = list(nx.topological_sort(G))
	
	mult_val_of_x = 1
	mult_val_of_y = 1 * mult_val_of_x

	d_pos_of_nodes = {}
	for node in topo_sort:
		d_pos_of_nodes[node] = {}
		d_pos_of_nodes[node]["x"] = (topo_sort.index(node) + 1) * mult_val_of_x
		d_pos_of_nodes[node]["y"] = 0

	print("d_pos_of_nodes")
	print(d_pos_of_nodes)
	roots = (v for v, d in G.in_degree() if d == 0)
	leaves = [v for v, d in G.out_degree() if d == 0]
	all_paths = []
	for root in roots:
		paths = nx.all_simple_paths(G, root, leaves)
		all_paths.extend(paths)
	all_paths.sort(reverse = True)

	print(20 * "=")

	l_pos = []
	for path in all_paths:
		print(path)
		print(all_paths.index(path) + 1)

		for node in path:
			if(d_pos_of_nodes[node]["y"] == 0):
				d_pos_of_nodes[node]["y"] = (all_paths.index(path) + 1) * mult_val_of_y
				if(d_pos_of_nodes[node]["y"] not in l_pos):
					l_pos.append(d_pos_of_nodes[node]["y"])
			else:
				continue

	print("d_pos_of_nodes")
	print(l_pos)

	d_pos = {}

	for key in d_pos_of_nodes.keys():
		d_pos_of_nodes[key]["y"] = (l_pos.index(d_pos_of_nodes[key]["y"]) + 1) * mult_val_of_y 
		print(key)
		d_pos[key] = (d_pos_of_nodes[key]["y"],d_pos_of_nodes[key]["x"])

	print(d_pos)
	print("d_pos")

	print(20 * "=")
	plt.title('Hierachical Drawing for Traceroute: ' + msm_id)
	pos = d_pos
	#pos = graphviz_layout(G, prog='dot')
	print(pos)
	print(20 * "=")
	l_xes = []
	l_yes = []
	for node in d_pos_of_nodes.keys():
		l_yes.append(d_pos_of_nodes[node]["y"])
		l_xes.append(d_pos_of_nodes[node]["x"])
	print("l_xes")
	l_xes.sort()
	print(l_xes)
	print("l_yes")
	l_yes.sort()
	print(l_yes)
	nx.draw_networkx_nodes(G, pos) # , node_size = 77 
	nx.draw_networkx_edges(G, pos, arrows=True)

	
	nx.draw_networkx_labels(G,pos,labels,font_size=7) #,labels,font_size=7
	plt.savefig('nx_test.png')

	plt.show()


def getSquareRoot ():
	msm_id = entry1.get()
	plot_RIPE_traceroute(msm_id)


root= tk.Tk()
root.title("The Still Unnamed Project")

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Welcome to:\n The Still Unnamed Project\nVersion: 0.0.1')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 40, window=label1)

label2 = tk.Label(root, text='Type the Measurement ID\nof RIPE Atlas Traceroute:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

button1 = tk.Button(text='Generate graph', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
