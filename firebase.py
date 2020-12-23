from Pyrebase import pyrebase
from flask import *
from functions import code, timerFunction, test_strings
import random
import requests

config = {

    "apiKey": "AIzaSyAAtBuPe4aVoa_vm2bV9WVcfI7Pa4SakR0",
    "authDomain": "adivina-87126.firebaseapp.com",
    "databaseURL": "https://adivina-87126-default-rtdb.firebaseio.com",
    "projectId": "adivina-87126",
    "storageBucket": "adivina-87126.appspot.com",
    "messagingSenderId": "321353211600",
    "appId": "1:321353211600:web:98e6de42daf2d2a0a088d5",
    "measurementId": "G-NR8RJW3B0E"

}

questions = {
    "0":"Give %s a funny nickname","1":"Now, What rumour would you like to start about %s ?","2":"Great! now who do you think %s will end up marrying",
    "3":"What do you think %s should really work on ","4":"Why do you think %s is so depressed ...or happy for ?",
    "5":"What is the emoji you have always wanted to give %s ?","6":"Hmmm, In your opinion what funny thing %s might have been in previous life ?",
    "7":"If you have a coconut and %s with you. What will you do?","8":"What song you want to dance %s on","9":"Going good! And what song will you dance with %s on btw",
    "10":"Okay..., now Which song you always wanted %s to sing?","11":"What according to you satisfies %s the most ?"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
<<<<<<< HEAD
    x = 5
    val = timerFunction(x)
    db.child("questions").set(questions)
    return render_template('index.html', t=x)
        
    
=======
    # x = 5
    # val = timerFunction(x)
    # db.child("questions").set(questions)
    return render_template('index.html', t="Welcome to Adivina")

>>>>>>> 4f0042f18a0390247e3891b8e38a4cdc74db995b

@app.route('/get', methods=['GET', 'POST'])
def get_questions():
    if request.method == 'GET':
        questions = db.child("questions").get()
        return render_template('index.html', t=questions.val())
    return render_template('index.html')
    

@app.route('/generate', methods=['GET', 'POST'])
def generate_code():
    if request.method == 'POST':
        join_code = code()
        room = request.form['room']
<<<<<<< HEAD
        db.child('rooms').child(join_code).set({'room': room})
=======
        admin = request.form['admin']
        if test_strings(room, admin):
            return render_template('index.html', t="Empty Strings")
        db.child('rooms').child(join_code).set({'room': room, 'admin': admin})
>>>>>>> 4f0042f18a0390247e3891b8e38a4cdc74db995b
        return render_template('index.html', t=join_code)
    return render_template('index.html')


@app.route('/join', methods=['POST'])
def method_name():
    if request.method == 'POST':
        join = request.form['join']
        name = request.form['name']
        if test_strings(join, name):
            return render_template('index.html', t="Empty Strings")
        val = db.child('rooms').shallow().get().val()
        for i in val:
            if i == join:
<<<<<<< HEAD
                db.child('rooms').child(join).update({name: 'present'})
        return render_template('index.html', t=join)
    return render_template('index.html')

@app.route('/rooms/get', methods=['GET'])
def get_rooms():
    if request.method == 'GET':
        val = db.child('rooms').get().val()
        return render_template('index.html', t=val)
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_game():
=======
                db.child('rooms').child(join).child('students').set({name: True})
        return render_template('index.html', t=join)
    return render_template('index.html')


@app.route('/question/add', methods=['POST'])
def add_question():
    if request.method == 'POST':
        room = request.form['room']
        admin = request.form['admin']
        question = request.form['question']
        if test_strings(room, admin, question):
            return render_template('index.html', t="Empty Strings")
        val = 0
        if db.child('rooms').child(room).child('questions').shallow().get().val() != None:
            val = len(db.child('rooms').child(room).child('questions').shallow().get().val())
        db.child('rooms').child(room).child('questions').child(val).set({question: True})
        return render_template('index.html', t="Done")


@app.route('/question/get', methods=['POST'])
def get_question():
    if request.method == 'POST':
        room = request.form['room']
        index = request.form['index']
        if test_strings(room, index):
            return render_template('index.html', t="Empty Strings")
        return render_template('index.html', t=db.child('rooms').child(room).child('questions').child(index).get().val())

@app.route('/question/answer', methods=['POST'])
def ans_question():
    if request.method == 'POST':
        room = request.form['room']
        name = request.form['name']
        index = request.form['index']
        answer = request.form['answer']
        if test_strings(room, name, index, answer):
            return render_template('index.html', t="Empty Strings")

        db.child('rooms').child(room).child('questions').child(index).child('answers').child(name).set({'answer': answer})
        return render_template('index.html', t=answer)


@app.route('/rooms/get', methods=['GET'])
def get_rooms():
    if request.method == 'GET':
        val = db.child('rooms').get().val()
        return render_template('index.html', t=val)
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_viva():
>>>>>>> 4f0042f18a0390247e3891b8e38a4cdc74db995b
    if request.method == 'POST':
        return render_template('index.html', t="Entered")
        

if __name__ == '__main__': 
    app.run(debug=True)