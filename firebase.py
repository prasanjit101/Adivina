from Pyrebase import pyrebase

config = {

    "apiKey": "AIzaSyAAtBuPe4aVoa_vm2bV9WVcfI7Pa4SakR0",
    "authDomain": "adivina-87126.firebaseapp.com",
    "databaseURL": "https://adivina-87126-default-rtdb.firebaseio.com",
    "projectId": "adivina-87126",
    "storageBucket": "adivina-87126.appspot.com",
    "messagingSenderId": "321353211600",
    "appId": "1:321353211600:web:282a6da4fb4e4a8ea088d5",
    "measurementId": "G-3QC6ZEXYNX"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.child("questions").push("questions", { "name": "Prasanjit" })