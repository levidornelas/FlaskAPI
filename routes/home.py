from flask import Blueprint
from flask import render_template

home_route = Blueprint('Home', __name__)

@home_route.route('/')
def home():
  return render_template('index.html')