import os
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_CONNECTION = os.getenv("DATABASE_CONNECTION")

db = SQLAlchemy()
database_name = "casting_agency"
database_path = DATABASE_URL.format(DATABASE_CONNECTION, database_name)


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgres://u8dbcmqtk3uthk:p34ee9f2f4a62dffe0fe7b5943177542e64b1b99cd4ff7afd2ce60d411d575ab6@cc0gj7hsrh0ht8.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d6jud581qnlmqr"
    )
    db.app = app
    app.app_context().push()
    Migrate(app, db)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Movie(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), unique=True)
    release_date = Column(DateTime(timezone=True))

    def format(self):
        return {"id": self.id, "title": self.title, "release_date": self.release_date}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.format())


class Actor(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True)
    age = Column(Integer)
    gender = Column(Boolean)

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.format())
