import networkx as nx
import csv
with open('/Users/zhangzhenji/Desktop/answers2.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for stid,s,t in f_csv:
        print stid,s,t
        break

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edge(1,2)

print G