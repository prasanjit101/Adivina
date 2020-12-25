from Pyrebase import pyrebase
from flask import *
from functions import code, timerFunction, test_strings, assign_codes_to_roll_no
import random
import requests
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
 

@app.route('/', methods=['GET', 'POST'])
def generate_code():
    if request.method == 'POST':

        room = code()
        name = request.form.get('name')
        admin = request.form.get('admin')
        start = request.form.get('start')
        end = request.form.get('end')

        students = assign_codes_to_roll_no(int(start), int(end))

        if test_strings(name, admin, start, end):
            return render_template('home.html', t="Empty Strings")

        db.child('rooms').child(room).set({'admin': admin, 'name': name})
        db.child('rooms').child(room).child('students').set(students)

        return render_template('home.html', info="Room Created", room=room, admin=admin, name=name)
    return render_template('home.html', info="Welcome to Adivina")


@app.route('/admin', methods=['POST'])
def admin_join():
    if request.method == 'POST':
        room = request.form.get('room')
        admin = request.form.get('admin')
        if test_strings(room, admin):
            return render_template('home.html')
        val = db.child('rooms').shallow().get().val()
        for i in val:
            if i == room:
                details = db.child('rooms').child(room).get().val()
                if details['admin'] == admin:
                    return render_template('admin.html', name=details['name'], room=room)         
        return render_template('home.html', info="Unexpected Error")


@app.route('/student', methods=['POST'])
def student_join():
    if request.method == 'POST':
        room = request.form.get('room')
        code = request.form.get('code')
        name = request.form.get('name')
        if test_strings(room, name):
            return render_template('home.html', t="Empty Strings")

        val = db.child('rooms').shallow().get().val()
        for i in val:
            if i == room:
                if db.child('rooms').child(room).child('students').get().val() != None:
                    student = db.child('rooms').child(room).child('students').get().val()
                    if len(student) > int(name) and student[int(name)] == code:
                        room_name = db.child('rooms').child(room).get().val()['name']
                        return render_template('student.html', name=room_name, room=room, student=name)
    return render_template('home.html', info="Unexpected Error")



@app.route('/admin/<room>/<name>/add', methods=['POST'])
def add_question(room, name):
    if request.method == 'POST':
        question = request.form.get('question')
        name = request.form.get('name')
        if test_strings(room, question):
            return render_template('admin.html', info="Empty Strings")
        question_number = 0
        if db.child('rooms').child(room).child('questions').shallow().get().val() != None:
            question_number = len(db.child('rooms').child(room).child('questions').shallow().get().val())
        db.child('rooms').child(room).child('questions').child(question_number).set({'question': question})
        return render_template('admin.html', info="Uploaded", room=room, name=name)


@app.route('/<room>/<student>/<name>/answer', methods=['POST'])
def ans_question(room, student, name):
    if request.method == 'POST':
        answer = request.form['answer']
        if test_strings(answer):
            return render_template('student.html', t="Empty Strings")
        if db.child('rooms').child(room).child('questions').shallow().get().val() != None:
            question_number = len(db.child('rooms').child(room).child('questions').shallow().get().val())
            question = db.child('rooms').child(room).child('questions').child(question_number - 1).get().val()['question']
            db.child('rooms').child(room).child('questions').child(question_number - 1).child('answers').child(student).set({'answer': answer})
            return render_template('student.html', info="Uploaded", room=room, student=student, name=name, question=question)
        return render_template('student.html', info="Unexpected Error",room=room, name=name, student=student)
        

if __name__ == '__main__': 
    app.run(debug=True)