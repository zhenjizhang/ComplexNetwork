import MySQLdb
import networkx as nx
import matplotlib.pyplot as plt

db = MySQLdb.connect("localhost","root","1234","test")
cur = db.cursor()
G = nx.DiGraph()

def drawG(userid):
    cur.execute("SELECT q_u_id, a_u_id FROM edges_done WHERE q_u_id = %d OR a_u_id = %d" %(userid,userid))
    T = True
    countEdge = 0
    userList = []
    while T:
        row = cur.fetchone()
        if row != None:
            G.add_edge(int(row[0]),int(row[1]))
        else:
            T = False
        countEdge = countEdge + 1
        # print countEdge
#--------------------------------------------------------------------------------#
    cur.execute("SELECT a_u_id FROM edges_done WHERE q_u_id = %d" %userid)
    T = True
    while T:
        row = cur.fetchone()
        if row != None:
            userList.append(int(row[0]))
        else:
            T = False
    nx.draw(G,pos=nx.random_layout(G), with_labels=True,alpha = 0.6, node_size=50,width=1)
    # plt.savefig("%d.png" %userid)
    # plt.show()
    G.clear()
    print "who ask = ",userid
    return userList

# cur1 = db.cursor()
# cur1.execute("SELECT * FROM pagerank ORDER BY pr DESC")
# T = True
# i=0
# while T:
#     row = cur1.fetchone()
#     if row != None:
#         cur.execute("INSERT INTO rank(user_id,PR) VALUE (%d,%f)"%(int(row[0]),float(row[1])))
#         db.commit()
#     else:
#         T =False
#     i = i + 1
#     print i
# cur1.close()
# cur.close()

def getAttr(userList):
    for userid in userList:
        cur.execute("SELECT * FROM rank WHERE user_id= %d" % userid)
        row = cur.fetchone()
        print "a_userid = ", userid, "rank = ",row[0]," PR = ",row[2]
    return 1

def main(numOfuser = 10):
    user = []
    n = 0
    cur.execute("SELECT user_id FROM rank")
    while n < numOfuser:
        row = cur.fetchone()
        user.append(int(row[0]))
        n = n + 1

    for userid in user:
        userList = drawG(userid)
        getAttr(userList)

if __name__ == '__main__':
    main(20)
    cur.close()
    db.close()