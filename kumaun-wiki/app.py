# h3avren

import sqlite3
from flask import Flask, redirect, render_template, request, url_for

# global variables
logged_in = 0

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home(logged_in = logged_in):
    return render_template('home.html', logged_in = logged_in)

@app.route('/search', methods = ['POST'])
def search():
    if request.method == 'POST':
        topic = request.form['search_value'].lower()
        with open('articles.txt','r') as file:
            text = file.read()
        if(topic in text):
            return render_template(f"{topic.replace(' ', '_')}.html")
        else:
            return "Error..!"

@app.route('/login_page')
def login_page():
    global logged_in
    if(logged_in):
        print(logged_in)
        return render_template('home.html',logged_in = logged_in)
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    global logged_in
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('website.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT Password FROM Users WHERE Username'\
                        ' = (:username)',{'username' : username})
            try:
                db_password = cur.fetchall()[0][0]
                if(db_password == password):
                    logged_in = 1
                else:
                    return ('Wrong Password Entered..!')
            except:
                return ('Username Not Found..!')

    return render_template('home.html', logged_in = logged_in)

@app.route('/create_article')
def create_article():
    global logged_in
    if(logged_in != 0):
        return render_template('create_articles.html')
    return "You need to Login First..!"

@app.route('/post_article', methods=['POST'])
def post_article():
    global logged_in
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect('articles.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO Articles (Title, Content) values (:title, :content)',
                        {'title': title, 'content' : content})
            conn.commit()
        return render_template('home.html', logged_in = logged_in)

@app.route('/signup_page')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('website.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO Users (Username, Password)'\
                        ' VALUES (:username, :password)',
                        {'username' : username, 'password' : password})
            conn.commit()
        return redirect(url_for('login_page'))
    else:
        return 'Error..!'

@app.route('/logout')
def logout():
    global logged_in
    logged_in = 0
    return render_template('home.html', logged_in = logged_in)


