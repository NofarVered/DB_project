select genres.genre, round(pct, 2) as pct
from (
         select distinct genre_id,
                         100 * count(*) over (partition by genre_id) / count(*) over () as pct
         from movies m
                  join movie_genres mg on m.id = mg.movie_id
         where MATCH(overview, tagline) AGAINST('+sleep +nightmare' IN BOOLEAN MODE)
     ) a
         join genres on a.genre_id = genres.id
order by pct desc;
