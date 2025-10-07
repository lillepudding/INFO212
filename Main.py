from flask import Flask, render_template
from pathlib import Path
from random import randint
import sqlite3

ROOT_DIR = Path(__file__).parent


app = Flask(__name__)


movie_dict = {}


class Movie:
    def __init__(self, title, year, director, description, genre, image):
        self.title = title
        self.year = year
        self.director = director
        self.description = description
        self.genre = genre
        self.image = image
    
    def info_string(self):
        return self.title+","+str(self.year)+","+self.director+","+self.description+","+self.genre+","+self.image


def save_movies():
    with open(ROOT_DIR/"static/movies.txt", "w") as m:
        for movie in movie_dict:
            m.write(movie_dict[movie].info_string()+"\n")


def load_movies():
    with open(ROOT_DIR/"static/movies.txt", "r") as mo:
        movie_list = mo.read().split("\n")[:-1]
        print(movie_list)
        for movie in movie_list:
            features = movie.split(",")
            mov = Movie(features[0],features[1],features[2],features[3],features[4],features[5])
            movie_dict[mov.title] = mov


def add_movie(movie):
    movie_dict[movie.title] = movie
    with open(ROOT_DIR/"static/movies.txt", "a") as m:
        m.write(movie.info_string()+"\n")

def remove_movie(movie_name):
    load_movies()
    


def print_movies():
    for movie in movie_dict:
        print(movie_dict[movie].info_string())

load_movies()
print(movie_dict)
print(movie_dict)
save_movies()


@app.route("/Filmside")
def test():
    return "<p>test</p>"

@app.route("/")
def Filmside():
    test = movie_dict["The last tomate"]
    movies = [movie_dict[x] for x in movie_dict]
    return render_template("FilmSide.html", test=test, movies=movies)

@app.route("/register")
def register():
    return render_template("Bruker.html")

@app.route("/<movie>")
def movie_frame(movie):
    return render_template("movie_frame.html",movie=movie_dict[movie],root=ROOT_DIR)

@app.route("/recommendation")
def recommendation():
    keys = list(movie_dict.keys())
    movie_num = randint(0, len(keys)-1)
    rec = movie_dict[keys[movie_num]]
    return render_template("movie_frame.html",movie=rec,root=ROOT_DIR)


if __name__ == '__main__':
   app.run()

'''
{% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
'''
#Brukes i filmside.html?