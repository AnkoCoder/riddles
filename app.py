from flask import Flask, render_template, request
from sqlalchemy import func
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'something'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin = Admin(app, name='riddles')
db = SQLAlchemy(app)


class Riddle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(80), unique=True, nullable=False)
    answer = db.Column(db.String(80), unique=True, nullable=False)


class RiddleAdmin(ModelView):
    column_list=['id', 'question', 'answer']

admin.add_view(RiddleAdmin(Riddle, db.session))

@app.route('/')
def home():
    riddles = Riddle.query.all()
    return render_template('index.html', riddles=riddles)

@app.route('/riddle/<id>', methods=['GET', 'POST'])
def riddle(id):
    msg = ''
    riddle = Riddle.query.get(id)
    if request.method == 'POST':
        if request.form['answer'].lower() == riddle.answer.lower():
            msg = 'Вы угадали!'
        else:
            msg = 'Не угадали! Попробуйте еще раз'    
    return render_template('riddle.html', riddle=riddle, msg=msg)
