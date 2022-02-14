import imp
from utils import run_sql_file
import mysql.connector

CONNECTOR = mysql.connector.connect(
    host='127.0.0.1',
    port=3305,
    user='DbMysql36',
    password='DbMysql36',
    database='DbMysql36'
)
print(CONNECTOR)
mycursor = CONNECTOR.cursor()
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
mycursor.close()

while (True):
    what_to_ask = """
    Welcome to M-Investments! 
    The best app for your next investment on show bizz.
    By the next quetions we will help you, by our information, to get the best decision is where to put your money.
    So.... 
    What would you like to know today?
    1 - I want to know what is the total profit of all the movies X-actor played on.
    2 - I want to know what is the average profit for X-genere movies.
    3 - I want to know how many actors from X-gender, played in the top ten leading movie by profit.
    4 - I want to know what is the average rating that X-actor got for her\his movies.
    5 - I want to know what is the AVERAGE run time in movies released at X-year.
    6 - ITAI QUERIS
    7 - ITAI QUERIS
    """
    navigate = input(what_to_ask)

    if navigate == '1':
        pt = input("\nWhich actor?")
        if pt is None:
            raise ValueError("Must be provided!")
        run_sql_file(CONNECTOR, "sqls/full_text_1.sql", pt)
        break
    elif navigate == '2':
        pt = input("\nWhich genere?")
        if pt is None:
            raise ValueError("Must be provided!")
        run_sql_file(CONNECTOR, "sqls/avg_genre_X_profit_2.sql", pt)
        break
    elif navigate == '3':
        pt = input("\nWhich movie title?")
        if pt is None:
            raise ValueError("Must be provided!")
        run_sql_file(
            CONNECTOR, "sqls/For_given_movie_is_he_has_more_F.M_actors_3.sql", pt)
        break
    elif navigate == '4':
        pt = input("\nWhich actor?")
        if pt is None:
            raise ValueError("Must be provided!")
        run_sql_file(
            CONNECTOR, "sqls/What_is_the_average_rating_that_X_got_for_his_movies_4.sql", pt)
        break
    elif navigate == '5':
        pt = input("\nWhich year?")
        if pt is None:
            raise ValueError("Must be provided!")
        run_sql_file(
            CONNECTOR, "sqls/What_is_the_aver_run_time_in_movies_released_at_X_5.sql", pt)
        break
    elif navigate == '6':
        user_year = input("\nWhich year?")
        user_genre = input("\nWhich genre?")
        if user_year is None or user_genre is None:
            raise ValueError("Must be provided!")
        run_sql_file(
            CONNECTOR, "sqls/yearly_change_6.sql", user_year, user_genre)
        break
    elif navigate == '7':
        user_genre = input("\nWhich genre?")
        user_num = input("\nHow many times?")
        if user_genre is None or user_num is None:
            raise ValueError("Must be provided!")
        run_sql_file(
            CONNECTOR, "sqls/Actor_genre_X_frequency_7.sql", user_genre, user_num)
        break


CONNECTOR.close()
