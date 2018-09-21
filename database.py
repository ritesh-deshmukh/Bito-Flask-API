from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql3257909'
app.config['MYSQL_PASSWORD'] = '4huh44rjk1'
app.config['MYSQL_DB'] = 'sql3257909'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT data FROM test WHERE id = 1''')
    return_value = cur.fetchall()
    return str(return_value)

@app.route('/addone/<string:insert>')
def add(insert):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT MAX(id) FROM test''')
    maxid = cur.fetchone()  # (10,)
    cur.execute('''INSERT INTO test (id, data) VALUES (%s, %s)''', (maxid[0] + 1, insert))
    mysql.connection.commit()
    return "Done"

@app.route('/getall')
def getall():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM test''')
    returnvals = cur.fetchall()  # ((1, "ID1"), (2, "ID2"),...)

    printthis = ""
    for i in returnvals:
        printthis += str(i) + "<br>"

    return printthis



if __name__ == '__main__':
    app.run(debug=True)
