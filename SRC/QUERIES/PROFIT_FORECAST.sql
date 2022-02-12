SELECT  Yearly_revenue.YEAR,
        revenues,
        LEAD (revenues, 12) OVER (ORDER BY month ASC) AS next_year_revenue
FROM Yearly_revenue
ORDER BY next_year_revenue DESC;
