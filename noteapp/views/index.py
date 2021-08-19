from flask import Blueprint, render_template
import glob

bp = Blueprint('index', __name__, template_folder='templates')

def fetchNotes():
    notes_text = []
    notes = glob.glob("noteapp/notes/*.note")
    
    for note in notes:
        with open(note) as note_file:
            notes_text.append(note_file.read())
        note_file.close()

    return notes_text


@bp.route('/')
def show():
    return render_template('index.html', notes=fetchNotes())
