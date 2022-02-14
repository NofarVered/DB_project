import mysql.connector


def run_sql_file(CONNECTOR, sql_path, pt, **fmt):
    cur = CONNECTOR.cursor()
    with open(sql_path, "r") as f:
        cur.execute(f.read().format(**fmt))
        result = cur.fetchone()
    for row in result:
        print(row)
    cur.close()


def query_1(CONNECTOR, input):
    query = """SELECT Movies.title
    FROM
    Movies AS m
    WHERE
	  MATCH(Movies.title) AGAINST( %s IN BOOLEAN MODE) """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [input])
    result_len = len(mycursor.fetchall())
    query2 = """"SELECT * FROM Movies"""
    mycursor.execute(query2)
    total_len = len(mycursor.fetchall())
    mycursor.close()
    print(result_len/total_len*100)


def query_4(CONNECTOR, act1, act2):
    query = """SELECT Actors.name AS act_name, AVG(Movies.rating) AS avg_rating
    FROM    
    Movies
    INNER JOIN
        Movie_actors ON Movies.imdb_id = Movie_actors.movie_id
    INNER JOIN
    Actors ON Actors.imdb_id = Movie_actors.actor_id
    WHERE Actors.name = %s OR Actors.name = %s
    GROUP BY act_name
    LIMIT 2 """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [act1, act2])
    result = mycursor.fetchall()
    rating1 = result[0][1]
    name1 = result[0][0]
    rating2 = result[1][1]
    name2 = result[1][0]
    mycursor.close()
    if (rating1 > rating2):
        print("The rating of", name1, "is higher")
    elif (rating1 < rating2):
        print("The rating of", name2, "is higher")
    else:
        print("They have the same rating")
