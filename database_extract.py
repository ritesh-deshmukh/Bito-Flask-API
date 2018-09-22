from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(debug=True)