import random
import string
import time

def code():
    n=5
    res=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=n))
    return res

<<<<<<< HEAD
print(code())

@app.route('/join', methods=['POST'])
def method_name():
    if request.method == 'POST':
        join = request.form['join']
        name = request.form['name']
        val = db.child('rooms').get().val()
        for i in val:
            if i == join:
                db.child('rooms').child(join).update({name: 'present'})
        return render_template('index.html', c=join)
    return render_template('index.html')
=======
def time_lapse():
    start = time.time()
    while True:
        end = time.time()
        if (end - start)>3:
        #call a function to make the answer time time-out

>>>>>>> a1e76881cc4cedfab2042ab7e9b89418313ced8f
