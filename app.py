from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    

@app.route('/user/<username>')
def user(username):
    return f'Hello {username} !'



if __name__ == "__main__":
    app.run(debug=True)
