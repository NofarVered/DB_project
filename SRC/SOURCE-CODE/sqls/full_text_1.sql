SELECT
    CONCAT("How many percent of the movies have the word %s in there name?") as question,
    (COUNT(m.imdb_id)/ma.amount)*100 as answer,
FROM
    Movies AS m, amount_movies_in_db AS ma
WHERE
	  MATCH(title) AGAINST( %s IN BOOLEAN MODE)
LIMIT 1
END