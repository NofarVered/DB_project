import mysql.connector


def query_1(CONNECTOR, input):
    query = """SELECT m.title
    FROM
    Movies AS m
    WHERE
	  MATCH(m.title) AGAINST( %s IN BOOLEAN MODE) """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [input])
    result_len = len(mycursor.fetchall())
    
    mycursor.execute("SELECT * FROM Movies")
    total_len = len(mycursor.fetchall())
    
    mycursor.close()
    print("The movies that have ",input, "in their title make ", result_len/total_len*100, "% of the entire movies")


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


def query_6(CONNECTOR, year, genre):
    query = """SELECT Q.Genre_name, Q.Year, Q.revenue-Q.past_year_revenue AS Yearly_change
        FROM
        (SELECT  Genres.name AS Genre_name, x.Year AS Year,
                x.revenues AS revenue,
                y.revenues AS past_year_revenue
                FROM  Genres, Genre_Yearly_Revenues x, Genre_Yearly_Revenues y
                WHERE x.Year= %s
                AND y.Year = (CONVERT(%s, SIGNED INTEGER) - 1)
                AND Genres.name= %s
                AND x.name= %s
                AND y.name= %s
                AND y.revenues IS NOT NULL
        ) AS Q """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [year, year, genre, genre, genre])
    result = mycursor.fetchall()
    print(result)
    if (result[0][2]<0):
        print(year, "was a bad year for the ", genre, "movies")
    else:
        print(year, "was a good year for the ", genre, "movies")
    mycursor.close()


def query_2(CONNECTOR, pt):
    query = """SELECT
            a.avg_profit as answer
        FROM
            (SELECT 
            Genres.name, AVG(Movies.profit) as avg_profit
            FROM Movies
                INNER JOIN
            Movie_genres ON Movies.imdb_id = Movie_genres.movie_id
                INNER JOIN
            Genres ON Genres.id = Movie_genres.genre_id
            GROUP BY Genres.name) AS a
        WHERE
            a.name = %s
        LIMIT 1"""
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [pt])
    result = mycursor.fetchall()
    print("the average profit is", result[0][0], "USD dollars")
    mycursor.close()


def query_3(CONNECTOR, pt):
    query = """ SELECT
            a.title, a.total_gender, b.total_cast, IF (a.total_gender*2> b.total_cast, "True", "False") AS feminist
            FROM
                    (SELECT  Movies.title AS title, Movies.imdb_id AS id, Movies.profit AS profit, COUNT(Actors.sex) AS total_gender
                FROM Movies, Movie_actors, Actors
                WHERE Movies.imdb_id = Movie_actors.movie_id 
                AND Movies.imdb_id = Movie_actors.movie_id 
                AND Actors.imdb_id = Movie_actors.actor_id
                AND Actors.sex = "Female"
                GROUP BY id)a, 
                    (SELECT  Movies.title AS title, Movies.imdb_id AS id, Movies.profit AS profit, COUNT(Actors.imdb_id) AS total_cast
                    FROM Movies, Movie_actors, Actors
                    WHERE Movies.imdb_id = Movie_actors.movie_id 
                    AND Movies.imdb_id = Movie_actors.movie_id 
                    AND Actors.imdb_id = Movie_actors.actor_id
                    GROUP BY id)b
            WHERE  a.title = b.title
            AND a.title = %s
            LIMIT 1 """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [pt])
    result = mycursor.fetchall()
    print(result)
    if (result[0][3] == "False"):
        print("Unfortantlly, there is more males actors in the cast! they have only", result[0][1],"female actors")
    else:
         print("It is a feminist cast!", result[0][1],"female actors")
    mycursor.close()


def query_5(CONNECTOR, pt):
    query = """ SELECT AVG(a.run_time) as answer
                FROM (SELECT Movies.run_time, Movies.imdb_id, Genres.name 
                        FROM Movies, Genres, Movie_genres, Genre_Yearly_Revenues
                        WHERE YEAR(Movies.release_date) = %s
                        AND Movie_genres.movie_id= Movies.imdb_id
                        AND Movie_genres.genre_id= Genres.id
                        AND Genre_Yearly_Revenues.Year= %s
                        AND Genre_Yearly_Revenues.name= Genres.name
                        AND Genre_Yearly_Revenues.Revenues>= ALL (SELECT Genre_Yearly_Revenues.Revenues 
                                                            FROM Genre_Yearly_Revenues
                                                            WHERE Year = %s)) AS a
                        
                ORDER BY answer DESC
                LIMIT 1 """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [pt, pt, pt])
    result = mycursor.fetchall()
    print(result[0][0])
    mycursor.close()


def query_7(CONNECTOR, user_genre, user_num):
    query = """ SELECT Q.Actor_name, Q.total_profit
                FROM
                (SELECT Actors.name AS Actor_name, Genres.name, SUM(Movies.profit) AS total_profit
                FROM Actors, Genres, Movie_genres, Movie_actors, Movies
                WHERE Actors.imdb_id= Movie_actors.actor_id 
                    AND Movie_actors.movie_id= Movies.imdb_id 
                    AND Movies.imdb_id= Movie_genres.movie_id 
                    AND Genres.id=Movie_genres.genre_id
                    AND Genres.name = %s
                GROUP BY Actors.name
                HAVING COUNT(DISTINCT Movies.imdb_id) >= CONVERT(%s, SIGNED INTEGER)) AS Q
                ORDER BY Q.total_profit DESC
                LIMIT 1 """
    mycursor = CONNECTOR.cursor()
    mycursor.execute(query, [user_genre, user_num])
    result = mycursor.fetchall()
    print(result)
    print(result[0][0], "is the most profitable actor" )
    mycursor.close()
