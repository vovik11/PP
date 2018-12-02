import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "cardatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class NewCar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autoName = db.Column(db.String(120), index=True, unique=True)
    autoModel = db.Column(db.String(120), index=True, unique=True)
    engine = db.Column(db.String(64), index=True, unique=False)
    passengers = db.Column(db.String(64), index=True, unique=False)

    def get_id(self):
        return str(self.id)


@app.route('/')
def welcome_page():
    return render_template('welcome.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('addAuto.html')


@app.route('/showList', methods=['GET', 'POST'])
def showlist():
    if request.form:
        car = NewCar(autoName=request.form.get("name"), autoModel=request.form.get("model"),
                     engine=request.form.get("engine"), passengers=request.form.get("passengers"))
        db.session.add(car)
        db.session.commit()
    cars = NewCar.query.all()
    return render_template("showList.html", cars=cars)


@app.route('/booking')
def booking():
    cars = NewCar.query.all()
    return render_template("booking.html", cars=cars)


@app.route('/return')
def done():
    return render_template('return.html')


if __name__ == '__main__':
    app.run()
