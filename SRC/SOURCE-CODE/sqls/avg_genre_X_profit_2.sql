SELECT
    CONCAT("What is the average profit of {pt} movies ?") as question,
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
	a.name = {pt}
LIMIT 1