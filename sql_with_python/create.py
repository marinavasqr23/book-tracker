import psycopg

con = psycopg.connect (
    host='localhost',   
    dbname='Livros',        
    user='postgres',           
    password='marina34'
)

cur = con.cursor()

try:
    # Creating tables
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Genre (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Author (
<<<<<<< HEAD
            id SERIAL PRIMARY KEY,
=======
            id INT PRIMARY KEY,
>>>>>>> e365000185ce93d7b81c3b6490614613067bcec8
            name VARCHAR(100),
            birth_date DATE,
            country VARCHAR(50),
            biography TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Book (
<<<<<<< HEAD
            id SERIAL PRIMARY KEY,
=======
            id INT PRIMARY KEY,
>>>>>>> e365000185ce93d7b81c3b6490614613067bcec8
            title VARCHAR(100),
            num_pags INT,
            publication_year DATE,
            id_author INT,
            id_genre INT,
            rating DECIMAL(3,2),
            read_year DATE,
            language VARCHAR(50),
            image VARCHAR(255),
            reading_status VARCHAR(50),
            synopsis TEXT,
            FOREIGN KEY (id_author) REFERENCES Author(id),
            FOREIGN KEY (id_genre) REFERENCES Genre(id)
        );
    """)

    con.commit()
    print("Tabelas criadas com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro ao criar tabelas:", e)

finally:
    cur.close()
    con.close()