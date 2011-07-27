"""The sqlalchemy model definitions for the tables in the movies.db file

movies.db is the sakila sample database from mysql but ported over to work on
sqlite as best as I cared to port it.


"""
from datetime import datetime
from sqlalchemy import create_engine

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import ForeignKey
from sqlalchemy import Table

from sqlalchemy.orm import Query
from sqlalchemy.orm import relation
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///movies.db', echo=True)

# create a configured "Session" class
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

Base = declarative_base()
Base.metadata.bind = engine

# turns docs Session.query(User) into User.query
Base.query = Session.query_property(Query)

# create a Session
session = Session()

"""
Actors and Films are a many->many

To build this we need a central table to hold references to each

"""
film_actor = Table('film_actor', Base.metadata,
    Column('actor_id', Integer, ForeignKey('actor.actor_id'), primary_key=True),
    Column('film_id', Integer, ForeignKey('film.film_id'), primary_key=True)
)


"""
Actor

actor_id SMALLINT UNSIGNED NOT NULL ,
first_name VARCHAR(45) NOT NULL,
last_name VARCHAR(45) NOT NULL,
last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
PRIMARY KEY  (actor_id)

"""
class Actor(Base):
    __tablename__ = 'actor'

    actor_id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(Unicode(45), nullable=False)
    last_name = Column(Unicode(45), nullable=False)
    last_update = Column(DateTime, default=datetime.now)


"""
Language 

Notice this is related to the Film

  language_id INTEGER,
  name CHAR(20) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

"""
class Language(Base):
    __tablename__ = 'language'

    language_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(20), nullable=False)
    last_update = Column(DateTime, default=datetime.now)

"""
Film

  film_id SMALLINT UNSIGNED NOT NULL ,
  title VARCHAR(255) NOT NULL,
  description TEXT DEFAULT NULL,
  release_year YEAR DEFAULT NULL,
  language_id TINYINT UNSIGNED NOT NULL,
  original_language_id TINYINT UNSIGNED DEFAULT NULL,
  rental_duration TINYINT UNSIGNED NOT NULL DEFAULT 3,
  rental_rate DECIMAL(4,2) NOT NULL DEFAULT 4.99,
  length SMALLINT UNSIGNED DEFAULT NULL,
  replacement_cost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
  rating VARCHAR(10) DEFAULT 'G',
  special_features VARCHAR(30) DEFAULT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
  PRIMARY KEY  (film_id)
);

"""
class Film(Base):
    __tablename__ = 'film'

    film_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    description = Column(UnicodeText)
    release_year = Column(Integer)
    language_id = Column(Integer, nullable=False)
    original_language_id = Column(Integer, nullable=False)
    rental_duration = Column(Integer, nullable=False, default='3')
    rental_rate = Column(Float(2), nullable=False, default='4.99')
    length = Column(Integer)
    replacement_cost = Column(Float(2), nullable=False, default='19.99')
    rating = Column(Unicode, default=u'G')
    special_features = Column(Unicode)
    last_update = Column(DateTime, default=datetime.now)

    actors = relation(Actor,
        backref="films",
        secondary=film_actor,
    )
