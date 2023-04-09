#Syniah Peterson
#I used https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=844s to set up the exercise.
#I used https://www.youtube.com/watch?v=qbnqNWXf_tU and https://www.youtube.com/watch?v=r3Xmcdlx-Us to handle errors like missing fields.
#I used https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables to fix the database not being creating after following the video.
from flask import Flask, request, url_for, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students'
app.config['SECRET_KEY']="blue"

db = SQLAlchemy(app)

class registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(200), nullable=False)


def __init__(self, name, organization):
    self.name = name
    self.organization = organization


with app.app_context():
    db.create_all()


@app.route('/')
def registered():
    return render_template('registered.html', registration = registration.query.all())


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['organization']:
            flash('Please enter all the fields', 'error')
        else:
            student = registration(name = request.form['name'], organization = request.form['organization'])

            db.session.add(student)
            db.session.commit()
            return redirect(url_for('registered'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug = True)