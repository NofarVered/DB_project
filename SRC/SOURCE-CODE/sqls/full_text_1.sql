SELECT
    CONCAT("How many percent of the movies have the word {pt} in there name?") as question,
    (COUNT(m.imdb_id)/ma.amount)*100 as answer,
FROM
    Movies AS m, amount_movies_in_db AS ma
WHERE
	  MATCH(Movies.title) AGAINST( {pt} IN BOOLEAN MODE)
GROUP BY m.imdb_id
LIMIT 1
END

