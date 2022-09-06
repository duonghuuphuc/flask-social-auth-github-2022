# Filename: app.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template, redirect, url_for, jsonify
from flask_login import login_required, logout_user
from flask_dance.contrib.github import github
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'tHiS-iS-a-H@rD-tO-gUeSs-sTrInG'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# The import statement is placed here to avoid the circular import error
from oauth import github_blueprint
app.register_blueprint(github_blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    request = github.get('/user')
    username = request.json()["login"]
    return f"Your GitHub's username: {username}"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/test')
def test_func():
    return jsonify(test="200 OK")
