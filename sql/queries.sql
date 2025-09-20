-- Hilton Queries --

-- Query 1: Calculates the percentage of traffic per keyword.
SELECT 
    k.keyword_id,
    traffic_type,
    COUNT(*) AS traffic_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM hilton_access), 2) AS traffic_percentage
FROM hilton_access a
JOIN hilton_keyword k ON a.keyword_id = k.keyword_id
GROUP BY k.keyword_id, traffic_type;

-- Query 2: Calculates the bounce rate per month.
-- Bounce rate is the percentage of visits with only 1 page visited.
SELECT 
    EXTRACT(YEAR FROM access_date) AS year,
    EXTRACT(MONTH FROM access_date) AS month,
    COUNT(CASE WHEN pages_visited = '1' THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM hilton_access
GROUP BY year, month;

-- Query 3: Calculates the average session duration in seconds and formatted as HH:MM:SS.
SELECT 
    ROUND(AVG(EXTRACT(EPOCH FROM session_duration)), 0) AS avg_session_duration_seconds,
    TO_CHAR(AVG(session_duration), 'HH24:MI:SS') AS avg_session_duration_formatted
FROM hilton_access;

-- Query 4: Calculates the average number of pages visited per session.
SELECT 
    ROUND(AVG(CAST(pages_visited AS INTEGER)), 2) AS avg_pages_per_visit
FROM hilton_access;

-- Query 5: Calculates the overall bounce rate.
SELECT 
    ROUND(
        (SUM(CASE WHEN pages_visited = '1' THEN 1 ELSE 0 END) * 100.0) 
        / COUNT(*), 2) AS bounce_rate
FROM hilton_access;

-- Query 6: Calculates the percentage of visitors by gender.
SELECT gender,ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM hilton_visitor), 2) AS gender_percentage
FROM hilton_visitor
GROUP BY gender;

-- Query 7: Calculates the percentage of visitors by age group.
SELECT age_group,ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM hilton_visitor), 2) AS age_group_percentage
FROM hilton_visitor
GROUP BY age_group;

-- Query 8: Calculates the percentage of visitors by country, sorted in descending order.
SELECT country,ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM hilton_visitor), 2) AS country_percentage
FROM hilton_visitor
GROUP BY country
ORDER BY country_percentage DESC;

-- Query 9: Counts the total number of accesses per month.
SELECT EXTRACT(YEAR FROM access_date) AS year,EXTRACT(MONTH FROM access_date) AS month,COUNT(*) AS total_accesses
FROM hilton_access
GROUP BY year, month;

-- Query 10: Calculates the bounce rate per month.
SELECT EXTRACT(YEAR FROM access_date) AS year,EXTRACT(MONTH FROM access_date) AS month,COUNT(CASE WHEN pages_visited = '1' THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM hilton_access
GROUP BY year, month;

-- Query 11: Calculates the average number of pages visited per month.
SELECT EXTRACT(YEAR FROM access_date) AS year,EXTRACT(MONTH FROM access_date) AS month,AVG(CAST(pages_visited AS INTEGER)) AS average_pages_visited
FROM hilton_access
GROUP BY year, month
ORDER BY year, month;

-- Query 12: Counts the number of accesses per device type and calculates the percentage.
SELECT device,COUNT(*) AS total_accesses,ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hilton_access)), 2) AS percentage
FROM hilton_access
GROUP BY device
ORDER BY total_accesses DESC;


-- Query 13: Calculates the average session duration per month.
SELECT EXTRACT(YEAR FROM access_date) AS year,EXTRACT(MONTH FROM access_date) AS month,AVG(CAST(session_duration AS INTERVAL)) AS average_session_duration
FROM hilton_access
GROUP BY year, month
ORDER BY year, month;

-- Four Seasons Queries --

-- Query 1: Calculates the percentage of traffic per keyword.
SELECT 
    k.keyword_id,
    traffic_type,
    COUNT(*) AS traffic_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM fourseasons_access), 2) AS traffic_percentage
FROM fourseasons_access a
JOIN fourseasons_keyword k ON a.keyword_id = k.keyword_id
GROUP BY k.keyword_id, traffic_type;

-- Query 2: Calculates the bounce rate per month.
-- Bounce rate is the percentage of visits with only 1 page visited.
SELECT 
    EXTRACT(YEAR FROM access_date) AS year,
    EXTRACT(MONTH FROM access_date) AS month,
    COUNT(CASE WHEN pages_visited = '1' THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM fourseasons_access
GROUP BY year, month;

-- Query 3: Calculates the average session duration in seconds and formatted as HH:MM:SS.
SELECT 
    ROUND(AVG(EXTRACT(EPOCH FROM session_duration)), 0) AS avg_session_duration_seconds,
    TO_CHAR(AVG(session_duration), 'HH24:MI:SS') AS avg_session_duration_formatted
FROM fourseasons_access;

-- Query 4: Calculates the total number of visitors by country.
SELECT 
    country, 
    COUNT(*) AS total_visitors
FROM fourseasons_visitor
GROUP BY country
ORDER BY total_visitors DESC;

-- Query 5: Retrieves the top 10 most common keywords used in searches.
SELECT 
    k.keyword,
    COUNT(*) AS keyword_usage
FROM fourseasons_access a
JOIN fourseasons_keyword k ON a.keyword_id = k.keyword_id
GROUP BY k.keyword
ORDER BY keyword_usage DESC
LIMIT 10;

-- Query 6: Calculates the total number of visits per traffic type.
SELECT 
    traffic_type, 
    COUNT(*) AS total_visits
FROM fourseasons_access a
JOIN fourseasons_keyword k ON a.keyword_id = k.keyword_id
GROUP BY traffic_type;

-- Query 7: Finds the most popular backlink sources.
SELECT 
    b.source_url, 
    COUNT(*) AS referral_count
FROM fourseasons_access a
JOIN fourseasons_backlink b ON a.backlink_id = b.backlink_id
GROUP BY b.source_url
ORDER BY referral_count DESC
LIMIT 10;

-- Query 8: Determines the percentage of visitors from each age group.
SELECT 
    age_group, 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM fourseasons_visitor) AS age_group_percentage
FROM fourseasons_visitor
GROUP BY age_group;

-- Query 9: Finds the average number of pages visited per session.
SELECT 
    ROUND(AVG(pages_visited), 2) AS avg_pages_per_session
FROM fourseasons_access;

-- Query 10: Identifies the busiest days based on visitor count.
SELECT 
    access_date, 
    COUNT(*) AS visit_count
FROM fourseasons_access
GROUP BY access_date
ORDER BY visit_count DESC
LIMIT 10;

-- Query 11: Calculates the proportion of organic vs. paid traffic.
SELECT 
    traffic_type, 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM fourseasons_access) AS traffic_percentage
FROM fourseasons_access a
JOIN fourseasons_keyword k ON a.keyword_id = k.keyword_id
GROUP BY traffic_type;

-- Query 12: Determines the most common country of origin for visitors.
SELECT 
    country, 
    COUNT(*) AS visitor_count
FROM fourseasons_visitor
GROUP BY country
ORDER BY visitor_count DESC
LIMIT 1;

-- Query 13: Finds the longest and shortest session durations.
SELECT 
    MAX(session_duration) AS longest_session, 
    MIN(session_duration) AS shortest_session
FROM fourseasons_access;

-- Marriott Queries -- 

-- Query 1: Calculates the percentage of traffic per keyword.
SELECT 
    k.keyword_id,
    traffic_type,
    COUNT(*) AS traffic_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM marriott_access), 2) AS traffic_percentage
FROM marriott_access a
JOIN marriott_keyword k ON a.keyword_id = k.keyword_id
GROUP BY k.keyword_id, traffic_type;

-- Query 2: Calculates the bounce rate per month.
-- Bounce rate is the percentage of visits with only 1 page visited.
SELECT 
    EXTRACT(YEAR FROM access_date) AS year,
    EXTRACT(MONTH FROM access_date) AS month,
    COUNT(CASE WHEN pages_visited = '1' THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM marriott_access
GROUP BY year, month;

-- Query 3: Calculates the average session duration in seconds and formatted as HH:MM:SS.
SELECT 
    ROUND(AVG(EXTRACT(EPOCH FROM session_duration)), 0) AS avg_session_duration_seconds,
    TO_CHAR(AVG(session_duration), 'HH24:MI:SS') AS avg_session_duration_formatted
FROM marriott_access;

-- Query 4: Calculates the total number of visitors by country.
SELECT 
    country, 
    COUNT(*) AS total_visitors
FROM marriott_visitor
GROUP BY country
ORDER BY total_visitors DESC;

-- Query 5: Retrieves the top 10 most common keywords used in searches.
SELECT 
    k.keyword,
    COUNT(*) AS keyword_usage
FROM marriott_access a
JOIN marriott_keyword k ON a.keyword_id = k.keyword_id
GROUP BY k.keyword
ORDER BY keyword_usage DESC
LIMIT 10;

-- Query 6: Calculates the total number of visits per traffic type.
SELECT 
    traffic_type, 
    COUNT(*) AS total_visits
FROM marriott_access a
JOIN marriott_keyword k ON a.keyword_id = k.keyword_id
GROUP BY traffic_type;

-- Query 7: Finds the most popular backlink sources.
SELECT 
    b.source_url, 
    COUNT(*) AS referral_count
FROM marriott_access a
JOIN marriott_backlink b ON a.backlink_id = b.backlink_id
GROUP BY b.source_url
ORDER BY referral_count DESC
LIMIT 10;

-- Query 8: Determines the percentage of visitors from each age group.
SELECT 
    age_group, 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM marriott_visitor) AS age_group_percentage
FROM marriott_visitor
GROUP BY age_group;

-- Query 9: Finds the average number of pages visited per session.
SELECT 
    ROUND(AVG(pages_visited), 2) AS avg_pages_per_session
FROM marriott_access;

-- Query 10: Identifies the busiest days based on visitor count.
SELECT 
    access_date, 
    COUNT(*) AS visit_count
FROM marriott_access
GROUP BY access_date
ORDER BY visit_count DESC
LIMIT 10;

-- Query 11: Calculates the proportion of organic vs. paid traffic.
SELECT 
    traffic_type, 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM marriott_access) AS traffic_percentage
FROM marriott_access a
JOIN marriott_keyword k ON a.keyword_id = k.keyword_id
GROUP BY traffic_type;

-- Query 12: Determines the most common country of origin for visitors.
SELECT 
    country, 
    COUNT(*) AS visitor_count
FROM marriott_visitor
GROUP BY country
ORDER BY visitor_count DESC
LIMIT 1;

-- Query 13: Finds the longest and shortest session durations.
SELECT 
    MAX(session_duration) AS longest_session, 
    MIN(session_duration) AS shortest_session
FROM marriott_access;

-- Shangri-La Queries -- 

-- Query 1: Calculates the percentage of traffic per keyword.
SELECT 
    k.keyword_id,
    traffic_type,
    COUNT(*) AS traffic_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM shangri_access), 2) AS traffic_percentage
FROM shangri_access a
JOIN shangri_keyword k ON a.keyword_id = k.keyword_id
GROUP BY k.keyword_id, traffic_type;

-- Query 2: Calculates the bounce rate per month.
-- Bounce rate is the percentage of visits with only 1 page visited.
SELECT 
    EXTRACT(YEAR FROM access_date) AS year,
    EXTRACT(MONTH FROM access_date) AS month,
    COUNT(CASE WHEN pages_visited = '1' THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM shangri_access
GROUP BY year, month;

-- Query 3: Calculates the average session duration in seconds and formatted as HH:MM:SS.
SELECT 
    ROUND(AVG(EXTRACT(EPOCH FROM session_duration)), 0) AS avg_session_duration_seconds,
    TO_CHAR(AVG(session_duration), 'HH24:MI:SS') AS avg_session_duration_formatted
FROM shangri_access;

-- Query 4: Calculates the average number of pages visited per session.
SELECT 
    ROUND(AVG(CAST(pages_visited AS INTEGER)), 2) AS avg_pages_per_visit
FROM shangri_access;

-- Query 5: Calculates the overall bounce rate.
SELECT 
    ROUND(
        (SUM(CASE WHEN pages_visited = '1' THEN 1 ELSE 0 END) * 100.0) 
        / COUNT(*), 2) AS bounce_rate
FROM shangri_access;

-- Query 6: Calculates the percentage of visitors by gender.
SELECT 
    gender,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM shangri_visitor), 2) AS gender_percentage
FROM shangri_visitor
GROUP BY gender;

-- Query 7: Calculates the percentage of visitors by age group.
SELECT 
    age_group,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM shangri_visitor), 2) AS age_group_percentage
FROM shangri_visitor
GROUP BY age_group;

-- Query 8: Calculates the percentage of visitors by country, sorted in descending order.
SELECT 
    country,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM shangri_visitor), 2) AS country_percentage
FROM shangri_visitor
GROUP BY country
ORDER BY country_percentage DESC;

-- Query 9: Counts the total number of accesses per month.
SELECT EXTRACT(YEAR FROM access_date) AS year,
       EXTRACT(MONTH FROM access_date) AS month,
       COUNT(*) AS total_accesses
FROM shangri_access
GROUP BY year, month;

-- Query 10: Calculates the bounce rate per month.
SELECT EXTRACT(YEAR FROM access_date) AS year,
       EXTRACT(MONTH FROM access_date) AS month,
       COUNT(CASE WHEN pages_visited = '1' THEN 1 END) * 100.0 / COUNT(*) AS bounce_rate
FROM shangri_access
GROUP BY year, month;

-- Query 11: Calculates the average number of pages visited per month.
SELECT 
    EXTRACT(YEAR FROM access_date) AS year,
    EXTRACT(MONTH FROM access_date) AS month,
    AVG(CAST(pages_visited AS INTEGER)) AS average_pages_visited
FROM 
    shangri_access
GROUP BY 
    year, month
ORDER BY 
    year, month;

-- Query 12: Counts the number of accesses per device type and calculates the percentage.
SELECT 
    device,
    COUNT(*) AS total_accesses,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM shangri_access)), 2) AS percentage
FROM 
    shangri_access
GROUP BY 
    device
ORDER BY 
    total_accesses DESC;

-- Query 13: Calculates the average session duration per country in seconds.
SELECT v.country, AVG(EXTRACT(EPOCH FROM session_duration)) AS avg_session_duration_seconds
FROM shangri_access a
JOIN shangri_visitor v ON a.visitor_id = v.visitor_id
GROUP BY v.country;

-- Query 14: Calculates the average session duration per month.
SELECT 
    EXTRACT(YEAR FROM access_date) AS year,
    EXTRACT(MONTH FROM access_date) AS month,
    AVG(CAST(session_duration AS INTERVAL)) AS average_session_duration
FROM 
    shangri_access
GROUP BY 
    year, month
ORDER BY 
    year, month;
