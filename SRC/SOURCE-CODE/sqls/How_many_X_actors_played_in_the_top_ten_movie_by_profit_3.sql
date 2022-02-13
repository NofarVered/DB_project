SELECT
    CONCAT("How many %s (sex) actors played in the top ten leading movie by profit?") as question,
    COUNT(a.id) AS answer,
FROM
    (SELECT DISTINCT Movies.imdb_id AS id, Movies.profit AS profit, Actors.sex AS sex
    FROM    
        Movies
        LEFT JOIN
            Movies ON Movies.imdb_id = Movie_actors.movie_id
        LEFT JOIN
        Actors ON Actors.imdb_id = Movie_actors.actor_id
    ORDER BY Movies.profit DESC
    LIMIT 10) a
WHERE
    Actors.sex = %s
LIMIT 1
END




