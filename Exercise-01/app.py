#Syniah Peterson
#I used https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=844s to import Flask and set up the exercise
from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current= datetime.now()
    return render_template('index.html', current_day = current.strftime('%A, %B %d, %Y %H:%M:%S'))

if __name__ == "__main__":
    app.run(debug=True)