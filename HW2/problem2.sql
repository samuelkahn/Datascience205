SELECT username, COUNT(*) as frequency
FROM
(SELECT page_users.page_id, page_users.user_id,pages.page_title, users.username
FROM page_users
LEFT JOIN pages
ON page_users.page_id=pages.page_id
INNER JOIN users
ON page_users.user_id=users.user_id
GROUP BY username,page_title)
GROUP BY username
ORDER BY frequency DESC;
