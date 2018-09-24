from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask import jsonify


application = app = Flask(__name__)
# add your database credentials below
app.config['MYSQL_HOST'] = 'myRDSEndpoint'
app.config['MYSQL_USER'] = 'myRDSUsername'
app.config['MYSQL_PASSWORD'] = 'myRDSPassword'
app.config['MYSQL_DB'] = 'myRDSDBName'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
CORS(app)


# data from test_teams_rand
@app.route('/')
def get():
    cur = mysql.connect.cursor()
    cur.execute('''select * from test_teams_rand''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'test_teams_rand' : r})


# data from test_teams_rand for table on webpage
@app.route('/display10')
def display10():
    cur = mysql.connect.cursor()
    cur.execute('''select * from test_teams_rand ORDER BY team_id DESC LIMIT 10;''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'test_teams_rand' : r})


# get 10 results from test_soccer_rand for visualization
@app.route('/next10')
def next10():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_teams_rand ORDER BY team_id DESC LIMIT 10;''')
    returnvals = jsonify(cur.fetchall())
    return returnvals


# get 10 results from test_soccer_rand for visualization
@app.route('/check')
def check():
    count_dict = {}
    count_dict['count'] = []
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_teams_rand;''')
    returnvals = cur.fetchall()
    for result in returnvals:
        count_dict['count'].append(result[0])
    # count_arr = []
    if len(count_dict['count']) > 100:
        cur.execute('''DELETE FROM test_teams_rand ORDER BY team_id ASC LIMIT 10''')
        mysql.connection.commit()
        return "Done"
    else:
        return jsonify(count_dict)


# get 10 results from test_soccer_rand for visualization
@app.route('/to_react')
def to_react():
    game_dict = {}
    game_dict['team_name'] = []
    game_dict['team_noofwins'] = []
    game_dict['team_goals'] = []
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_teams_rand ORDER BY team_id DESC LIMIT 10;''')
    returnvals = cur.fetchall()
    for result in returnvals:
        game_dict['team_name'].append(result[1])
        game_dict['team_noofwins'].append(result[2])
        game_dict['team_goals'].append(result[3])
    return jsonify(game_dict)


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5001)