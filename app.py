from flask import Flask, jsonify, abort
import requests
import subprocess
from readability import Document
import os
import random
import string


# functions

def download(url, file_name):
  with open(file_name, "wb") as file:
      response = requests.get(url)
      file.write(response.content)

def extract(link):
  response = requests.get(link)
  doc = Document(response.text)
  return doc.title(), doc.summary()

def rand_str():
  ''.join([random.choice(string.ascii_letters + string.digits)
           for n in range(32)])

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


@app.route("/api/pdf_to_html/<path:url>")
def convert_to_html(url):
  try:
    path_in = f'temp/{rand_str()}.pdf'
    download(url, path_in)
    path_out = f'temp/{rand_str()}.html'
    subprocess.call(f"pdf2htmlEX {path_in} {path_out}", shell=True)
    with open(path_out, 'r') as file:
      data = file.read().replace('\n', '')
    
    # os.remove(path_in)
    os.remove(path_out)
    return jsonify(data)
  except:
    return abort(400)

if __name__ == '__main__':
    app.run(debug=True)

