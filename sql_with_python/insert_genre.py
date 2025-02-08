import psycopg

con = psycopg.connect(
    host='localhost',   
    dbname='Livros',        
    user='postgres',           
    password='marina34'
)

cur = con.cursor()
try:
    cur.execute("""
        INSERT INTO Genre (name) VALUES
        ('Fiction'),
        ('Non-fiction'),
        ('Fantasy'),
        ('Science Fiction'),
        ('Mystery'),
        ('Romance'),
        ('Thriller'),
        ('Biography'),
        ('Historical'),
        ('Horror');
    """)

    con.commit()
    print("Data inserted successfully!")

except Exception as e:
    con.rollback()
    print("Error:", e)

finally:
    cur.close()
    con.close()
