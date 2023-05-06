from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_users():
    # Connect to the database
    conn = sqlite3.connect('hox.db')

    c = conn.cursor()

    # Retrieve all users from the user_info table
    c.execute('SELECT * FROM user')
    users = c.fetchall()

    # Close the database connection
    c.close()

    # Render the user list in an HTML template
    return render_template('home.html', users=users)

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
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
