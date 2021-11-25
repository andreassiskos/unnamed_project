from ripe.atlas.cousteau import AtlasResultsRequest
import time

def get_measurement(pk):

	kwargs = {
	    "msm_id": pk
	}

	results = []
	try:

		is_success, results = AtlasResultsRequest(**kwargs).create()
	except:
		print("Please insert another measurement ID")
	is_success, results = AtlasResultsRequest(**kwargs).create()

	return results


def get_traceroute_hops(pk):

	l_probe_with_hops = []
	trace_list = get_measurement(pk)

	for result in trace_list:
		
		
		d_probe_results = {}
		
		l_with_total_hops = []


		probe_id = result["prb_id"]
		d_probe_results[probe_id] = {}

		for hop in result["result"]:
			d_hops = {}
			l_rtts 			= []
			d_hops["hop"] 	= hop["hop"]
			try:
				d_hops["ip"] 	= hop["result"][0]["from"]
			
				for traceroutes in hop["result"]:
					l_rtts.append(traceroutes["rtt"])
					d_hops["rtts"] 	= l_rtts
			except :
				d_hops["ip"] = "*"
				d_hops["rtts"] = "*"

			l_with_total_hops.append(d_hops)
			#print(d_hops)

		d_probe_results[probe_id] = l_with_total_hops

		#print(d_probe_results)
			

		l_probe_with_hops.append(d_probe_results)

	return(l_probe_with_hops)


def l_data_for_edges(l_hops_per_probe):
	#print("Here: " + str(l_hops_per_probe))
	l_edges_per_hop = []
	
	for num_of_node in range(0, len(l_hops_per_probe) - 1):
		
		node1_id = str(l_hops_per_probe[num_of_node]["data"]["id"])
		node2_id = str(l_hops_per_probe[num_of_node + 1]["data"]["id"])

		hop_edge_data = {'data': {'source': node1_id, 'target': node2_id}}

		l_edges_per_hop.append(hop_edge_data)

	return l_edges_per_hop

def l_data_for_nodes(data):
		
	l_with_nodes = []
	l = []
	c_id_for_unknown_ips = 0
	for probes in data:
		#print(probes)

		l_with_nodes_for_calc_edges = []
		prb_id = str(list(probes.keys())[0])
		probe_node_data = {'data': {'id': 'prb_id_' + prb_id, 'label': 'probe ' + prb_id}}
		l_with_nodes_for_calc_edges.append(probe_node_data)
		l_with_nodes.append(probe_node_data)


		hops = (list(probes.values()))[0]
		
		
		for hop in hops:
			
			ip = hop["ip"]
			l.append(ip)
			if(ip != '*'):
				possible_hop_node_data = {'data': {'id': str(ip), 'label': str(ip)}}
				#if (possible_hop_node_data in l_with_nodes):
				#	pass
				#else:
				hop_node_data = possible_hop_node_data
				l_with_nodes_for_calc_edges.append(hop_node_data)

			else:
				hop_node_data = {'data': {'id': str(c_id_for_unknown_ips), 'label': str(ip)}}
				l_with_nodes_for_calc_edges.append(hop_node_data)
				c_id_for_unknown_ips += 1

			l_with_nodes.append(hop_node_data)

		edges = l_data_for_edges(l_with_nodes_for_calc_edges)
		
		for edge in edges:
			l_with_nodes.append(edge)


	
	#print(l_with_nodes)
	#l.sort()
	#print(l)	
	return l_with_nodes



def get_data_for_cyto(msm_id):

	l_with_data_for_cyto = []

	################	node data 		########################

	#print(list(get_traceroute_hops(msm_id)))
	prb_id 			= str(list(get_traceroute_hops(msm_id)[0].keys())[0])
	prb_ids_data 	= list(get_traceroute_hops(msm_id))

	nodes = l_data_for_nodes(prb_ids_data)
	
	'''
	
	prb_id_10020
	prb_id_3161
	prb_id_6175
	prb_id_631
	prb_id_6632



	for prb_id_data in prb_ids_data:
		#print(prb_id_data)
		prb_id = str(list(prb_id_data.keys())[0])
		#print(prb_id)

	

	probe_node_data = {'data': {'id': 'prb_id_' + prb_id, 'label': 'probe ' + prb_id}}
	l_with_data_for_cyto.append(probe_node_data)

	hops = list(get_traceroute_hops(msm_id)[0].values())[0]
 
	c_id_for_unknown_ips = 0
	for hop in hops:
		ip = hop["ip"]

		if(ip != '*'):
			hop_node_data = {'data': {'id': str(ip), 'label': str(ip)}}
		else:
			hop_node_data = {'data': {'id': str(c_id_for_unknown_ips), 'label': str(ip)}}
			c_id_for_unknown_ips += 1

		l_with_data_for_cyto.append(hop_node_data)



	################	edge data 		########################

	#{'data': {'source': 'one', 'target': 'two'}}
	

	for num_of_node in range(0, len(l_with_data_for_cyto) - 1):
		
		
		node1_id = str(l_with_data_for_cyto[num_of_node]["data"]["id"])
		node2_id = str(l_with_data_for_cyto[num_of_node + 1]["data"]["id"])

		hop_edge_data = {'data': {'source': node1_id, 'target': node2_id}}

		l_with_data_for_cyto.append(hop_edge_data)
	'''

	return nodes


#print(get_data_for_cyto(28550687))

'''

l_with_data_for_cyto = []
data_of_one_probe = get_traceroute_hops(28298578)[4]

################	node data 		########################

prb_id = str(list(get_traceroute_hops(28298578)[4].keys())[0])

probe_node_data = {'data': {'id': 'prb_id_' + prb_id, 'label': 'probe ' + prb_id}}
l_with_data_for_cyto.append(probe_node_data)

hops = list(get_traceroute_hops(28298578)[4].values())[0]

c_id_for_unknown_ips = 0
for hop in hops:
	ip = hop["ip"]


	if(ip != '*'):

		hop_node_data = {'data': {'id': str(ip), 'label': str(ip)}}
	else:
		hop_node_data = {'data': {'id': str(c_id_for_unknown_ips), 'label': str(ip)}}
		c_id_for_unknown_ips += 1

	l_with_data_for_cyto.append(hop_node_data)



################	edge data 		########################

#{'data': {'source': 'one', 'target': 'two'}}


for num_of_node in range(0, len(l_with_data_for_cyto) - 1):
	
	
	node1_id = str(l_with_data_for_cyto[num_of_node]["data"]["id"])
	node2_id = str(l_with_data_for_cyto[num_of_node + 1]["data"]["id"])

	hop_edge_data = {'data': {'source': node1_id, 'target': node2_id}}

	l_with_data_for_cyto.append(hop_edge_data)


print(l_with_data_for_cyto)
'''