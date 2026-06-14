SELECT
    ROUND(
        COUNT(DISTINCT a.player_id) /
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM Activity a
JOIN Activity b
    ON a.player_id = b.player_id
WHERE DATEDIFF(b.event_date, a.event_date) = 1
AND a.event_date = (
    SELECT MIN(event_date)
    FROM Activity c
    WHERE c.player_id = a.player_id
);