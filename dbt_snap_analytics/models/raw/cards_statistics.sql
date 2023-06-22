SELECT
    index,
    stats_position,
    stats_cuberate_played,
    stats_winrate,
    stats_winrate_played,
    stats_cuberate,
    stats_loss,
    stats_cube_won,
    stats_cube_lost,
    stats_win,
    name
FROM cards
WHERE stats_position IS NOT NULL
ORDER BY stats_position;