📚 Personal Reading Project
This is a website to track my personal readings. Through this system, I can add books, update information about my readings, and view the reading progress of each book, all privately. Other people can access the site, but they do not have permission to edit or add books.

🛠️ Technologies Used
This project was developed using the following tools and technologies:

📌 Frontend:
React.js: A JavaScript library for building dynamic and interactive user interfaces.
Tailwind CSS: A CSS framework for creating modern and responsive interfaces quickly and efficiently.
Axios: A library for making HTTP requests to the backend and updating information in the database.

📌 Backend:
Node.js: A JavaScript runtime environment for running the server.
Express.js: A framework for building RESTful APIs simply and efficiently.
MySQL: A relational database management system to store information about books, authors, and genres.

📌 Others:
Figma: Project mockups.
Git & GitHub: Version control tools for managing the source code and project versioning.

🗃️ Database Entities
The system is based on three main entities: Book, Author, and Genre.
Below are the details of each entity:

Book (
    id INT PRIMARY KEY,                  -- Unique identifier for the book
    title VARCHAR(100),                   -- Title of the book (maximum 100 characters)
    num_pags INT,                         -- Number of pages in the book
    publication_year DATE,                -- Year of publication of the book
    id_author INT,                        -- Author ID (linked to the Author table)
    id_genre INT,                         -- Genre ID (linked to the Genre table)
    rating DECIMAL(3,2),                  -- Rating of the book (0 to 10, with up to 2 decimal places)
    read_year DATE,                       -- Year the book was read
    language VARCHAR(50),                 -- Language the book was written in
    image VARCHAR(255),                   -- URL or path to the book cover image (maximum 255 characters)
    reading_status VARCHAR(50),           -- Status of reading (e.g., "In progress", "Completed")
    synopsis TEXT,                        -- Synopsis or summary of the book (long text)
    FOREIGN KEY (id_author) REFERENCES Author(id),  -- Relationship with the Author table
    FOREIGN KEY (id_genre) REFERENCES Genre(id)     -- Relationship with the Genre table
);



Author (
    id INT PRIMARY KEY,                -- Unique identifier for the author
    name VARCHAR(100),                  -- Author's name
    birth_date DATE,                    -- Author's birth date
    country VARCHAR(50),                -- Author's country of origin
    biography TEXT                      -- Author's biography
);

Genre (
    id INT PRIMARY KEY,                -- Unique identifier for the genre
    name VARCHAR(50)                    -- Name of the genre (e.g., "Fiction", "Fantasy", "Romance", etc.)
);
