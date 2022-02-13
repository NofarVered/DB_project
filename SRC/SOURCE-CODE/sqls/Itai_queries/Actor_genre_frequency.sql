-- Show the most profitable actor that playes in at least %s movies of the specified genre
SELECT Actors.name
FROM Actors, Genres, Movie_genres, Movie_actors
WHERE Actors.id= Movie_actors.actor_id AND Movie_actors.movie_id= Movies. id AND Movies.id= Movie_genres.movie_id AND genres.id=Movie_genres.genre_id
AND genre.name= "%s"
GROUP BY Actors.name
HAVING COUNT(DISTINCT Movies.id)>"%s"
