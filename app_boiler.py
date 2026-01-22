from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
@app.route('/')
def home():
    return render_template("")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("")

if __name__ == '__main__':
    app.run(debug=True)