SELECT
    CONCAT("What is the average profit of %s (genre) movies ?") as question,
    AVG(Movies.profit) as answer,
FROM
    Movies
        LEFT JOIN
    Movie_genres ON Movies.imdb_id = Movie_genres.movie_id
        LEFT JOIN
    Genres ON genres.id = Movie_genres.genre_id
WHERE
	  Genres.name = %s
GROUP BY Genres.name
LIMIT 1
