from flask import request, Blueprint
import json
import time

blueprint = Blueprint('api_payments', __name__)

def byte_to_emoji(value):
  buffer = ""

  if value == 0:
    buffer += "❤️"

  while value > 0:
    if 200 <= value <= 255:
      emoji, subtract = "🫂", 200
    elif 50 <= value <= 199:
      emoji, subtract = "💖", 50
    elif 10 <= value <= 49:
      emoji, subtract = "✨", 10
    elif 5 <= value <= 9:
      emoji, subtract = "🥺", 5
    elif 1 <= value <= 4:
      emoji, subtract = ",", 1
    else:
      break

    buffer += emoji
    value -= subtract

  buffer += "👉👈"
  return buffer

def reply(message, data=None):
  return json.dumps({
    'message': message,
    'data': data,
    'timestamp': time.time()
  })

@blueprint.route('/api/bottomize', methods=['GET', 'POST'])
def all():
  text = request.form['text']

  utf8_nums = [num for num in text.encode('utf-8')]

  newtext = ""

  for num in utf8_nums:
    newtext += byte_to_emoji(num)

  data = newtext

  return reply('Bottomized!', data=data), 200