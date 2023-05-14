from flask import Flask, render_template
import random

app = Flask(__name__)

# Generate some random data
def generate_data():
    data = []
    for i in range(30):
        data.append([i, random.randint(0, 100)])
    return data

@app.route('/')
def index():
    data = generate_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
