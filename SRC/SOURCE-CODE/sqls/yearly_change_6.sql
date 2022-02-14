SELECT Q.Genre_name,  Q.revenues- Q. past_year_revenue AS Yearly_change
FROM 
(SELECT  Genres.name AS Genre_name, Genre_Yearly_Revenues.Year,
        Genre_Yearly_Revenues.revenues,
        LAG (Genre_Yearly_Revenues.revenues) OVER (ORDER BY  Year) AS past_year_revenue
FROM Genre_Yearly_Revenues, Genres
WHERE Genre_Yearly_Revenues.Year= {user_year}
AND Genres.name= {user_genre}
AND past_year_revenue IS NOT NULL
) AS Q
LIMIT 1 
END 

-- A query to fetch the delta between the specified year's revenue of a genre to the revenue of the year before that
