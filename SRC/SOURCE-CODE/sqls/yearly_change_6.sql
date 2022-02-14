SELECT Q.Genre_name, Q.Year, Q.revenue- Q.past_year_revenue AS Yearly_change
FROM
(SELECT  Genres.name AS Genre_name, x.Year AS Year,
        x.revenues AS revenue,
        y.revenues AS past_year_revenue
        FROM  Genres, Genre_Yearly_Revenues x, Genre_Yearly_Revenues y
        WHERE x.Year= 2009
        AND y.Year = (2009 - 1)
        AND Genres.name= 'Action'
        AND x.name= 'Action'
        AND y.name= 'Action'
        AND y.revenues IS NOT NULL
) AS Q

-- A query to fetch the delta between the specified year's revenue of a genre to the revenue of the year before that
