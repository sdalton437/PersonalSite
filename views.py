from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def menu():
	return render_template("index.html")

@app.route('/NeighbourhoodMap')
def neighbourhoodMap():
	return render_template("NeighbourhoodMap/index.html")

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)