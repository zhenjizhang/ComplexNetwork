import MySQLdb

db = MySQLdb.connect("localhost", "root", "1234", "test")
cur = db.cursor()

cur.execute("SELECT user_id FROM users")
user = []
question = []
#day1 begin done
#day2 begin done
#day3 begin done
#day4 begin done
#day5 begin done
#day6 begin done
#day7 wait
n = 0
while n <= 120000:
    row1 = cur.fetchone()
    print "n= %d\n" %n
    n = n + 1


n = 120001
while n <= 140681:  # read table users,and get 100 user_id
    row1 = cur.fetchone()
    user.append(int(row1[0]))
    n = n + 1
#day1 0--20000
#day2 20001--40000
#day3 40001--60000
#day4 60001--80000
#day5 80001--100000
#day6 100001--120000
#day7 120001--140681
e_id = 1
for x in user:  # users --> questions, x is user_id which in table users
    cur.execute("SELECT question_id FROM  questions WHERE post_user_id = %d" % x)
    n = 0
    tem = []
    weight = 0
    while n < 214400:
        row2 = cur.fetchone()  # row2 is question_id in table questions
        if row2 == None:
            pass
        else:
            question.append(int(row2[0]))
        n = n + 1
    for y in question:  # questions --> answers
        cur.execute("SELECT user_id FROM answers WHERE question_id = %d" % y)
        i = 0
        while i < 285237:
            row3 = cur.fetchone()  # row3 is user_id in table answers
            if row3 == None:
                pass
            else:
                if row3[0] == None:
                    pass
                else:
                    # you hua zhe li
                    cur.execute("INSERT INTO edges (q_u_id, a_u_id, weight) VALUES (%d, %d, 0)" % (x, row3[0]))
                    db.commit()
                    print 'qu->au: %s -> %s' % (x, row3[0])
                    # if tem == [x, row3[0]]:
                    #     weight = weight + 1
                    #     cur.execute("UPDATE edges SET weight = %d WHERE id = %d" % (weight, e_id))
                    #     db.commit()
                    #     print "weight = %d\n" %weight
                    # else:
                    #     cur.execute("INSERT INTO edges (q_u_id, a_u_id, weight) VALUES (%d, %d, 0)" % (x, row3[0]))
                    #     db.commit()
                    #     e_id = e_id + 1
                    #     # get user_id in table answers
                    #     # insert x and row3[0]
                    #     weight = 0
                    # tem = [x, row3[0]]
            i = i + 1
    # following code is test code
    # if question == []:
    #     pass
    # else:
    #     print 'x=%s' % x, question
    question = []

cur.close()
db.close()

