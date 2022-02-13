SELECT CONCAT("What is the average rating that %s (actor) got for her\his movies?") AS question, 
AVG(a.rt) AS answer
FROM     
	(SELECT DISTINCT Movies.imdb_id AS id, Movies.rating AS rt, Actors.name AS nm
    FROM    
        Movies
        LEFT JOIN
            Movies ON Movies.imdb_id = Movie_actors.movie_id
        LEFT JOIN
        Actors ON Actors.imdb_id = Movie_actors.actor_id
		GROUP BY nm) a
WHERE a.nm = %s
LIMIT 1
END