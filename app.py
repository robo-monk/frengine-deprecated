from flask import Flask, jsonify, abort
import requests
from readability import Document

def extract(link):
  response = requests.get(link)
  doc = Document(response.text)
  return doc.title(), doc.summary()
  

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Frengine </h1> <p> Find out about this project on <a href='https://github.com/robo-monk/frengine'> GitHub </a> </p>"


@app.route("/<path:link>")
def preview(link):
  title, body = extract(link)
  return f"<h1>{title}</h1>" + body

@app.route("/api/<path:link>")
def api(link):
  try:
    title, body = extract(link)
    data = {
      "title" : title,
      "summary" : body
    }
    return jsonify(data)
  except:
    return abort(400)


if __name__ == '__main__':
    app.run(debug)

# @app.route('/')
# def home():
#   return 'README'



# if __name__ == '__main__':
#     app.run(debug=True)
