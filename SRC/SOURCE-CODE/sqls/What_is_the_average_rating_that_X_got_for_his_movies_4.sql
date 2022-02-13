SELECT CONCAT("What is the average rating that {pt} (actor) got for her\his movies?") AS question, 
a.avg_rating AS answer
FROM     
	(SELECT Actors.name AS act_name, AVG(Movies.rating) AS avg_rating
    FROM    
        Movies
        INNER JOIN
            Movies ON Movies.imdb_id = Movie_actors.movie_id
        INNER JOIN
        Actors ON Actors.imdb_id = Movie_actors.actor_id
		GROUP BY act_name) a
WHERE a.act_name = {pt}
LIMIT 1
END