from flask import Flask

app = Flask(__name__)
movies = {}

class Movie:
    def __init__(self, title, year, director, description, poster_path):
        self.title = title
        self.year = year
        self.director = director
        self.description = description
        self.poster_path = poster_path
    
    def info_string(self):
        return self.title+","+str(self.year)+","+self.director+","+self.description+","+self.poster_path


def save_movies():
    with open("info212/movies.txt", "w") as m:
        for movie in movies:
            m.write(movies[movie].info_string()+"\n")


def load_movies():
    with open("info212/movies.txt") as mo:
        movie_list = mo.read().split("\n")[:-1]
        print(movie_list)
        for movie in movie_list:
            features = movie.split(",")
            mov = Movie(features[0],features[1],features[2],features[3],features[4])
            movies[mov.title] = mov


def add_movie(movie):
    movies[movie.title] = movie
    with open("info212/movies.txt", "a") as m:
        m.write(movie.info_string()+"\n")

def remove_movie(movie_name):
    load_movies()
    


def print_movies():
    for movie in movies:
        print(movies[movie].info_string())

load_movies()
print(movies)
print(movies)
save_movies()


@app.route("/info212/Filmside")
def test(name):
    return "test"

"ok"
"ja"

if __name__ == '__main__':
   app.run()