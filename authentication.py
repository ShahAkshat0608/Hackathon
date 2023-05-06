from flask import Flask, render_template, request, redirect, url_for,session,jsonify
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
    
    conn.commit()
    cursor.close()
    conn.close()
    
    session['userId'] = userId
    return redirect('/home')
    
@app.route('/matches')
def get_matches():
    userId = session.get('userId')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # get the user's liked list and convert to a list
    c.execute("SELECT like FROM user WHERE userid=?", (userId,))
    like_string = c.fetchone()[0]
    liked_list = like_string.split(',')

    # iterate through each person the user has liked
    matches = []
    for liked_person in liked_list:
        c.execute("SELECT like FROM user WHERE userid=?", (liked_person,))
        liked_string = c.fetchone()[0]
        if liked_string:
            liked_list = liked_string.split(',')
            if userId in liked_list:
                matches.append(liked_person)
    match_string = ','.join(matches)
    
    c.execute("update user set matches=? where userid = ?",(match_string,userId))
    conn.commit()  
   

    

    users_data=[]
    for user_id in matches:
        c.execute('SELECT * FROM user WHERE userid = ?', (user_id,))
        user_data = c.fetchone()
        user_dict = {
            
            'name': user_data[1],
            'study':user_data[3],
            'languages': user_data[4],
            'age':user_data[2]
        }
        users_data.append(user_dict)
    conn.close()
    return render_template('matches.html', users=users_data)

if __name__ == '__main__':
    app.run(debug=True)   

