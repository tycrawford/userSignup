from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True   

@app.route("/")
def index():
    something = 5
    return render_template('home.html')

app.run()

