from psycopg2 import sql
from coolapp import db
class NotesRepository:
    @staticmethod
    def create_note(title, text):
        with db.cursor() as cursor:
            db.autocommit = True
            values = [
                (title, text)
            ]
            insert = sql.SQL(
                'INSERT INTO notes (title, text) VALUES {}').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(insert)
        print("asdasd")
    @staticmethod
    def get_all_notes():
        ret = {}
        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM notes;')
            for row in cursor:
                ret[row[0]] = {
                    'title': row[1],
                    'text': row[2]
                }
        return ret
    @staticmethod
    def get_note(line_id):
        ret = {}
        with db.cursor() as cursor:
            values = [ line_id ]
            select = sql.SQL(
                'SELECT * FROM notes WHERE notes.id = {}').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(select)
            for row in cursor:
              ret[row[0]] = {
                  'title': row[1],
                  'text': row[2]
              }
        return ret
