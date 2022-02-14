SELECT
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
AND a.title = {pt}



