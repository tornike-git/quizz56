from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class tvshows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f"title: {self.title}, year: {self.year}, rating: {self.rating}"


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form['name']
        session['name'] = name

        password = request.form['pass']
        session['pass'] = password

        if name == '' or password == '':
            flash("შეავსეთ ყველა ველი")
        else:
            return redirect(url_for("index"))
    return render_template("user.html")


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        t = request.form['title']
        y = request.form['year']
        r = request.form['rating']

        if t == '' or y == '' or r == '':
            flash("შეავსეთ ყველა ველი")

        elif not y.isnumeric() or r.isnumeric():
            flash("შეიტანეთ რიცხვები")
        else:
            s1 = tvshows(title=t, year=y, rating=r)
            db.session.add(s1)
            db.session.commit()
            flash("დამატებულია")

    return render_template("index.html")


@app.route('/info')
def info():
    all_shows = tvshows.query.all()
    return  render_template("info.html", all_shows=all_shows)


@app.route('/out')
def out():
    session.pop('name', None)
    return render_template("base.html")


if __name__ in '__main__':
    app.run(debug=True)
