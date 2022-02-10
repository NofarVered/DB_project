import mysql.connector as connector  # Kathy's library
import pandas as pd
import pymysql as mysql
import omdb  # The db that wasn't used in our reference's code
import tmdbv3api  # tmdbv3api documentation- https://github.com/AnthonyBloomer/tmdbv3api
# Just attempts of mine with several libraries
import omdbapi
import requests
import json
import time
import zlib
import urllib
from imdb import IMDb
API_URL = "http://www.omdbapi.com"
API_KEY = "dcf700b1"
REQUEST_URL = API_URL+"?apikey="+API_KEY+"&"

MAX_SIZE = 30000


INSERT_INTO_ACTORS = """INSERT INTO Actors
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

INSERT_INTO_MOVIES = """ INSERT INTO Movies (id, imdb_id, title, runtime, popularity, poster_path, release_date, boxOffice_dollars)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

INSERT_INTO_GENRES = """INSERT INTO Genres VALUES (%s, %s)"""

INSERT_INTO_COMPANIES = """INSERT INTO Companies (company_id, name, description, headquarters, origin_country, homepage, logo_path)
                                      VALUES (%s, %s, %s, %s, %s, %s, %s)"""


user_pswd_dbname = 'DbMysql36'
#import os
#os.system("ssh -fN -L 3307:nova.cs.tau.ac.il:3306 itaizemah@nova.cs.tau.ac.il")
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

def load_tmdb_actors():
   per = tmdbv3api.Person()
   # in tmdb, sex is 0,1,2. so I used this list in a way that 0,1,2 are the indexes of the correct values (I did it as an enum)
   sex_convert = ['Other', 'Female', 'Male']
   # Same as sex_convert, I tried to make sure the "true" value from the api will be converted to our tinyiny
   FalseOrTrue = {'True': 1, 'False': 0}
   actor_count = 0  # In the Person part of the API, there are directors and writers as well. So if we want N actors in our db, we need to count the actors like that
   i = 0
   while actor_count < MAX_SIZE:
       # converted the result to json for an easier update to our db
       p = json.loads(per.details(i))
       i += 1
       if p['known_for_department'] == 'acting':
           actor_count += 1
           mycursor.execute(INSERT_INTO_ACTORS, p['id'], p['name'], sex_convert[p['gender']], p['birthday'], convert_to_null(p['deathday']), convert_to_null(p['biography']), float(
               p['popularity']),  p['imdb_id'], FalseOrTrue[p['adult']], convert_to_null(p['homepage']),  convert_to_null(p['profile_path']), convert_to_null(p['place_of_birth']))


def load_tmdb_popular_movies():
    movie = tmdbv3api.Movie()
    popular = movie.popular()
    for i in range(MAX_SIZE):
        try:
            p = json.loads(popular.details(i))
        except:
            break
        mycursor.execute(INSERT_INTO_MOVIES, p['id'], p['imdb_id'], p['title'], p['runtime'], p['popularity'], convert_to_null(
            p['poster_path']), p['release_date'], p['revenue'])
        mydb.commit()


def load_genres(genre):
    genre = tmdbv3api.Genre()
    for g in genre.movie_list():
        mycursor.execute(INSERT_INTO_GENRES, int(g["id"]), g["name"])
        mydb.commit()


def load_companies():
    from tmdbv3api import Company
    company = Company()
    for i in range(MAX_SIZE):
        try:
            details = company.details(i)
        except:
            break
        params = [details.id, details.name, details.description, details.headquarters, details.origin_country, details.homepage, details.logo_path]
        mycursor.execute(INSERT_INTO_COMPANIES, params )
        mydb.commit()

def load_movie_companies():
    load_connecting_table="""INSERT INTO Movie_companies (movie_id, company_id)
                            VALUES (%s, %s)"""
    from tmdbv3api import Movie
    popular_movies= Movie.popular()
    for i in range(MAX_SIZE):
        try:
             dets= popular_movies.details(i)
        except:
            break
        comp= json.loads(dets.production_companies)
        for c in comp:
            mycursor.execute(load_connecting_table, i, c["id"])
            mydb.commit()

def load_movie_actors():
    #We need to complete this. What I think we need to do is try to load these connections from the imdb csvs or the imdb APIs Einav used
    return 0





'''
Nofar- ignore this part


#This is a draft of loading the data from a local csv file- gotten from  https://www.imdb.com/interfaces/
#Choosing the 30,000 youngest actors from the IMDB name database
file_loc= '/Users/itaizemah/Desktop/movie_names.csv'
name_df = pd.read_csv(file_loc)
name_df.sort_values(by='birthYear', axis=0)
name_df = name_df.head(30000)
names= name_df.loc[:,'primaryName']
for i,name in enumerate(names):
    if 'actor' in name_df.at[i,'birthYear'] or 'actress' in name_df.at[i,'birthYear']:
        actor= Actor()

#Getting the 10,000 latest movies from the IMDB title database
title_df = pd.read_csv('/Users/itaizemah/Desktop/movie_titles.csv')
title_df.sort_values(by='startYear', axis=0)
title_df = title_df.head(10000)




titles= title_df[:,'primaryTitle']
for i, title in enumerate(titles):
    omsb_json= json.loads(omdb.title(title))


'''
if __name__ == "__main__":
  
    #incomplete
    load_companies()
    load_tmdb_actors()
    load_genres()
    mycursor.close()
    mydb.close()

