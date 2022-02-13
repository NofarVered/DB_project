SELECT
   topten.name, topten.total_gender
FROM
    (SELECT Movies.name AS name, Movies.imdb_id AS id, Movies.profit AS profit, COUNT(Actors.sex) AS total_gender
    FROM    
        Movies
        INNER JOIN
            Movies ON Movies.imdb_id = Movie_actors.movie_id
        INNER JOIN
        Actors ON Actors.imdb_id = Movie_actors.actor_id
    WHERE Actors.sex= %s
    GROUP BY id
    ORDER BY profit DESC
    LIMIT 10) topten
END




