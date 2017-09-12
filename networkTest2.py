#coding:utf-8
__author__ = "zhangzhenji"

import networkx as nx
import matplotlib.pyplot as plt
import MySQLdb

G = nx.Graph()
db = MySQLdb.connect("localhost","root","1234","test")
cur = db.cursor()

cur.execute("SELECT * FROM users")
i = 0
while i < 140681:
    row1 = cur.fetchone()
    G.add_node(int(row1[0]))
    i = i + 1
    print 140981 - i

cur.execute("SELECT * FROM edges_done")

i = 0
while i < 161435:
    row2 = cur.fetchone()
    G.add_edge(int(row2[1]),int(row2[2]),weight = int(row2[3]))
    i = i + 1
    print 161435 - i
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
print "n = ",0,"     clustering = ",nx.average_clustering(G)
T = True
n = 0
cur.execute("SELECT user_id FROM rank")
while T:
    row = cur.fetchone()
    if row != None:
        G.remove_node(int(row[0]))
    else:
        T = False
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
# pr = nx.pagerank(G,alpha=0.85)
# x = 0
# for node, value1 in pr.items():
#     x = x + value1
#     print "node = ",node,"value = ",value1
#     cur.execute("INSERT INTO pagerank (user_id, pr) VALUES (%d, %f)" % (node, value1))
#     db.commit()
# print(x)