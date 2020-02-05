from flask import Flask, render_template
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='rk6239hx',
                             password='us10interstate39',
                             db='rk6239hx_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select from Students Table the name set as input
        sql = ("SELECT * FROM Students")
        
        # execute the SQL command
        cursor.execute(sql)
        output = cursor.fetchall()

finally: connection.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/database')
def database():
    return render_template('database.html', output=output)
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6239)