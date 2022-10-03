from flask import Flask, redirect, render_template, request, session, Response

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  return render_template('index.html')

@app.route("/works", methods=['GET'])
def works():
  return render_template('works.html')

@app.route("/collection", methods=['GET'])
def collection():
  return render_template('collection.html')