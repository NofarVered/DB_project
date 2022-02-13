SELECT CONCAT(" What is the average run time in movies released at {pt} (year)? ") AS question,
AVG(a.run_time) as answer,
FROM (SELECT Movies.run_time, Movies.imdb_id
		FROM Movies
		WHERE YEAR(Movies.release_date) = {pt}) a
ORDER BY cnt DESC
LIMIT 1
END