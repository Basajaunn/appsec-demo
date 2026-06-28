from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password_hash = generate_password_hash(password)
    
        db.create_user(username, password_hash)
    
        return f"User {username} has been created!"
    return render_template('register.html')
    

@app.route('/user/<username>')
def user(username):
    return f'Hello {username} !'


if __name__ == "__main__":
    app.run(debug=True)
