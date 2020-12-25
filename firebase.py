from Pyrebase import pyrebase
from flask import *
from functions import code, timerFunction, test_strings, assign_codes_to_roll_no
import random
import os


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

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # x = 5
    # val = timerFunction(x)
    # db.child("questions").set(questions)
    return render_template('index.html', t="Welcome to Adivina")

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
        room = request.form['start']
        admin = request.form['end']
        start = request.form['start']
        end = request.form['end']
        val = assign_codes_to_roll_no(int(start), int(end))
        if test_strings(room, admin, val):
            return render_template('index.html', t="Empty Strings")
        db.child('rooms').child(join_code).set({'room': room, 'admin': admin})
        db.child('rooms').child(join_code).child("students").set(val)
        return render_template('index.html', t=join_code)
    return render_template('index.html')


@app.route('/student/join', methods=['POST'])
def method_name():
    if request.method == 'POST':
        join = request.form['join']
        name = request.form['name']
        if test_strings(join, name):
            return render_template('index.html', t="Empty Strings")
        val = db.child('rooms').shallow().get().val()
        for i in val:
            if i == join:
                if db.child('rooms').child(join).child('students').get().val() != None:
                    student = db.child('rooms').child(join).child('students').get(name).val()
                    if student == name:
                        return render_template('index.html', t=student)
    return render_template('index.html')


@app.route('/question/add', methods=['POST'])
def add_question():
    if request.method == 'POST':
        room = request.form['room']
        admin = request.form['admin']
        question = request.form['question']
        time = request.form['time']
        if test_strings(room, admin, question, time):
            return render_template('index.html', t="Empty Strings")
        val = 0
        if db.child('rooms').child(room).child('questions').shallow().get().val() != None:
            val = len(db.child('rooms').child(room).child('questions').shallow().get().val())
        db.child('rooms').child(room).child('questions').child(val).set({'question': question, 'time': time})
        return render_template('index.html', t="Done")



@app.route('/question/get', methods=['POST'])
def get_question():
    if request.method == 'POST':
        room = request.form['room']
        if test_strings(room):
            return render_template('index.html', t="Empty Strings")
        val = 0
        if db.child('rooms').child(room).child('questions').shallow().get().val() != None:
            val = len(db.child('rooms').child(room).child('questions').shallow().get().val())
        if(val == 0):
            return render_template('index.html', t="No Question")
        que = "No Question"
        
        return render_template('index.html', t=db.child('rooms').child(room).child('questions').child(val - 1).get().val())


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
    if request.method == 'POST':
        return render_template('index.html', t="Entered")
        

if __name__ == '__main__': 
    app.run(debug=True)