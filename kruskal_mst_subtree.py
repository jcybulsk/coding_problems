def find_shortest_edge(gr, curr, mst_nodes):
    num = len(gr.keys())
    ncurr = len(curr.keys())
    if (num > 0) & (ncurr == 0):
        # Take the shortest overall branch and start 
        # your tree with that one.
        min_br = 99999999
        min_ind = -1
        for i in range(num):
            if gr[i][2] < min_br:
                min_br = gr[i][2]
                min_ind = i
        return min_ind
    if (num > 0) & (ncurr > 0):
        # Look for the shortest branch among those 
        # nodes currently connected to the tree!
        # But be careful not to add a branch that 
        # creates a loop.
        min_br = long(999999)
        min_ind = -1
        for i in gr.keys():
            if gr[i][2] < min_br:
                if (gr[i][0] in mst_nodes) ^ (gr[i][1] in mst_nodes):
                    min_br = gr[i][2]
                    min_ind = i
        return min_ind
    if num == 0:
        return None


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

# I need to build some catalog of the edge lengths 
# between nodes, in order to select the MST later.
graph = {}
mst = {}
for a0 in xrange(m):
    x,y,r = raw_input().strip().split(' ')
    x,y,r = [int(x),int(y),int(r)]
    graph[a0] = [x, y, r]

# The goal here is to find a MST representation, 
# and add up the edge lengths in that MST. Start 
# with the shortest branch in the full set, and 
# then expand out to consider the next shortest 
# branch connected to the current MST, and so on.
curr_mst_nodes = []
sum_mst_edges = 0
for i in range(n-1):
    new_node_id = find_shortest_edge(graph, mst, curr_mst_nodes)
    # Take the new node, transplant it into the 
    # MST dictionary and pop it out of the current 
    # full node dictionary
    mst[new_node_id] = graph.pop(new_node_id, None)
    if mst[new_node_id][0] not in curr_mst_nodes:
        curr_mst_nodes.append(mst[new_node_id][0])
    if mst[new_node_id][1] not in curr_mst_nodes:
        curr_mst_nodes.append(mst[new_node_id][1])
    sum_mst_edges += mst[new_node_id][2]

# Finally, print the branch lengths of the MST
print sum_mst_edges
