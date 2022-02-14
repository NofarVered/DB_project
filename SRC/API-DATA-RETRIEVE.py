import pandas as pd
import mysql
import mysql.connector
from imdb import IMDb
# tmdbv3api documentation- https://github.com/AnthonyBloomer/tmdbv3api
from tmdbv3api import TMDb, Genre, Movie, Person, Search

CONNECTOR = mysql.connector.connect(
    host='127.0.0.1',
    port=3305,
    user='DbMysql36',
    password='DbMysql36',
    database='DbMysql36'
)
mycursor = CONNECTOR.cursor()

MAX_SIZE = 10

INSERT_INTO_ACTORS = """INSERT INTO Actors (imdb_id, name, sex)
                        VALUES(%s,%s,%s)"""

INSERT_INTO_GENRES = """INSERT INTO Genres VALUES (%s, %s)"""

# Like in the documentation I gave in the link above
tmdb_API_KEY = "5827703e0b9f7a1f8b21b2928c293f5f"
#tmdb_Read_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ODI3NzAzZTBiOWY3YTFmOGIyMWIyOTI4YzI5M2Y1ZiIsInN1YiI6IjYxYzVlYmE4ZWNhZWY1MDA0MmEyOWJlYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eVet_jIYmyE6rIf6_RU_Wg77i7daZChQTQr3zLuFhAg"
tmdb = TMDb()
tmdb.api_key = tmdb_API_KEY


def convert_to_null(val):
    '''If the value is "None", return string "NULL" for database, or returns the value as is'''
    if val == 'None' or val == None or val == "":
        return "NULL"
    return val

# In some places in the file, I use json.loads, but I don't know if this is necessary


def load_actors(credits, id):
    per = Person()
    # in tmdb, sex is 0,1,2. so I used this list in a way that 0,1,2 are the indexes of the correct values (I did it as an enum)
    sex_convert = ['Other', 'Female', 'Male']
    # Same as sex_convert, I tried to make sure the "true" value from the api will be converted to our tinyiny
    FalseOrTrue = {'True': 1, 'False': 0}
    actor_count = 0  # In the Person part of the API, there are directors and writers as well. So if we want N actors in our db, we need to count the actors like that
    i = 1
    per = Person()
    search = Search()
    cast = credits['cast']
    for actor in cast:
        mycursor.execute(INSERT_INTO_ACTORS, [
                         actor['id'], actor['name'], sex_convert[actor['gender']]])
        actor_count += 1
        CONNECTOR.commit()
    mycursor.close()


def load_tmdb_movies():
    query = INSERT_INTO_MOVIES = """ INSERT IGNORE INTO Movies (imdb_id, title, rating, run_time, release_date, profit)
                            VALUES (%s,%s,%s,%s,%s,%s)"""
    movie = Movie()
    current_number_movies = 0
    i = 1
    for page in range(1, 120):
        popular = movie.popular(page)
        for p in popular:
            while current_number_movies < MAX_SIZE:
                try:
                    imdb = IMDb()
                    curr_movie = p.title
                    imdb_movie = imdb.search_movie(curr_movie)[0]
                    id_movie = imdb_movie.getID()
                except:
                    i += 1
                    continue
                i += 1
                data = [
                    int(curr_movie.id),
                    curr_movie.title,
                    movie.user_rating,
                    curr_movie.run_time,
                    curr_movie.release_date,
                    curr_movie.revenue
                ]
                mycursor.execute(query, data)
                CONNECTOR.commit()
    mycursor.close()


def load_genres():
    genre = Genre()
    for g in genre.movie_list():
        mycursor.execute(INSERT_INTO_GENRES, [g.id, g.name])
        CONNECTOR.commit()
    mycursor.close()


def load_movie_genres(movie_details):
    INSERT_INTO_MOVIE_GENRES = "INSERT IGNORE INTO Movie_genres (movie_id, genre_id) VALUES (%s,%s)"
    genres = movie_details.genres
    for g in genres:
        mycursor.execute(INSERT_INTO_MOVIE_GENRES, [
                         movie_details.imdb_id, g.id])
        CONNECTOR.commit()
    mycursor.close()


def parseImdbId(movie_id):
    return movie_id[2:]


def load_movie_actors(movie_id, cast):
    INSERT_INTO_MOVIE_ACTORS = "INSERT IGNORE INTO Movie_actors (movie_id, actor_id) VALUES (%s,%s)"
    for actor in cast:
        mycursor.execute(INSERT_INTO_MOVIE_ACTORS, [movie_id, actor['id']])
        CONNECTOR.commit()


# main
print("Beginning insertion")
# load_genres()
load_tmdb_movies()
print("Success!")
mycursor.close()
CONNECTOR.close()
