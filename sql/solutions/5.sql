WITH avg_students AS (
    SELECT
        district_id,
        AVG(fee) AS average_students
    FROM schools
    GROUP BY district_id
),

SELECT
    s.school_name,
    s.district_id,
    avgs.average_students
FROM school AS s
INNER JOIN avg_students AS avgs
    ON s.district_id = avgs.district_id;
