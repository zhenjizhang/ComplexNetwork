#coding:utf-8
__author__ = "zhangzhenji"

import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.Graph()

with open('/Users/zhangzhenji/Desktop/answers2.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for stid,s,t in f_csv:
        G.add_edge(s,t)
    print 'done'

prulist = []
with open('/Users/zhangzhenji/Desktop/pagerank.csv') as fpr:
    fpr_csv = csv.reader(fpr)
    headers = next(fpr_csv)
    for u,uid in fpr_csv:
        prulist.append(u)
# G.add_node(1)
# G.add_node(2)
# G.add_nodes_from([3,4,5,6])
# G.add_cycle([1,2,3])
# G.add_edge(1,4)
# G.add_edge(4,1)
# G.add_edges_from([(3,5),(3,6),(6,7)])
nx.draw(G,pos=nx.random_layout(G), alpha=0.6,with_labels=False, node_size=1,width=0.01)
# plt.savefig("zhangzhenji.png")
# plt.show()
n = 0
print "n = ",0,"     clustering = ",nx.average_clustering(G)
for uprid in prulist:
    G.remove_node(uprid) 
    n = n + 1
    if n == 1000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 2000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 3000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 4000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 5000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 6000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 7000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 8000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 9000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
    if n == 10000:
        print "n = ",n,"  clustering = ",nx.average_clustering(G)
        break
# pr = nx.pagerank(G,alpha=0.85)
# x = 0
# for node, value1 in pr.items():
#     x = x + value1
#     print "node = ",node,"value = ",value1
#     cur.execute("INSERT INTO pagerank (user_id, pr) VALUES (%d, %f)" % (node, value1))
#     db.commit()
# print(x)