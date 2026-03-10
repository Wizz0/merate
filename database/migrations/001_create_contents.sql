CREATE TABLE contents (
	id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    cover_url VARCHAR(255),
    release_year INTEGER,
    author VARCHAR(255),
    rating INTEGER,
    review_text TEXT,
    created_at DATE DEFAULT CURRENT_DATE
);

INSERT INTO contents(title, type, cover_url, release_year, author, rating, review_text) VALUES
    ('Minecraft', 'игра', '', 2011, 'Mojang', 6, 'Minecraft - моя жизнь');