SELECT CONCAT(" What is the average run time in movies released at %s (year)? ") AS question,
AVG(a.run_time) as answer,
FROM (SELECT Movies.run_time, Movies.imdb_id
		FROM Movies
		WHERE YEAR(Movies.release_date) = %s) a
LIMIT 1
END