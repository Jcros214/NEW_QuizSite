from flask import Blueprint, jsonify, request
import json
import random

api = Blueprint('api', __name__)

with open("static/json/questions.json", "r") as f:
    questions = json.load(f)


def retrieve_flashcard(chapters):
    doexit = False

    while not doexit:
        q = random.choice(questions)
        if q["reference"][:q["reference"].find(':')] in chapters:
            doexit = True
    return q


@api.route('/api/next-flashcard', methods=['GET', 'POST'])
def get_next_flashcard():
    data = request.get_json()
    chapters = data['chapters']
    # retrieve flashcard data based on selected chapters
    flashcard = retrieve_flashcard(chapters)
    # return flashcard data as a JSON response
    return jsonify({'front': flashcard.get("question"), 'back': flashcard.get('answer') + '<br>' + flashcard.get('reference')})
