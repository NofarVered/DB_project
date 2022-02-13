
import pandas as pd
import pymysql as mysql
import imdb
import tmdbv3api  # tmdbv3api documentation- https://github.com/AnthonyBloomer/tmdbv3api


ia = imdb.Cinemagoer()

MAX_SIZE = 3000


INSERT_INTO_ACTORS = """INSERT INTO Actors (imdb_id, name, sex, birthday, deathday, popularity, adult,  place_of_birth )
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

INSERT_INTO_MOVIES = """ INSERT IGNORE INTO Movies (imdb_id, title, rating, run_time,  release_date, profit)
                            VALUES (%s,%s,%s,%s,%s,%s)"""

INSERT_INTO_GENRES = """INSERT INTO Genres VALUES (%s, %s)"""

#INSERT_INTO_COMPANIES = """INSERT INTO Companies (company_id, name, description, headquarters, origin_country, homepage, logo_path)
#VALUES (%s, %s, %s, %s, %s, %s, %s)"""


user_pswd_dbname = 'DbMysql36'

mydb = mysql.connect(
    host='127.0.0.1',
    port=3305,
    user=user_pswd_dbname,
    password=user_pswd_dbname,
    database=user_pswd_dbname
)

mycursor = mydb.cursor()


#Like in the documentation I gave in the link above
tmdb_API_KEY = "5827703e0b9f7a1f8b21b2928c293f5f"
#tmdb_Read_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ODI3NzAzZTBiOWY3YTFmOGIyMWIyOTI4YzI5M2Y1ZiIsInN1YiI6IjYxYzVlYmE4ZWNhZWY1MDA0MmEyOWJlYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eVet_jIYmyE6rIf6_RU_Wg77i7daZChQTQr3zLuFhAg"
tmdb = tmdbv3api.TMDb()
tmdb.api_key = tmdb_API_KEY


def convert_to_null(val):
    '''If the value is "None", return string "NULL" for database, or returns the value as is'''
    if val == 'None' or val == None or val == "":
        return "NULL"
    return val

#In some places in the file, I use json.loads, but I don't know if this is necessary


def load_actors(cast):
   per = tmdbv3api.Person()
   # in tmdb, sex is 0,1,2. so I used this list in a way that 0,1,2 are the indexes of the correct values (I did it as an enum)
   sex_convert = ['Other', 'Female', 'Male']
   # Same as sex_convert, I tried to make sure the "true" value from the api will be converted to our tinyiny
   FalseOrTrue = {'True': 1, 'False': 0}
   actor_count = 0  # In the Person part of the API, there are directors and writers as well. So if we want N actors in our db, we need to count the actors like that
   i = 1
   from tmdbv3api import Person, Search
   per= Person()
   search = Search()
   for actor in cast:
       # converted the result to json for an easier update to our db
       try:
           result= search.people({"query": actor})
           id= result['results']['id']
           p= per.details(id)
       except:
           i+=1
           continue
       i += 1
       if p.known_for_department == 'acting':
           try:
               person_id = ia.get_imdbID(p.name)
           except:
               #Handling the case where an actor exists in tmdb, but not in imdb
               continue
           actor_count += 1
           mycursor.execute(INSERT_INTO_ACTORS, [person_id, p.name, sex_convert[p.gender], p.birthday, convert_to_null(
               p.deathday), float(p.popularity), FalseOrTrue[p.adult],  convert_to_null(p.place_of_birth)])
           mydb.commit()


def load_tmdb_movies():
    movie = tmdbv3api.Movie()
    movie_count=0
    i=1
    while movie_count<MAX_SIZE:
        try:
            p = movie.details(i)
        except:
            i+=1
            continue
        i+=1
        try:
            mov = ia.get_movie(parseImdbId(p.imdb_id))
        except:
            continue
        
        mycursor.execute(INSERT_INTO_MOVIES, [parseImdbId(p.imdb_id), p.title, mov['user rating'], p.runtime, p.release_date, p.revenue])
        mydb.commit()
        try:
            load_actors(mov['cast'])
            load_movie_actors(p.imdb_id)
        except:
            pass
        load_movie_genres(p)
        movie_count+=1



def load_genres():
    genre = tmdbv3api.Genre()
    for g in genre.movie_list():
        mycursor.execute(INSERT_INTO_GENRES , [g.id, g.name])
        mydb.commit()


def load_movie_genres(movie_details):
    INSERT_INTO_MOVIE_GENRES = "INSERT IGNORE INTO Movie_genres (movie_id, genre_id) VALUES (%s,%s)"
    genres = movie_details.genres
    for g in genres:
        mycursor.execute(INSERT_INTO_MOVIE_GENRES, [movie_details.imdb_id, g.id])
        mydb.commit()


def parseImdbId(movie_id):
    return movie_id[2:]


def load_movie_actors(movie_id):
   INSERT_INTO_MOVIE_ACTORS = "INSERT IGNORE INTO Movie_actors (movie_id, actor_id) VALUES (%s,%s)"
   movie_id = parseImdbId(movie_id)
   # If this outputs an error, try with str()
   imdb_movie = ia.get_movie(movie_id)
   try:
       cast = imdb_movie['cast']
   except:
       print("Movie isn't in IMDb, conitnue to next one please")
   for actor in cast:
       actor_id = ia.get_imdbID(actor)
       mycursor.execute(INSERT_INTO_MOVIE_ACTORS, [movie_id, actor_id])
       mydb.commit()


if __name__ == "__main__":
    print("Beginning insertion")
    #load_genres()
    load_tmdb_movies()
    print("Success!")
    mycursor.close()
    mydb.close()
