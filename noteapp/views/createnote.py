from flask import Blueprint, render_template, request, redirect
import random
import string

bp = Blueprint("createnote", __name__, template_folder="templates")


def randomString():
    length = 16
    random_string = ""
    alphabet = string.ascii_lowercase + string.digits

    for i in range(0, length):
        random_string += alphabet[random.randint(0,len(alphabet) - 1)]
    
    return random_string



@bp.route('/createnote', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        if request.form.get("createnote"):
            text = request.form.get("notetext")
        
            with open("noteapp/notes/{}.note".format(randomString()), "w+") \
                as note_file:
                    note_file.write(text)
            note_file.close()

            return redirect("/")
            

    return render_template('createnote.html')
