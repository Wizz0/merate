CREATE TABLE contents (
	id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    cover_url VARCHAR(255),
    release_year INTEGER,
    author VARCHAR(255),
    rating INTEGER,
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);