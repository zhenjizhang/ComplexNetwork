import MySQLdb

db = MySQLdb.connect("localhost","root","1234","test")
cur = db.cursor()
cur1 = db.cursor()

cur.execute("SELECT user_id,reputation FROM users")
i = 0
while i < 107725:
    row = cur.fetchone()
    i = i + 1
    print i
n = 107725
while n < 141511:
    row = cur.fetchone()
    user_id = int(row[0])
    if row[1] != None:
        reputation = int(row[1])
        cur1.execute("UPDATE rank SET reputation = %d WHERE user_id = %d" % (reputation,user_id))
        db.commit()
    else:
        continue
    n = n + 1
    print n,"remain = ",141511 - n
cur.close()
cur1.close()
db.close()