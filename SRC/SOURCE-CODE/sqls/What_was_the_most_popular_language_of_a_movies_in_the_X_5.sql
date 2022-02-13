SELECT CONCAT(" What was the most popular language of a movies in the %s (year)? ") AS question,
a.lan as answer
Count(a.id) AS cnt
FROM (SELECT Movies.language AS lan,
		Movies.imdb_id AS id
		FROM Movies
		WHERE YEAR(Movies.release_date) = %s) a
GROUP BY a.lan
ORDER BY cnt DESC
LIMIT 1
END