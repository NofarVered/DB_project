import pandas as pd
import pymysql as mysql
import mysql.connector
import imdb
import tmdbv3api  # tmdbv3api documentation- https://github.com/AnthonyBloomer/tmdbv3api


ia = imdb.Cinemagoer()

MAX_SIZE = 8

INSERT_INTO_ACTORS = """INSERT INTO Actors (imdb_id, name, sex, popularity, adult)
                        VALUES(%s,%s,%s,%s,%s)"""

INSERT_INTO_MOVIES = """ INSERT IGNORE INTO Movies (imdb_id, title, rating, run_time,  release_date, profit)
                            VALUES (%s,%s,%s,%s,%s,%s)"""

INSERT_INTO_GENRES = """INSERT INTO Genres VALUES (%s, %s)"""

# INSERT_INTO_COMPANIES = """INSERT INTO Companies (company_id, name, description, headquarters, origin_country, homepage, logo_path)
# VALUES (%s, %s, %s, %s, %s, %s, %s)"""

# Like in the documentation I gave in the link above
tmdb_API_KEY = "5827703e0b9f7a1f8b21b2928c293f5f"
#tmdb_Read_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ODI3NzAzZTBiOWY3YTFmOGIyMWIyOTI4YzI5M2Y1ZiIsInN1YiI6IjYxYzVlYmE4ZWNhZWY1MDA0MmEyOWJlYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eVet_jIYmyE6rIf6_RU_Wg77i7daZChQTQr3zLuFhAg"
tmdb = tmdbv3api.TMDb()
tmdb.api_key = tmdb_API_KEY


def convert_to_null(val):
    '''If the value is "None", return string "NULL" for database, or returns the value as is'''
    if val == 'None' or val == None or val == "":
        return "NULL"
    return val

# In some places in the file, I use json.loads, but I don't know if this is necessary


def load_actors(credits, id):
    from tmdbv3api import Person, Search
    mycursor = CONNECTOR.cursor()
    per = tmdbv3api.Person()
    # in tmdb, sex is 0,1,2. so I used this list in a way that 0,1,2 are the indexes of the correct values (I did it as an enum)
    sex_convert = ['Other', 'Female', 'Male']
    # Same as sex_convert, I tried to make sure the "true" value from the api will be converted to our tinyiny
    FalseOrTrue = {'True': 1, 'False': 0}
    actor_count = 0  # In the Person part of the API, there are directors and writers as well. So if we want N actors in our db, we need to count the actors like that
    i = 1
    per = Person()
    search = Search()
    cast= credits['cast']
    for actor in cast:
        
        
        mycursor.execute(INSERT_INTO_ACTORS, [actor['id'], actor['name'], sex_convert[actor['gender']],  float(actor['popularity']), actor['adult']])
        actor_count += 1
        CONNECTOR.commit()
    mycursor.close()


def load_tmdb_movies():
    movie = tmdbv3api.Movie()
    mycursor = CONNECTOR.cursor()
    movie_count = 0
    i = 1
    while movie_count < MAX_SIZE:
        print(i)
        try:
            p = movie.details(i)
        except:
            print("skipping id ", i)
            i += 1
            continue
        i += 1
        try:
            mov = ia.get_movie(parseImdbId(p.imdb_id))
        except:
            print("Movie not found on imdb")

        mycursor.execute(INSERT_INTO_MOVIES, [parseImdbId(
            p.imdb_id), p.title, mov['user rating'], p.runtime, p.release_date, p.revenue])
        CONNECTOR.commit()
        try:
            #print("loading actors ", i)
            load_actors(movie.credits(i),i)
            
        except Exception as e:
            print(e)
            print("no actors on movie", p.title)
        try:
            load_movie_actors(p.imdb_id, movie.credits(i)['cast'] )
        except Exception as e:
            print(e)
        load_movie_genres(p)
        movie_count += 1
    mycursor.close()


def load_genres():
    genre = tmdbv3api.Genre()
    mycursor = CONNECTOR.cursor()
    for g in genre.movie_list():
        mycursor.execute(INSERT_INTO_GENRES, [g.id, g.name])
        CONNECTOR.commit()
    mycursor.close()


def load_movie_genres(movie_details):
    mycursor = CONNECTOR.cursor()
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
    mycursor = CONNECTOR.cursor()
    INSERT_INTO_MOVIE_ACTORS = "INSERT IGNORE INTO Movie_actors (movie_id, actor_id) VALUES (%s,%s)"
    for actor in cast:
        mycursor.execute(INSERT_INTO_MOVIE_ACTORS, [movie_id, actor['id']])
        CONNECTOR.commit()
    mycursor.close()


if __name__ == "__main__":
    CONNECTOR = mysql.connector.connect(
        host='127.0.0.1',
        port=3305,
        user='DbMysql36',
        password='DbMysql36',
        database='DbMysql36'
    )
    print("Beginning insertion")
    # load_genres()
    load_tmdb_movies()
    print("Success!")
    CONNECTOR.close()
