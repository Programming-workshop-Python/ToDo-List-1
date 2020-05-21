from flask import Flask
import psycopg2


def create_app():
    app = Flask(__name__)
    return app


def create_db():
    return psycopg2.connect(
        dbname='qqcknmmy', 
        user='qqcknmmy', 
        password='Fv54tdIcdFOM-WfEmvzEtOnMJ4-2msz0', 
        host='salt.db.elephantsql.com'
    )


app = create_app()
db = create_db()
