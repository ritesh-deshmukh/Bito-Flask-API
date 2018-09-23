from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask import jsonify


application = app = Flask(__name__)
app.config['MYSQL_HOST'] = 'myRDSEndpoint'
app.config['MYSQL_USER'] = 'myRDSUsername'
app.config['MYSQL_PASSWORD'] = 'myRDSPassword'
app.config['MYSQL_DB'] = 'myRDSDBName'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
CORS(app)


# get 10 results from test_soccer_rand for visualization
@app.route('/next10')
def next10():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_soccer_rand ORDER BY team_id DESC LIMIT 10;''')
    returnvals = jsonify(cur.fetchall())
    return returnvals

# get 10 results from test_soccer_rand for visualization
@app.route('/to_react')
def to_react():
    game_dict = {}
    game_dict['team_name'] = []
    game_dict['team_opponent'] = []
    game_dict['match_date'] = []
    game_dict['team_winner'] = []
    game_dict['team_winner_goals'] = []
    game_dict['team_other_goals'] = []
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from test_soccer_rand ORDER BY team_id DESC LIMIT 10;''')
    returnvals = cur.fetchall()
    for result in returnvals:
        game_dict['team_name'].append(result[1])
        game_dict['team_opponent'].append(result[2])
        game_dict['match_date'].append(result[3])
        game_dict['team_winner'].append(result[4])
        game_dict['team_winner_goals'].append(result[5])
        game_dict['team_other_goals'].append(result[6])

    # return jsonify( game_dict['match_date'], game_dict['team_name'])
    # return str(game_dict)
    return jsonify(game_dict)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='127.0.0.1', port=5001)