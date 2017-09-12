import networkx as nx
import matplotlib.pyplot as plt
import MySQLdb

db = MySQLdb.connect("localhost","root","1234","test" )
cursor = db.cursor()
# print db
G = nx.DiGraph()
# for x in xrange(0, 10):
#     G.add_node(x)
# G.add_nodes_from([3, 4, 5, 6])
# G.add_cycle([1, 2, 3, 4])
# G.add_edge(1, 3)
# G.add_edges_from([(3, 5), (3, 6), (6, 7)])
cursor.execute("SELECT * FROM users")
n=0
while n < 140681:
    row = cursor.fetchone()
    print int(row[0])
    G.add_node(int(row[0]))
    n = n + 1


cursor.execute("SELECT * FROM edges")
n = 0
while n < 166272:
    row = cursor.fetchone()
    if row == None:
        break
    print "%d, %s, %s" % (row[0], row[1], row[2])
    G.add_edge(int(row[1]),int(row[2]))
    n = n + 1

# print "Number of rows returned: %d" % cursor.rowcount
cursor.close()
db.close()
# nx.draw_networkx_nodes(G, pos = nx.spring_layout(G),alpha = 0.8, width = 0.01)
nx.draw(G, node_size=1, pos=nx.random_layout(G), with_labels=False, alpha = 0.8, width = 0.01)
plt.savefig("zzj.png")
plt.show()