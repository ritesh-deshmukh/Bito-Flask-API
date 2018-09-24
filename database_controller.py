from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask import jsonify
from random import *

application = app = Flask(__name__)
# add your database credentials below
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
    cur.execute('''SELECT * FROM test_teams WHERE team_id = 1''')
    return_value = jsonify(cur.fetchall())
    return return_value


# # test route with DB for insert
# @app.route('/addone/<string:insert>')
# def add(insert):
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT MAX(id) FROM test''')
#     maxid = cur.fetchone()  # (10,)
#     cur.execute('''INSERT INTO test (id, data) VALUES (%s, %s)''', (maxid[0] + 1, insert))
#     mysql.connection.commit()
#     return "Done"


@app.route('/getall', methods=['GET'])
def getall():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM test_teams;''')
    returnvals = cur.fetchall()
    printthis = []
    for num in returnvals:
        printthis.append(num[0])

    print_in_json = jsonify(printthis)
    return print_in_json


# send data to test_soccer_rand in DB
@app.route('/insert_new')
def insert_new():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_teams;''')
    returnvals = cur.fetchall()
    for result in returnvals:
        team_name, team_noofwins, team_goals = result[1], result[2], result[3]
        cur.execute('''INSERT INTO test_teams_rand (team_name, team_noofwins, team_goals) 
                        VALUES (%s, %s, %s)''', (team_name, team_noofwins, team_goals))
    mysql.connection.commit()
    return str(returnvals)


# send data to test_soccer_rand in DB
@app.route('/insert_random')
def insert_random():
    count_dict = {}
    count_dict['count'] = []
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_teams_rand;''')
    check_100 = cur.fetchall()
    for result in check_100:
        count_dict['count'].append(result[0])
    if len(count_dict['count']) > 100:
        cur.execute('''DELETE FROM test_teams_rand ORDER BY team_id ASC LIMIT 10''')
        mysql.connection.commit()
        return "<h1>Data Inserted</h1>"
    else:
        cur.execute('''SELECT * FROM test_teams;''')
        returnvals = cur.fetchall()
        for result in returnvals:
            team_name, team_noofwins, team_goals = result[1], result[2], result[3]
            cur.execute('''INSERT INTO test_teams_rand (team_name, team_noofwins, team_goals) 
                            VALUES (%s, %s, %s)''', (team_name, team_noofwins, randint(5,20)))
        mysql.connection.commit()
        return "<h1>Data Inserted</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

