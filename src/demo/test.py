#!/usr/bin/env python
from models import Actor
from models import Category
from models import Film
from models import Language


from models import session


def plog(out):
    """Pretty print stuff with some spacing/etc"""
    print out
    print "\n\n"


"""
Let's play with the database and models


"""

actors = Actor.query.all()
plog("Actor Count: {0} ".format(len(actors)))

ct = Actor.query.count()
plog("Actor Count via .count(): {0} ".format(ct))

# inserting a record
rick = Actor()
rick.first_name = "Rick"
rick.last_name = "Harding"

session.add(rick)

# notice that we flush here, but we don't commit. The change won't actually
# make it to the db so when we rerun this script, it'll still report 200/201
session.flush()

ct = Actor.query.count()
plog("Inserted Rick, New Count: {0} ".format(ct))

session.delete(rick)
session.flush()

ct = Actor.query.count()
plog("Deleted Rick, New Count: {0} ".format(ct))

# test the language models
lg = Language.query.all()
plog("Languages: {0}".format(", ".join([l.name for l in lg])))


# test the relation between actor/film
some_actor = Actor.query.filter(Actor.actor_id == 11).first()
plog("Actor {0}".format(some_actor.last_name))
plog("Actor {0} was in {1}".format(
        some_actor.last_name,
        ", ".join([f.title for f in some_actor.films])))

# get the list of categories
cats = Category.query.all()
plog("Categories: {0}".format(", ".join([c.name for c in cats])))

travel_id = Category.query.filter(Category.name == "Travel").first()
travels = Film.query.filter(Film.categories.any(name='Travel')).all()
plog("Travels: {0}".format(", ".join([t.title for t in travels])))
