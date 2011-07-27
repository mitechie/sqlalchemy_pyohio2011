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
Homework

Now that the new actor 'Rick' is added, remove him and verify that you get back
200 actors in the database
"""


"""
Homework:

Tweak the actor class and add some helpful methods for:

a. Display the actors full name via a single method

"""


"""
Homework:

Add an ActorMgr class that can find Actors by first name, last name, or a
partial character search (e.g. actors with 'rod' in the first or last name)
"""


"""
Homework:

Film and Actors are a many-> many relation

Find any actor and then list out the title's of the films they were a part of

Part B: Once you've done that, find the record for one of the films and see
what other actors were a part of it.
"""


"""
Homework:

Films have a category they fall into such as Drama, Comedy, Family...

Find the titles of all of the films that are in the Category of Travel

Hint: See the end of the ORM tutorial:
    http://www.sqlalchemy.org/docs/orm/tutorial.html
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

Add a FilmMgr class with a method to return a list of the films where the
language  does not equal the original language. Basically we want to wrap the
above query into a nice reusable function call
"""


"""
Homework:

There are tables for customer and for store. Add models in the models.py for
these two tables. You also want to add the relation between them.

Once those are added, prove the relation works by displaying each store and the
number of customers there are for each store
"""


"""
Homework:

Since we have stores and customers, we next need to add a model for the rental
table. Once that's working, we want to display the top 5 customers ordered by
their number of rentals
"""


"""
Homework:

Next we want to add a model for the inventory table.

This table allows us to tell which films are available in which stores.
We want to also tie this to the rental table and get a list of the most and
least rented films.

Hint: There are two stores, so make sure you check rentals across both stores
"""


"""
Homework:

We now want to add a RentalMgr class and add a method to display all rentals
for a given date

Hint: SqlAlchemy loves datetime objects
Hint2: The sample data is old, make sure you check 2005-08-21 though the 23rd
"""
