# h3avren

import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search', methods = ['POST'])
def search():
    print('hererwrwrwwrwwrwrwqrwrqwrqwer')
    print(request.method)
    print(request.form)
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
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        print(request.form['username'])
        print(request.form['password'])
    return redirect(url_for('home'))

@app.route('/create_article')
def create_article():
    return render_template('create_articles.html')

@app.route('/post_article', methods=['POST'])
def post_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect('articles.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO Articles (Title, Content) values (:title, :content)',
                        {'title': title, 'content' : content})
            conn.commit()
        return  redirect(url_for('home'))
