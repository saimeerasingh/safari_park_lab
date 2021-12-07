DROP TABLE IF EXISTS staffs;

CREATE TABLE staffs(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    department VARCHAR(255),
    performance_rating INT
)