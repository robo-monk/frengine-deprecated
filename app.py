from flask import Flask, jsonify, abort
import requests
import subprocess
from readability import Document
import os
import random
import string

# utility functions

def download(url, file_name):
  with open(file_name, "wb") as file:
    response = requests.get(url)
    file.write(response.content)

def rand_str():
  return ''.join([random.choice(string.ascii_letters + string.digits)
           for n in range(32)])

def link2html(link):
  response = requests.get(link)
  doc = Document(response.text)
  return doc.title(), doc.summary()

def pdf2html(url):
  file_name = rand_str()
  path_in = f'temp/{file_name}.pdf'
  download(url, path_in)
  path_out = f'temp/{file_name}.html'
  if url=='elonmusk':
    path_in = 'test.pdf'
  subprocess.call(f"pdf2htmlEX {path_in} {path_out}", shell=True)
  with open(path_out, 'r') as file:
    data = file.read().replace('\n', '')
    os.remove(path_in)
    os.remove(path_out)
  return (data)


app = Flask(__name__)
  

@app.route('/')
def ctrl_home():
  return "<h1> Frengine </h1> <p> Find out about this project on <a href='https://github.com/robo-monk/frengine'> GitHub </a> </p>"

# LINK 2 HTML
@app.route("/link2html/<path:link>")
def ctrl_link2html(link):
  title, body = link2html(link)
  return f"<h1>{title}</h1>" + body


@app.route("/api/link2html/<path:link>")
def ctrl_link2html_api(link):
  try:
    title, body = link2html(link)
    data = {
      "title" : title,
      "summary" : body
    }
    return jsonify(data)
  except:
    return abort(400)


# PDF 2 HTML
@app.route("/pdf2html/<path:url>")
def ctrl_pdf2html(url):
  return pdf2html(url)


@app.route("/api/pdf2html/<path:url>")
def convert_to_html_api(url):
  try:
    return jsonify(pdf2html(url))
  except:
    return abort(400)


#START APP
if __name__ == '__main__':
    app.run()

