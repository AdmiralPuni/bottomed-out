from flask import *

from controllers.pages import blueprint as pages_blueprint
from controllers.api.uuu import blueprint as api_uuu

APP = Flask(__name__)

APP.register_blueprint(pages_blueprint)
APP.register_blueprint(api_uuu)

if __name__ == '__main__':
  APP.run(debug=True, host="127.0.0.1")
  
