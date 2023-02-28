# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text
#
# app_d = Flask(__name__)
# app_d.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_recommendation_data.db"
# app_d.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app_d)
#
#
# class MovieData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, unique=True, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     description = db.Column(db.String, nullable=True)
#     rating = db.Column(db.Float, nullable=False)
#     ranking = db.Column(db.Integer, unique=True, nullable=False)
#     review = db.Column(db.String, nullable=True)
#     img_url = db.Column(db.String, nullable=False)
#
#
# class Movie:
#
#     def __init__(self):
#         self.movie_data = ()
#         self.database = db
#
#     def add_movie(self, movie_info):
#         self.database.session.add(movie_info)
#         self.database.session.commit()
#
#     def update_movie(self, id_):
#         self.database.session.execute(text(f"select * from movie_data where id={id_}"))
#         self.database.session.commit()
#
#     def delete_movie(self, id_):
#         self.database.session.execute(text(f"delete from movie_data where id={id_}"))
#         self.database.session.commit()
#
#
# # new_movie = MovieData(
# #     title="Phone Booth",
# #     year=2002,
# #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
# #                 "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to "
# #                 "a jaw-dropping climax.",
# #     rating=7.3,
# #     ranking=11,
# #     review="My favourite character was the caller.",
# #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# # )
#
#
# with app_d.app_context():
#     db.create_all()
#
#
