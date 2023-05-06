from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def display_users():
    return redirect(url_for('login'))

@app.route('/user/<userid>')
def display_user(userid):
    # Connect to the database
    conn = sqlite3.connect('hox.db')

    c = conn.cursor()

    # Retrieve user information from the user_info table based on the provided user ID
    c.execute('SELECT * FROM user WHERE userid = ?', (userid,))
    user = c.fetchone()

    # Close the database connection
    c.close()

    # Render the user information in an HTML template
    return render_template('user.html', user=user, name=user[1], age=user[2], branch=user[3], language=user[4], hobbies=user[5], sleep=user[6], about=user[7], contact=user[8])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Connect to the database
        conn = sqlite3.connect('hox.db')
        c = conn.cursor()

        # Retrieve user information from the user_info table based on the provided user ID and password
        userid = request.form['userid']
        password = request.form['password']
        c.execute('SELECT * FROM user WHERE userid = ? AND pass = ?', (userid, password,))
        user = c.fetchone()

        # Close the database connection
        c.close()

        # Check if user exists in the database and the password is correct
        if user:
            session['userid'] = userid
            # Redirect to the home page after successful login
            return redirect(url_for('home'))
        else:
            # Render the login page with an error message
            return render_template('login.html', error="invalid")
    else:
        # Render the login page
        return render_template('login.html', error=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Connect to the database
        conn = sqlite3.connect('hox.db')
        c = conn.cursor()

        # Retrieve user information from the signup form
        userid = request.form['userid']
        name = request.form['name']
        age = request.form['age']
        branch = request.form['branch']
        language = request.form['language']
        hobbies = request.form['hobbies']
        sleep = request.form['sleep']
        about = request.form['about']
        contact = request.form['contact']
        password = request.form['password']

        # Check if user already exists in the database
        c.execute('SELECT * FROM user WHERE userid = ?', (userid,))
        user = c.fetchone()
        if user:
            # Render the signup page with an error message
            return render_template('signup.html', error=True)
        else:
            # Add the new user information to the database
            c.execute('INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                      (userid, name, age, branch, language, hobbies, sleep, about, contact, password,))
            conn.commit()

            # Store the user ID in the session
            session['userid'] = userid

            # Close the database connection
            c.close()

            # Redirect the user to their home page
            return redirect(url_for('home'))

    # Render the signup page
    return render_template('signup.html', error=False)

@app.route('/home')
def home():
    # Check if user is logged in
    if 'userid' in session:
        # Connect to the database
        conn = sqlite3.connect('hox.db')
        c = conn.cursor()

        # Retrieve all users from the user_info table except the current user
        c.execute('SELECT * FROM user WHERE userid != ?', (session['userid'],))
        users = c.fetchall()

        # Close the database connection
        c.close()

        # Render the user list in an HTML template
        return render_template('home.html', users=users)
    else:
        # Redirect to the login page if user is not logged in
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
