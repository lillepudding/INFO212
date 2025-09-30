

movies = {}

class Movie:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        movies[name] = self
    
    def info_string(self):
        return self.name+","+self.image


def save_movies():
    with open("info212\movies.txt", "w") as m:
        for movie in movies:
            m.write(movies[movie].info_string()+"\n")


def load_movies():
    with open("info212\movies.txt") as m:
        movie_list = m.read().split("\n")[:-1]
        for movie in movie_list:
            features = movie.split(",")
            mov = Movie(features[0], features[1])


def add_movie(movie):
    movies[movie.name] = movie
    with open("info212\movies.txt", "a") as m:
        m.write(movie.info_string()+"\n")

def remove_movie(movie_name):
    load_movies()
    


def print_movies():
    for movie in movies:
        print(movies[movie].info_string())


load_movies()
print_movies()

"ok"