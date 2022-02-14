SELECT CONCAT(" What is the average run time in movies from the most profitable genre at {pt} (year)? ") AS question,
AVG(a.run_time) as answer
FROM (SELECT Movies.run_time, Movies.imdb_id, Genres.name 
		FROM Movies, Genres, Movie_genres, Genre_Yearly_Revenues
		WHERE YEAR(Movies.release_date) =2008
        AND Movie_genres.movie_id= Movies.imdb_id
        AND Movie_genres.genre_id= Genres.id
        AND Genre_Yearly_Revenues.Year= 2008
        AND Genre_Yearly_Revenues.name= Genres.name
        AND Genre_Yearly_Revenues.Revenues>= ALL (SELECT Genre_Yearly_Revenues.Revenues 
                                             FROM Genre_Yearly_Revenues
                                             WHERE Year=2008)) AS a
        
ORDER BY answer DESC
LIMIT 1;
