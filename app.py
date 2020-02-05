from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='rk6239hx',
                             password='us10interstate39',
                             db='rk6239hx_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

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
    try:
        with connection.cursor() as cursor:
            # Gather a list of students
            sql = "SELECT * FROM Students"
                    
            # execute the SQL command
            cursor.execute(sql)
            
            # get the results
            for result in cursor:
                return result
            
            # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
            # So you must commit to save your changes. 
            # connection.commit()
    finally:
        connection.close()
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6239)