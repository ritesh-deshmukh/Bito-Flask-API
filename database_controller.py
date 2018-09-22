from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask import jsonify
from random import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'myRDSEndpoint'
app.config['MYSQL_USER'] = 'myRDSUsername'
app.config['MYSQL_PASSWORD'] = 'myRDSPassword'
app.config['MYSQL_DB'] = 'myRDSDBName'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
CORS(app)


# test route with DB for GET
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT team_name,team_opponent,team_winner FROM test_soccer WHERE team_id = 1''')
    return_value = cur.fetchall()
    return str(return_value)


# test route with DB for insert
@app.route('/addone/<string:insert>')
def add(insert):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT MAX(id) FROM test''')
    maxid = cur.fetchone()  # (10,)
    cur.execute('''INSERT INTO test (id, data) VALUES (%s, %s)''', (maxid[0] + 1, insert))
    mysql.connection.commit()
    return "Done"


@app.route('/getall', methods=['GET'])
def getall():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM test_soccer;''')
    returnvals = cur.fetchall()  # ((1, "ID1"), (2, "ID2"),...)

    printthis = []
    # for i in returnvals:
    #     printthis += str(i) + "<br>"
    for num in returnvals:
        printthis.append(num[0])

    print_in_json = jsonify(printthis)
    return print_in_json

# send data to test_soccer_rand in DB
@app.route('/insert_new')
def insert_new():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_soccer ORDER BY team_id DESC LIMIT 10;''')
    # returnvals = cur.fetchall()[0][1]
    returnvals = cur.fetchall()
    for result in returnvals:
        team_name, team_opponent, match_date, team_winner, team_winner_goals, team_other_goals = \
            result[1], result[2], result[3], result[4], result[5], result[6]
        cur.execute('''INSERT INTO test_soccer_rand (team_name, team_opponent, match_date, team_winner, team_winner_goals, team_other_goals) 
                        VALUES (%s, %s, %s, %s, %s, %s)''', (team_name, team_opponent, match_date, team_winner, team_winner_goals, team_other_goals))
    mysql.connection.commit()
    return str(returnvals)

# send data to test_soccer_rand in DB
@app.route('/insert_rand')
def insert_rand():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_soccer ORDER BY team_id DESC LIMIT 10;''')
    # returnvals = cur.fetchall()[0][1]
    returnvals = cur.fetchall()
    for result in returnvals:
        team_name, team_opponent, match_date, team_winner, team_winner_goals, team_other_goals = \
            result[1], result[2], result[3], result[4], result[5], result[6]
        cur.execute('''INSERT INTO test_soccer_rand (team_name, team_opponent, match_date, team_winner, team_winner_goals, team_other_goals) 
                        VALUES (%s, %s, %s, %s, %s, %s)''', (team_name, team_opponent, match_date, team_winner, randint(4,6), randint(0,3)))
    mysql.connection.commit()
    return str(returnvals)




if __name__ == '__main__':
    app.run(debug=True)

