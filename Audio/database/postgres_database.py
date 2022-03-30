import collections

from Audio.database.database import database
import psycopg2


class postgres_database(database):
    def __init__(self):
        pass

    def fingerprint_to_database(self,SongName,Audio):
        con = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

        cur = con.cursor()
        peaks = Audio.fingerprint(SongName, False)

        cur.execute('select id from audio where name=\'{}\''.format(SongName))
        names = cur.fetchall()
        # print("select id from audio where name=\'{}\'".format(SongName))
        if(len(names)==0):
            cur.execute("insert into audio(name) values (\'{}\');".format(SongName))
            cur.execute("select id from audio where name=\'{}\'".format(SongName))
            names = cur.fetchall()
            id = names[0][0]
            for i in range(len(peaks)):
                cur.execute('insert into hashvalues(hash,audio_id,position) values (\'{}\',{},{})'.format(peaks[i],id,i))
        con.commit()
        cur.close()
        con.close()

    def record_result_from_database(self,Audio):
        con = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"

        )
        cur = con.cursor()
        dict = collections.defaultdict(list)
        songs_found = []
        peaks = Audio.fingerprint("", True)
        for peak in peaks:
            cur.execute('select audio_id,position from hashvalues where hash=\'{}\''.format(peak))
            rows = cur.fetchall()
            for element in rows:
                dict[element[0]].append([element[1],peak])
                songs_found.append(element[0])
        songs_found = set(songs_found)
        songs_found = (list(songs_found))
        result = [peaks]
        for song in songs_found:
            dict[song].sort()
            temp = []
            for element in dict[song]:
                temp.append(element[1])
            result.append(temp)
        cur.close()
        con.close()
        return result, songs_found