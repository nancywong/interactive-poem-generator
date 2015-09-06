#!/usr/bin/env python
from flask import Flask, render_template, Response

# emulated camera
from flask import render_template
import ling

app = Flask(__name__)


# Views
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/poem')
def generate_line():
    # TODO replace dummy val for sentiment
    return ling.get_next_line(1.0)

if __name__ == '__main__':
    app.run(debug=True)
