from Pyrebase import pyrebase
from flask import *

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

db.child("questions").set(questions)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'GET':
        questions = db.child("questions").get()
        return questions.val()
    return -1

if __name__ == '__main__':
    app.run(debug=True)