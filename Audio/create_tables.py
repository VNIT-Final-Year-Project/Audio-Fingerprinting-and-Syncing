import psycopg2

con = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS audio (
              id serial primary key,
              name varchar(150) NOT NULL)""")
cur.execute("""CREATE TABLE IF NOT EXISTS hashvalues (
                      id serial primary key,
                      hash varchar(150) NOT NULL,
                      audio_id bigint NOT NULL,
                      position bigint NOT NULL)
                      """)

cur.execute("""CREATE INDEX idx_hash 
                ON hashvalues(hash);""")

con.commit()
cur.close()
con.close()