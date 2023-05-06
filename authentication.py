from flask import Flask, render_template, request, redirect, url_for,session
import sqlite3

from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
cors = CORS(app)

@app.route('/', methods=['POST','GET'])
def main():
    return render_template('main.html')
@app.route('/loginpage', methods=['POST','GET'])
def loginpage():
    return render_template('loginpage.html')

@app.route('/authenticate', methods=['POST'])
def login():
    userId = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM Login WHERE UserID=? AND Password=?"
    cursor.execute(query, (userId, password))
    
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result is not None:
        session['userId'] = userId
        return redirect('/home')
    else:
        return redirect('/loginpage?message=Invalid%20username%20or%20password')

if __name__ == '__main__':
    app.run(debug=True)
