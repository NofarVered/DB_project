-- Calculate the yearly revenue of companies 
CREATE VIEW Yearly_Revenues AS 
SELECT Companies.id, Companies.name, YEAR(x.release_date) AS 'Work Year', SUM(y.BoxOffice) AS 'Revenues'
FROM Companies, Movies x, Movies y, Movie_companies
WHERE Companies.id= Movie_companies.company_id AND x.id= Movie_companies.movie_id
AND x.id= y.id
GROUP BY Companies.name, 'Work Year'
ORDER BY Movies.BoxOffice;

SELECT  Yearly_revenue.YEAR,
        revenues,
        LEAD (revenues, 12) OVER (ORDER BY month ASC) AS next_year_revenue
FROM Yearly_revenue
ORDER BY next_year_revenue DESC;

