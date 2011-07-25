.. Proposal submission template for PyOhio 2011

.. Columbus, OH July 30 - 31, 2011

.. Information at http://pyohio.org or pyohio-organizers@python.org

.. Submit by June 7, 2011 to cfp@pyohio.org

.. Template uses reStructuredText format:  http://docutils.sourceforge.net/rst.html


Presentation Title
==================

:Type: hands on tutorial

:Presenter: Rick Harding <rharding@mitechie.com>

:Python level: beginner - intermediate


Description
-----------

SqlAlchemy is one of the top 5 'must have' modules for Python. We'll go through
why you might want to use an ORM, situations to use the different layers of
SqlAlchemy, and some tips and tricks on a real sample application.


Extended description
--------------------

As a big fan of SqlAlchemy I hear people complain that the docs are hard, that
it's complicated, and some people just aren't aware of the powerful advantages
over something like Storm or the Django ORM. I hope to explain how SqlAlchemy
has various layers, why it's advantagous, and provide people with working
example code that works with a database they can take home with them. In this
way it should hopefully provide a bit more convincing than a talk where I put
slides in front of the users, but they don't get the hands/take home
experience.

Outline
-------

My plan is to go through the basics of SqlAlchemy in the first hour or just
over:

- Why use an ORM
  - portability
  - speed of testing
  - easier to read code
- SqlAlchemy Intro: Demo uses and examples of each
  - raw sql
  - sql expression language
  - declarative ORM
- Intermediate features
  - Relations
    - one to many
    - many to many
    - one to one
  - More advanced items
    - Inheritance mappings

- Hands on application time
  - Classroom helper
    - Provided a sample sqlite database let's work together on adding some
      sqlalchemy models to be able to list/query teachers, students, and
      grades.
    - This should provide some examples of the declarative ORM, build
      realtions, and try to fit in some examples of events.


Bio
---
Rick Harding is a software developer for Michigan based Market Research company
Morpace, is an lover of all things Web, and wishes everyone else thought tiling
window managers and ZSH were so awesome. He's also the developer of an OSS
Delicious alternative Bookie. @mitechie && http://bmark.us


Recording release
-----------------

I will sign the recording release agreement (text at http://wiki.python.org/moin/PyOhio/RecordingRelease).


.. Email to to cfp@pyohio.org by June 3, 2011

