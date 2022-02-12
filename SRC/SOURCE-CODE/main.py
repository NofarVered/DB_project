import utils
import mysql.connector

CONNECTOR = mysql.connector.connect(
    host='localhost',
    port=3305,
    user='DbMysql36',
    password='DbMysql36',
    database='DbMysql1536'
)
print(CONNECTOR)
mycursor = CONNECTOR.cursor()
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)


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
    5 - I want to know what is the the most popular language at movies in the X-year.
    6 - ITAI QUERIS
    7 - ITAI QUERIS
    """
    navigate = input(what_to_ask)

    if navigate == '1':
        pt = input("\nWhich actor?")
        if pt is None:
            raise ValueError("Must be provided!")
        # TO DO
        break
    elif navigate == '2':
        pt = input("\nWhich genere?")
        if pt is None:
            raise ValueError("Must be provided!")
        utils.get_2(mycursor, pt)
        break
    elif navigate == '3':
        pt = input("\nWhich gender?")
        if pt is None:
            raise ValueError("Must be provided!")
        # TO DO
        break
    elif navigate == '4':
        pt = input("\nWhich actor?")
        if pt is None:
            raise ValueError("Must be provided!")
        # TO DO
        break
    elif navigate == '5':
        pt = input("\nWhich year?")
        if pt is None:
            raise ValueError("Must be provided!")
        # TO DO
        break
    elif navigate == '6':
        # TO DO
        break
    elif navigate == '7':
        # TO DO
        break


CONNECTOR.close()
