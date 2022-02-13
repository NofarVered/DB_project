
SELECT Q.Genre_name,  Q.revenues- Q. past_year_revenue AS Yearly_change
FROM 
(SELECT  Genres.name AS Genre_name, Yearly_revenue.YEAR,
        revenues,
        LAG (revenues) OVER (ORDER BY YEAR) AS past_year_revenue
FROM Yearly_revenue, Genres
WHERE Yearly_revenue.YEAR= "%s"
AND Genres.name= "%s") AS Q

-- A query to fetch the delta between the specified year's revenue of a genre to the revenue of the year before that
