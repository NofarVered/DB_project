-- Show the most profitable actor that playes in at least X movies of the specified genre
SELECT Q.Actor_name, Q.total_profit
FROM
(SELECT Actors.name AS Actor_name, Genres.name, SUM(Movies.profit) AS total_profit
FROM Actors, Genres, Movie_genres, Movie_actors, Movies
WHERE Actors.imdb_id= Movie_actors.actor_id 
    AND Movie_actors.movie_id= Movies.imdb_id 
    AND Movies.imdb_id= Movie_genres.movie_id 
    AND Genres.id=Movie_genres.genre_id
    AND Genres.name = 'Comedy'
GROUP BY Actors.name
HAVING COUNT(DISTINCT Movies.imdb_id) >=2) AS Q
ORDER BY Q.total_profit DESC
LIMIT 1;
