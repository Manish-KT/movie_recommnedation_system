from flask import Flask, render_template, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from edit import Signup, MovieTitle
from movie_api import Info
import json
from sqlalchemy.exc import IntegrityError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_recommendation_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

with app.app_context():
    db = SQLAlchemy(app)
    db.create_all()


class MovieData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=True)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        rating = request.form.get('new_rating')
        review = request.form.get('review')
        id_ = request.args.get("movie_id")
        if len(review) != 0:
            review = str(review)
            db.session.execute(text(f"update movie_data set review='{review}' where id={id_}"))
        elif rating is not None:
            db.session.execute(text(f"update movie_data set rating={rating} where id={id_}"))
        db.session.commit()

    elif request.method == "GET":
        try:
            movie = request.args.get("data")
            json_data_str = json.dumps(movie)
            json_data = eval(json.loads(json_data_str))
            print(json_data["titleText"]["text"])
            new_movie = MovieData(
                title=json_data["titleText"]["text"],
                year=json_data["releaseYear"]["year"],
                description="",
                rating=10,
                ranking=1,
                review="",
                img_url=json_data['primaryImage']['url']
            )
            db.session.add(new_movie)
            db.session.commit()
        except:
            pass
    movies = db.session.execute(text("select * from movie_data order by rating asc")).all()
    # movies = db.session.query(MovieData).all()
    return render_template("index.html", movies=movies)


@app.route("/update/<m_id>", methods=["GET", "POST"])
def update_movie(m_id):
    delete = request.form.get("delete")
    if bool(delete):
        print("i am here")
        db.session.execute(text(f"delete from movie_data where id={m_id}"))
        db.session.commit()
        return render_template(url_for("home"))
    form = Signup()
    movie = db.session.query(MovieData).get(m_id)
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    m_id = request.args.get("m_id")
    db.session.execute(text(f"delete from movie_data where id={m_id}"))
    db.session.commit()
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieTitle()
    if request.method == "GET":
        return render_template("add.html", form=form, show=False)
    elif request.method == "POST":
        title = request.form.get("title")
        movie_ = Info(title)
        return render_template("add.html", movie_list=movie_["results"], show=True)
    movies = db.session.query(MovieData).all()
    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
