from flask import render_template, Blueprint

blueprint = Blueprint('pages', __name__)

@blueprint.route('/', methods=['GET'])
def index():
  return render_template('home.html')