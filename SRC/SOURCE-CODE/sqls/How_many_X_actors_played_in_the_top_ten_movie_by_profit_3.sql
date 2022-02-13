SELECT
    CONCAT("How many %s (sex) actors played in the top ten leading movie by profit?") as question,
    COUNT(a.id) AS answer,
FROM
    (SELECT Movies.imdb_id AS id, Movies.profit AS profit, Actors.sex AS sex
    FROM    
        Movies
        INNER JOIN
            Movies ON Movies.imdb_id = Movie_actors.movie_id
        INNER JOIN
        Actors ON Actors.imdb_id = Movie_actors.actor_id
    ORDER BY Movies.profit DESC
    LIMIT 10) a
WHERE
    Actors.sex = %s
LIMIT 1
END




