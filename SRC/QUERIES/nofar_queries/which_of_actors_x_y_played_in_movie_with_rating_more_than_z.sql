SELECT CONCAT("Which of these two actors played in a movie that was rated more than %s on imdb?") AS question,
"Neither" AS option0,
       (SELECT actors.name FROM Actors WHERE actors.rnd_token = {actor_token1}) AS option1,
       "Both" AS option2,
       (SELECT actors.name FROM actors WHERE actors.rnd_token = {actor_token2}) AS option3,
       IF(COUNT(actors.rnd_token) <> 1, COUNT(actors.rnd_token), IF(MIN(actors.rnd_token) = {actor_token1}, 1, 3)) AS answer,
FROM actors
WHERE (actors.rnd_token = {actor_token1} OR actors.rnd_token = {actor_token2}) AND
	  EXISTS (SELECT movies.vote_average
			  FROM movie_actors JOIN movies ON movies.id = movie_actors.movie_id
			  WHERE actors.id = movie_actors.actor_id
					AND vote_average > {rating_token}
			 )
