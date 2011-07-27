#!/usr/bin/env python
"""
Follow the description and see if you can adjust the code to work


We'll start you off with some imports and samples


"""
from models import Actor
from models import Language
from models import session

def plog(out):
    """Pretty print stuff with some spacing/etc"""
    print out
    print "\n\n"


"""
Demo:

Find out how many actors there are in the database

"""
actors = Actor.query.all()
plog("Actor Count: {0} ".format(len(actors)))


"""
Now figure it out a second method

if you used python above, try using SQL and
if you used SQL previous, try using Python

"""
ct = Actor.query.count()
plog("Actor Count via .count(): {0} ".format(ct))


"""
Demo #2

Add a new Actor to the database
Verify that it's added

"""
rick = Actor()
rick.first_name = "Rick"
rick.last_name = "Harding"

session.add(rick)
# notice that we flush here, but we don't commit. The change won't actually
# make it to the db so when we rerun this script, it'll still report 200/201
session.flush()

ct = Actor.query.count()
plog("Inserted Rick, New Count: {0} ".format(ct))

"""
Homework:

Film and Actors are a many-> many relation

Find any actor and then list out the title's of the films they were a part of

Part B: Once you've done that, find the record for one of the films and see
what other actors were a part of it.

"""





"""
Homework:

The film table has two references to the language table.

Add a relation for these two columns (langauge_id, original_language_id)
and then query the films for records where the language and original_lanuage
are different

Hint: You'll need to add two relations to the Film object

"""


"""
Homework:




"""
