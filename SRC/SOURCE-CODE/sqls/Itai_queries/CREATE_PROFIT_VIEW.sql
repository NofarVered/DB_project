-- Calculate the yearly revenue of companies 
CREATE VIEW Yearly_Revenues AS 
SELECT Genres.name, YEAR(x.release_date) AS 'Work Year', SUM(y.profit) AS 'Revenues'
FROM Movies x, Movies y, Movie_genres
WHERE Movie_genres.genre_id= Genres.id AND x.id= Movie_genres.movie_id
AND x.id= y.id
GROUP BY Genres.name, 'Work Year'
ORDER BY Work Year DESC;

