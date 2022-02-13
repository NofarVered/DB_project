SELECT
    CONCAT("What is the total profit for movies that have the word %s in there title?") as question,
    SUM(Movies.profit) as answer,
FROM
    Movies
WHERE
	  MATCH(title) AGAINST(%s IN BOOLEAN MODE)
GROUP BY movie_id
LIMIT 1
