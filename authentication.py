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

@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')


@app.route('/authenticate', methods=['POST'])
def login():
    userId = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM user WHERE userid=? AND pass=?"
    cursor.execute(query, (userId, password))
    
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result is not None:
        session['userId'] = userId
        return redirect('/home')
    else:
        return redirect('/loginpage?message=Invalid%20username%20or%20password')
    
@app.route('/home')
def home():
    userId = session.get('userId')
    name = None  # Assign a default value to the name variable
    
    if userId:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        query = "SELECT name FROM user WHERE userid=?"
        cursor.execute(query, (userId,))
        
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result is not None:
            name = result[0]
            
    if name is not None:
        return render_template('home.html', namePlace=name)
    else:
        return redirect('/loginpage')

@app.route('/newuser', methods=['POST'])
def insert():
    userId = request.form['username']
    
    password = request.form['password']
    name = request.form['name']
    branch = request.form['branch']
    hobbies = request.form['hobbies']
    languages = request.form['languages']
    contact = request.form['contact']
    sleep = request.form['sleep']
    description = request.form['description']
    age = request.form['age']
    
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "insert into user values (?,?,?,?,?,?,?,?,?,?,'','')"
    cursor.execute(query, (userId, name,age,branch,languages,hobbies,sleep,description,contact,password))
    print(newquery)
    conn.commit()
    cursor.close()
    conn.close()
    
    session['userId'] = userId
    return redirect('/home')
    
    
if __name__ == '__main__':
    app.run(debug=True)
