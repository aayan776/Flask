from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)""")
    con.commit()
    con.close()
init_db()

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        con.commit()
        con.close()
        return "User registered successfully"
    return render_template('register.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        con.close()
        
        if user:
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/resume', methods = ['POST'])
def resume():
    fullname = request.form['fullname']
    address = request.form['address']
    email = request.form['email']
    mobile = request.form['mobile']
    skills = request.form['skills']

    image = request.files['image']
    image_path = 'static/' + image.filename
    image.save(image_path)

    return render_template('/resume',
                        fullname = fullname,
                        address = address,
                        email = email,
                        mobile = mobile,
                        skills = skills,
                        image_path = image_path)
if __name__ == '__main__':
    app.run(debug = False)