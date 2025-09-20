-- Hilon Visitor Table --
CREATE TABLE hilton_visitor (
	visitor_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female')),
    country TEXT NOT NULL,
    age INT NOT NULL CHECK (age >= 18 AND age <= 120),
    age_group VARCHAR(20) GENERATED ALWAYS AS (
        CASE
            WHEN age BETWEEN 18 AND 24 THEN '18 - 24'
            WHEN age BETWEEN 25 AND 34 THEN '25 - 34'
            WHEN age BETWEEN 35 AND 44 THEN '35 - 44'
            WHEN age BETWEEN 45 AND 54 THEN '45 - 54'
			WHEN age BETWEEN 55 AND 64 THEN '55 - 64'
            WHEN age >= 65 THEN '65+'
            ELSE 'Unknown'
        END
    ) STORED
);
-- Hilton Backlink Table - 
CREATE TABLE hilton_backlink (
    backlink_id SERIAL PRIMARY KEY,
	backlink_url TEXT NOT NULL UNIQUE,
    source_url TEXT NOT NULL 
);
-- Hilton Keyword Table -- 
CREATE TABLE hilton_keyword(
    keyword_id SERIAL PRIMARY KEY,
    traffic_type VARCHAR(50) NOT NULL CHECK (traffic_type IN ('Organic', 'Paid')),
    keyword TEXT NOT NULL UNIQUE
);
-- Hilton Access Table --
CREATE TABLE hilton_access (
	session_id SERIAL PRIMARY KEY,
    visitor_id INT NOT NULL,
    access_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pages_visited INT NOT NULL,
    session_duration INTERVAL NOT NULL DEFAULT '00:00:00',
    device VARCHAR(50) NOT NULL,
    backlink_id INT,
    keyword_id INT,
    FOREIGN KEY (visitor_id) REFERENCES hilton_visitor(visitor_id) ON DELETE CASCADE, -- foreign keys for data integrity
    FOREIGN KEY (backlink_id) REFERENCES hilton_backlink(backlink_id) ON DELETE CASCADE, -- all backlinks should be able to be verified, data integrity
    FOREIGN KEY (keyword_id) REFERENCES hilton_keyword(keyword_id)
);
-- Four Seasons Visitor Table --
CREATE TABLE fourseasons_visitor (
    visitor_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female')),
    country TEXT NOT NULL,
    age INT NOT NULL CHECK (age >= 18 AND age <= 150),
    age_group VARCHAR(20) GENERATED ALWAYS AS (
        CASE
            WHEN age BETWEEN 18 AND 24 THEN '18 - 24'
            WHEN age BETWEEN 25 AND 34 THEN '25 - 34'
            WHEN age BETWEEN 35 AND 44 THEN '35 - 44'
            WHEN age BETWEEN 45 AND 54 THEN '45 - 54'
            WHEN age BETWEEN 55 AND 64 THEN '55 - 64'
            WHEN age >= 65 THEN '65+'
            ELSE 'Unknown'
        END
    ) STORED
);
-- Four Seasons Backlink Table
CREATE TABLE fourseasons_backlink (
    backlink_id SERIAL PRIMARY KEY, 
	backlink_url TEXT NOT NULL UNIQUE,
    source_url TEXT NOT NULL
);
-- Four Seasons Keyword Table -- 
CREATE TABLE fourseasons_keyword(
    keyword_id SERIAL PRIMARY KEY,
    traffic_type VARCHAR(50) NOT NULL CHECK (traffic_type IN ('Organic', 'Paid')),
    keyword TEXT NOT NULL UNIQUE
    );
-- Four Seasons Access Table -- 
CREATE TABLE fourseasons_access (
    access_id SERIAL PRIMARY KEY,
    visitor_id INT NOT NULL,
    access_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pages_visited INT NOT NULL,
    session_duration INTERVAL NOT NULL DEFAULT '00:00:00',
    device VARCHAR(50) NOT NULL,
    backlink_id INT,
    keyword_id INT,
    FOREIGN KEY (visitor_id) REFERENCES fourseasons_visitor(visitor_id) ON DELETE CASCADE, -- foreign keys for data integrity
    FOREIGN KEY (backlink_id) REFERENCES fourseasons_backlink(backlink_id) ON DELETE CASCADE, -- all backlinks should be able to be verified, data integrity
    FOREIGN KEY (keyword_id) REFERENCES fourseasons_keyword(keyword_id)
);
-- Marriott Visitor Table --
CREATE TABLE marriott_visitor (
visitor_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female')),
    country TEXT NOT NULL,
    age INT NOT NULL CHECK (age >= 18 AND age <= 150),
    age_group VARCHAR(20) GENERATED ALWAYS AS (
        CASE
            WHEN age BETWEEN 18 AND 24 THEN '18 - 24'
            WHEN age BETWEEN 25 AND 34 THEN '25 - 34'
            WHEN age BETWEEN 35 AND 44 THEN '35 - 44'
            WHEN age BETWEEN 45 AND 54 THEN '45 - 54'
WHEN age BETWEEN 55 AND 64 THEN '55 - 64'
            WHEN age >= 65 THEN '65+'
            ELSE 'Unknown'
        END
    ) STORED
);
-- Marriott Backlink Table --
CREATE TABLE marriott_backlink (
    backlink_id SERIAL PRIMARY KEY, 
	backlink_url TEXT NOT NULL UNIQUE,
    source_url TEXT NOT NULL
);
-- Marrriott Keyword Table --
CREATE TABLE marriott_keyword(
    keyword_id SERIAL PRIMARY KEY,
    traffic_type VARCHAR(50) NOT NULL CHECK (traffic_type IN ('Organic', 'Paid')),
    keyword TEXT NOT NULL UNIQUE
);
-- Marriott Access Table --
CREATE TABLE marriott_access (
	access_id SERIAL PRIMARY KEY,
    visitor_id INT NOT NULL,
    pages_visited INT NOT NULL,
    session_duration INTERVAL NOT NULL DEFAULT '00:00:00',
    device VARCHAR(50) NOT NULL,
    backlink_id INT,
    keyword_id INT,
    access_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (visitor_id) REFERENCES marriott_visitor(visitor_id) ON DELETE CASCADE, -- foreign keys for data integrity
    FOREIGN KEY (backlink_id) REFERENCES marriott_backlink(backlink_id) ON DELETE CASCADE, -- all backlinks should be able to be verified, data integrity
    FOREIGN KEY (keyword_id) REFERENCES marriott_keyword(keyword_id)
);
-- Shangri-La Visitor Table --
CREATE TABLE shangri_visitor (
    visitor_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female')),
    country TEXT NOT NULL,
    age INT NOT NULL CHECK (age >= 18 AND age <= 150),
    age_group VARCHAR(20) GENERATED ALWAYS AS (
        CASE
            WHEN age BETWEEN 18 AND 24 THEN '18 - 24'
            WHEN age BETWEEN 25 AND 34 THEN '25 - 34'
            WHEN age BETWEEN 35 AND 44 THEN '35 - 44'
            WHEN age BETWEEN 45 AND 54 THEN '45 - 54'
            WHEN age BETWEEN 55 AND 64 THEN '55 - 64'
            WHEN age >= 65 THEN '65+'
            ELSE 'Unknown'
        END
    ) STORED
);
-- Shangri-La Backlink Table --
CREATE TABLE shangri_backlink (
    backlink_id SERIAL PRIMARY KEY, 
	backlink_url TEXT NOT NULL UNIQUE,
    source_url TEXT NOT NULL
);
-- Shangri-La Keyword Table --
CREATE TABLE shangri_keyword (
    keyword_id SERIAL PRIMARY KEY,
    traffic_type VARCHAR(50) NOT NULL CHECK (traffic_type IN ('Organic', 'Paid')),
    keyword TEXT NOT NULL UNIQUE
);
-- Shangri-La Access Table --
CREATE TABLE shangri_access (
    access_id SERIAL PRIMARY KEY,
    visitor_id INT NOT NULL,
    pages_visited INT NOT NULL,
    session_duration INTERVAL NOT NULL DEFAULT '00:00:00',
    device VARCHAR(50) NOT NULL,
    backlink_id INT,
    keyword_id INT,
    access_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (visitor_id) REFERENCES shangri_visitor(visitor_id) ON DELETE CASCADE,
    FOREIGN KEY (backlink_id) REFERENCES shangri_backlink(backlink_id) ON DELETE CASCADE,
    FOREIGN KEY (keyword_id) REFERENCES shangri_keyword(keyword_id)
);

