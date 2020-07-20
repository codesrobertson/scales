# !/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip(python 3.8)

from flask import Flask, render_template, url_for, request
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import weigh 


app = Flask(__name__, static_url_path="", template_folder="templates")

@app.route("/")
def index(): 
  return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
  return f"hello {request.form.get('name')}"

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/documentation")
def documentation():
  return render_template("documentation.html")

@app.route("/howitworks")
def process():
  return render_template("howitworks.html")

@app.route("/weigh", methods=["POST"])
def submission():
  weigh.Weigh().return_analysis(request.form.get('url'))
  return render_template("weigh.html")

if __name__ == "__main__":
  app.run(debug=True)
