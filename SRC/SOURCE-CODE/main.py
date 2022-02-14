import utils
import mysql.connector

CONNECTOR = mysql.connector.connect(
    host='127.0.0.1',
    port=3305,
    user='DbMysql36',
    password='DbMysql36',
    database='DbMysql36'
)
# print(CONNECTOR)
# mycursor = CONNECTOR.cursor()
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)
# mycursor.close()

while (True):
    what_to_ask = """
    Welcome to M-Investments! 
    The best app for your next investment on show bizz.
    By the next quetions we will help you, by our information, to get the best decision is where to put your money.
    So.... 
    What would you like to know today?
    1 - I want to know how comman is the word X in movie titles (FULL TEXT)
    2 - I want to know what is the average profit for X-genere movies.
    3 - I want to know if there is more females than males in X-movie's cast... Is he feminist movie?
    4 - Which of two given actors hava the higher average rating... 
    5 - I want to know what is the AVERAGE run time in movies from the most profitable genrereleased at X-year.
    6 - Show the yearly change in profit for a X year for a Y genre
    7 - I want to know who is the most profitable actor that playes in at least X movies of the Y genre.

    """
    navigate = input(what_to_ask)

    if navigate == '1':
        pt = input("\nWhich word?")
        if pt is None:
            raise ValueError("Must be provided!")
        utils.query_1(CONNECTOR, pt)
        break
    elif navigate == '2':
        pt = input("\nWhich genere?")
        if pt is None:
            raise ValueError("Must be provided!")
        utils.query_2(CONNECTOR, pt)
        break
    elif navigate == '3':
        pt = input("\nWhich movie title?")
        if pt is None:
            raise ValueError("Must be provided!")
        utils.query_3(
            CONNECTOR, pt)
        break
    elif navigate == '4':
        act1 = input("\nWhich actor1?")
        act2 = input("\nWhich actor2?")
        if act1 is None or act2 is None:
            raise ValueError("Must be provided!")
        utils.query_4(
            CONNECTOR, act1, act2)
        break
    elif navigate == '5':
        pt = input("\nWhich year?")
        if pt is None:
            raise ValueError("Must be provided!")
        utils.query_5(
            CONNECTOR, pt)
        break
    elif navigate == '6':
        user_year = input("\nWhich year?")
        user_genre = input("\nWhich genre?")
        if user_year is None or user_genre is None:
            raise ValueError("Must be provided!")
        utils.query_6(
            CONNECTOR, user_year, user_genre)
        break
    elif navigate == '7':
        user_genre = input("\nWhich genre?")
        user_num = input("\nHow many movies?")
        if user_genre is None or user_num is None:
            raise ValueError("Must be provided!")
        utils.query_7(
            CONNECTOR, user_genre, user_num)
        break


CONNECTOR.close()
