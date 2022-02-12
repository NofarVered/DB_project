-- Select all the companies from countries with at least 5 different movie companies, and show their boxoffice average 

SELECT Companies.name, AVG(Movies.BoxOffice), Companies.origin_country
FROM Companies, Movies, Movie_companies
WHERE Companies.id= Movie_companies.company_id AND Movies.id= Movie_companies.movie_id
AND Comapnies.origin_country IN
 (SELECT Companies.origin_country FROM Companies GROUP BY Companies.origin_country HAVING COUNT(*)>5)
GROUP BY Companies.name
