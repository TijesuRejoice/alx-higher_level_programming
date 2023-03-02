-- Lists all shows contained in hntn_0d_tvshows that have at least one genre linked
-- Lists all rows of a database that have one column in common
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_shows_genres ON tv_shows.id = tv_show_genre.show.id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
