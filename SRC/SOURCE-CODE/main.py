# from queries-manager import
import pymysql

CONNECTOR = pymysql.connect(
    host='localhost',
    port=3305,
    user='DbMysql36',
    password='DbMysql36',
    database='DbMysql1536'
)


what_to_ask = """
Welcome to M-Investments! 
The best app for your next investment on show bizz.
By the next quetions we will help you, by our information, to get the best decision is where to put your money.
So.... 
What would you like to know today?
1 - I want to know what is the total profit of all the movies X-actor played on.
2 - I want to know what is the average profit for X-genere movies.
3 - I want to know how many actors from X-gender, played in the top ten leading movie by profit
4 - I want to know what is the average rating that X-actor got for her\his movies.
5 - I want to know what is the the most popular language at movies in the X-year.
6 - ITAI QUERIS
7 - ITAI QUERIS
"""

navigate = input(what_to_predict)

if navigate == '1':
    RatingPredictor(query)
elif navigate == '2':
    ActorsPredictor(query)
elif navigate == '3':
    SimilarityCalculator(query)
elif navigate == '4':
    LanguageCalculator(query)
elif navigate == '5':
    CastOriginalityCalculator(query)
elif navigate == '6':
    query_pop_view = "select * from top50_movies"
    query.execute_query(query_pop_view)
    print(CONNECTOR.cursor.fetchall())

CONNECTOR.close()
