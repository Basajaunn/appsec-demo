from flask import Flask, render_template, request, session, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import db

app = Flask(__name__)
app.secret_key = "super-secure-secret-key"

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
    
        flash('Account was created!')
        return redirect(url_for("login"))
    return render_template('register.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.get_user(username)

        if user and check_password_hash(user["password_hash"], password):
            session['username'] = user['username']
            flash('Login was successful')
            return redirect(url_for("home")
        else:
            flash("Invalid username and/or password")
            return redirect(url_for("login"))

    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
