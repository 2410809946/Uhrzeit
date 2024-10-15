from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    now = datetime.now().strftime("%H:%M:%S")
    return jsonify(time=now)

@app.route('/date')
def get_date():
    today = datetime.now().strftime("%Y-%m-%d")
    return jsonify(date=today)

@app.route('/show_date')
def show_date():
    return render_template('date.html')

if __name__ == '__main__':
    app.run(debug=True)