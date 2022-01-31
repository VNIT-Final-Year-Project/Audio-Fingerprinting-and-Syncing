from Audio.database import database
import psycopg2


class postgres_database(database):
    def __init__(self,connection_string):
        self.connection_string = connection_string

    def fingerprint_to_database(self,SongName):
        con = psycopg2.connect(
            host="localhost",
            database="tarundb",
            user="postgres",
            password="postgres"

        )

        cur = con.cursor()


        cur.closer()
        con.close()

    def record_result_from_database(self):
        con = psycopg2.connect(
            host="localhost",
            database="tarundb",
            user="postgres",
            password="postgres"

        )



        con.close()