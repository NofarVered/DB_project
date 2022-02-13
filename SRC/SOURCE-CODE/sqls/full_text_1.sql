SELECT
    CONCAT("How many percent of the movies have the word %s in there name?") as question,
    SUM(Movies.profit)/CONCAT() as answer,
FROM
    Movies
WHERE
	  MATCH(title) AGAINST(%s IN BOOLEAN MODE)
GROUP BY Movies.imdb_id
LIMIT 1
