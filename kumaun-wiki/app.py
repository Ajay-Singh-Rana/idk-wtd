# h3avren

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search', methods = ['POST'])
def search():
    return render_template('search_results_page.html', data = request.form)

