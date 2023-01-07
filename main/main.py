from flask import Blueprint, render_template
from  flask_login  import  current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/material')
def material():
    return render_template('material.html')

@main.route('/practice')
def practice():
    return render_template('practice.html')
