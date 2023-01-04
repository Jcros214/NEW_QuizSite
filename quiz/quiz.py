from flask import Blueprint, render_template

quiz = Blueprint('quiz', __name__)


@quiz.route('/quiz')
def tmp_quiz():
    return render_template('quiz.html')
